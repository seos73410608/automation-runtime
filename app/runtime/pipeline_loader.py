from app.db.models import ExecutionPipeline
from app.db.models import JobConfig

from app.utils.logger import logger


class PipelineLoader:

    def __init__(self, db):
        self.db = db

    def load(self, job_name: str):

        """
        job_name → config_id 변환 후
        pipeline step 로딩
        """

        logger.info(
            f"[PIPELINE LOAD] job_name={job_name}"
        )

        # JobConfig 조회
        config = (
            self.db.query(JobConfig)
            .filter(
                JobConfig.job_name == job_name
            )
            .first()
        )

        if not config:
            raise ValueError(
                f"JobConfig not found: {job_name}"
            )

        # config_id 기반 Pipeline 조회
        steps = (
            self.db.query(ExecutionPipeline)
            .filter(
                ExecutionPipeline.config_id
                == config.config_id
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