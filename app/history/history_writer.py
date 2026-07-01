from sqlalchemy import text

from app.utils.logger import logger


class HistoryWriter:

    def __init__(self, db):
        self.db = db

    def write(self, context):

        #
        # 등록된 Job인지 확인
        #
        exists_sql = """
            SELECT COUNT(*)
            FROM tb_automation_job
            WHERE job_id = :job_id
        """

        logger.info(f"[DEBUG] HistoryWriter job_id={context.job_id}")

        exists = self.db.execute(
            text(exists_sql),
            {
                "job_id": context.job_id
            }
        ).scalar()

        logger.info(f"[DEBUG] exists={exists}")
        
        #
        # 등록되지 않은 Job이면 History Skip
        #
        if not exists:

            logger.info(
                f"[HISTORY WRITER] "
                f"skip job_id={context.job_id} "
                f"(not registered)"
            )

            return

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