import uuid

from app.jobs.base_job import BaseJob

from app.excel.excel_reader import read_excel
from app.excel.excel_exporter import export_excel

from app.rules.repair_pending_rule import (
    filter_pending,
    group_by_vendor
)

from app.utils.zip_creator import create_zip
from app.utils.logger import logger

from app.models.job_result import JobResult

from app.config.settings import (
    JOB_REPAIR_PENDING,
    TO_EMAIL
)

from app.mail.mail_sender import send_mail

from app.mail.mail_template import (
    build_subject,
    build_body
)

from app.db.database import SessionLocal

from app.db.models import (
    AutomationJob,
    AutomationJobHistory
)

from app.db.repository import AutomationRepository

from app.constants.job_status import (
    STATUS_RUNNING,
    STATUS_SUCCESS,
    STATUS_FAILED
)

from app.constants.job_step import (
    STEP_READ_EXCEL,
    STEP_FILTER,
    STEP_GROUP,
    STEP_EXPORT,
    STEP_ZIP,
    STEP_MAIL
)


class RepairPendingJob(BaseJob):

    def execute(
        self,
        file_name: str
    ):

        db = SessionLocal()

        repo = AutomationRepository(db)

        job_id = str(
            uuid.uuid4()
        )

        try:

            job = AutomationJob(
                job_id=job_id,
                file_name=file_name,
                status=STATUS_RUNNING,
                total_rows=0,
                vendor_count=0
            )

            repo.create_job(job)

            # READ_EXCEL
            df = read_excel()

            repo.insert_history(
                AutomationJobHistory(
                    job_id=job_id,
                    step_name=STEP_READ_EXCEL,
                    status=STATUS_SUCCESS,
                    message=f"{len(df)} rows loaded"
                )
            )

            # FILTER
            filtered = filter_pending(df)

            repo.insert_history(
                AutomationJobHistory(
                    job_id=job_id,
                    step_name=STEP_FILTER,
                    status=STATUS_SUCCESS,
                    message=f"{len(filtered)} rows matched"
                )
            )

            # GROUP
            groups = group_by_vendor(filtered)

            repo.insert_history(
                AutomationJobHistory(
                    job_id=job_id,
                    step_name=STEP_GROUP,
                    status=STATUS_SUCCESS,
                    message=f"{len(groups)} vendors grouped"
                )
            )

            # EXPORT
            files = export_excel(groups)

            repo.insert_history(
                AutomationJobHistory(
                    job_id=job_id,
                    step_name=STEP_EXPORT,
                    status=STATUS_SUCCESS,
                    message=f"{len(files)} files created"
                )
            )

            # ZIP
            zip_path = create_zip(files)

            repo.insert_history(
                AutomationJobHistory(
                    job_id=job_id,
                    step_name=STEP_ZIP,
                    status=STATUS_SUCCESS,
                    message=zip_path
                )
            )

            subject = build_subject(
                JOB_REPAIR_PENDING
            )

            body = build_body(
                job_name=JOB_REPAIR_PENDING,
                total_rows=len(df),
                filtered_rows=len(filtered),
                vendor_count=len(groups),
                file_count=len(files)
            )

            # MAIL
            try:

                send_mail(
                    subject=subject,
                    body=body,
                    attachment_path=zip_path
                )

                repo.insert_history(
                    AutomationJobHistory(
                        job_id=job_id,
                        step_name=STEP_MAIL,
                        status=STATUS_SUCCESS,
                        message=f"mail sent to {TO_EMAIL}"
                    )
                )

            except Exception as mail_error:

                repo.insert_history(
                    AutomationJobHistory(
                        job_id=job_id,
                        step_name=STEP_MAIL,
                        status=STATUS_FAILED,
                        message=str(mail_error)
                    )
                )

                raise

            job.total_rows = len(df)
            job.vendor_count = len(groups)
            job.status = STATUS_SUCCESS

            db.commit()

            return JobResult(
                job_name=JOB_REPAIR_PENDING,
                total_rows=len(df),
                filtered_rows=len(filtered),
                vendor_count=len(groups),
                output_file_count=len(files),
                zip_file_path=zip_path,
                success=True,
                message="처리 완료"
            )

        except Exception as e:

            logger.exception(e)

            try:

                repo.update_job_status(
                    job_id,
                    STATUS_FAILED
                )

                repo.insert_history(
                    AutomationJobHistory(
                        job_id=job_id,
                        step_name="ERROR",
                        status=STATUS_FAILED,
                        message=str(e)
                    )
                )

            except Exception:
                pass

            return JobResult(
                job_name=JOB_REPAIR_PENDING,
                total_rows=0,
                filtered_rows=0,
                vendor_count=0,
                output_file_count=0,
                zip_file_path="",
                success=False,
                message=str(e)
            )

        finally:

            db.close()
