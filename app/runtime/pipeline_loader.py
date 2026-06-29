from app.db.models import (
    ExecutionPipeline,
    InputConfig,
    JobConfig,
    OutputConfig
)

from app.utils.logger import logger


class PipelineLoader:

    def __init__(self, db):
        self.db = db

    def load(self, job_name: str):

        """
        job_name → config_id 변환 후

        - JobConfig
        - InputConfig
        - OutputConfig
        - ExecutionPipeline

        조회
        """

        logger.info(
            f"[PIPELINE LOAD] job_name={job_name}"
        )

        # ----------------------------------------
        # JobConfig
        # ----------------------------------------
        job_config = (
            self.db.query(JobConfig)
            .filter(
                JobConfig.job_name == job_name,
                JobConfig.enabled == "Y"
            )
            .first()
        )

        if not job_config:

            raise ValueError(
                f"JobConfig not found: {job_name}"
            )

        # ----------------------------------------
        # InputConfig
        # ----------------------------------------
        input_config = (
            self.db.query(InputConfig)
            .filter(
                InputConfig.config_id == job_config.config_id,
                InputConfig.enabled == "Y"
            )
            .first()
        )

        # ----------------------------------------
        # OutputConfig
        # ----------------------------------------
        output_config = (
            self.db.query(OutputConfig)
            .filter(
                OutputConfig.config_id == job_config.config_id,
                OutputConfig.enabled == "Y"
            )
            .first()
        )

        # ----------------------------------------
        # Pipeline
        # ----------------------------------------
        steps = (
            self.db.query(ExecutionPipeline)
            .filter(
                ExecutionPipeline.config_id == job_config.config_id,
                ExecutionPipeline.enabled == "Y"
            )
            .order_by(
                ExecutionPipeline.step_order.asc()
            )
            .all()
        )

        logger.info(
            f"[PIPELINE LOAD] loaded steps={len(steps)}"
        )

        return {
            "job_config": job_config,
            "input_config": input_config,
            "output_config": output_config,
            "steps": steps
        }