from sqlalchemy import text

from app.utils.logger import logger


class HistoryWriter:

    def __init__(self, db):
        self.db = db

    def write(self, context):

        status = "SUCCESS"

        if context.error:
            status = "FAIL"

        message = (
            f"rows={context.filtered_rows}, "
            f"vendors={context.vendor_count}, "
            f"files={context.output_file_count}"
        )

        sql = """
            INSERT INTO tb_automation_job_history
            (
                job_id,
                step_name,
                status,
                message
            )
            VALUES
            (
                :job_id,
                :step_name,
                :status,
                :message
            )
        """

        self.db.execute(
            text(sql),
            {
                "job_id": context.job_id,
                "step_name": "JOB_FINISHED",
                "status": status,
                "message": message
            }
        )

        self.db.commit()

        logger.info(
            f"[HISTORY WRITER] saved "
            f"job_id={context.job_id}"
        )