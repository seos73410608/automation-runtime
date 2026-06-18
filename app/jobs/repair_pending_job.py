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

from app.config.settings import JOB_REPAIR_PENDING

from app.mail.mail_sender import send_mail

from app.mail.mail_template import (
    build_subject,
    build_body
)

from app.db.database import SessionLocal

from app.db.models import AutomationJob

from app.db.repository import AutomationRepository


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
                status="RUNNING",
                total_rows=0,
                vendor_count=0
            )

            repo.create_job(job)

            df = read_excel()

            filtered = filter_pending(df)

            groups = group_by_vendor(filtered)

            files = export_excel(groups)

            zip_path = create_zip(files)

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

            send_mail(
                subject=subject,
                body=body,
                attachment_path=zip_path
            )

            job.total_rows = len(df)

            job.vendor_count = len(groups)

            job.status = "SUCCESS"

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

            logger.error(str(e))

            try:

                repo.update_job_status(
                    job_id,
                    "FAILED"
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