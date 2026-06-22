from app.db.models import ExecutionPipeline
from app.utils.logger import logger


class PipelineLoader:

    def __init__(self, db):
        self.db = db

    def load(self, job_name: str):

        """
        job_name 기준으로 pipeline step 로딩
        """

        logger.info(
            f"[PIPELINE LOAD] job_name={job_name}"
        )

        steps = (
            self.db.query(ExecutionPipeline)
            .filter(
                ExecutionPipeline.job_name == job_name
            )
            .order_by(
                ExecutionPipeline.step_order.asc()
            )
            .all()
        )

        logger.info(
            f"[PIPELINE LOAD] loaded steps={len(steps)}"
        )

        return steps