from app.jobs.base_job import BaseJob

from app.models.job_result import JobResult

from app.config.settings import JOB_INBOUND_MISSING


class InboundMissingJob(BaseJob):

    def execute(self):

        return JobResult(
            job_name=JOB_INBOUND_MISSING,
            total_rows=0,
            filtered_rows=0,
            vendor_count=0,
            output_file_count=0,
            zip_file_path="",
            success=False,
            message="InboundMissingJob 구현 예정"
        )
