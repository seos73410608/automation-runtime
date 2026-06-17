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


class RepairPendingJob(BaseJob):

    def execute(self):

        try:

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
