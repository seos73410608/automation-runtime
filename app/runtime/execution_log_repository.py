from sqlalchemy import text

from app.utils.logger import logger


class ExecutionLogRepository:

    def __init__(self, db):
        self.db = db

    def save(self, context):

        sql = """
            INSERT INTO tb_runtime_execution_log
            (
                job_id,
                config_id,
                job_name,

                file_name,
                execution_mode,

                start_time,
                end_time,
                duration,

                total_rows,
                filtered_rows,
                vendor_count,
                output_file_count,

                status,
                error_message
            )
            VALUES
            (
                :job_id,
                :config_id,
                :job_name,

                :file_name,
                :execution_mode,

                :start_time,
                :end_time,
                :duration,

                :total_rows,
                :filtered_rows,
                :vendor_count,
                :output_file_count,

                :status,
                :error_message
            )
        """

        self.db.execute(
            text(sql),
            {
                "job_id": context.job_id,
                "config_id": context.config_id,
                "job_name": context.job_name,

                "file_name": context.file_name,
                "execution_mode": context.execution_mode,

                "start_time": context.start_time,
                "end_time": context.end_time,
                "duration": context.duration,

                "total_rows": context.total_rows,
                "filtered_rows": context.filtered_rows,
                "vendor_count": context.vendor_count,
                "output_file_count": context.output_file_count,
                "status": context.status,
                "error_message": (
                    context.error_message
                    or context.error
                )
            }
        )

        self.db.commit()

        logger.info(
            f"[EXECUTION LOG] saved "
            f"job_id={context.job_id}, "
            f"status={context.status}"
        )