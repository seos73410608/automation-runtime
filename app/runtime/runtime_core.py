from datetime import datetime

from app.runtime.pipeline_loader import PipelineLoader
from app.runtime.step_executor import StepExecutor
from app.runtime.step_context import StepContext

from app.db.database import SessionLocal
from app.utils.logger import logger

from app.runtime.execution_log_repository import (
    ExecutionLogRepository
)


class RuntimeCore:

    def __init__(self):

        self.db = SessionLocal()

        self.pipeline_loader = PipelineLoader(
            self.db
        )

        self.step_executor = StepExecutor(
            self.db
        )

    def execute(self, job_name, context: StepContext):

        try:

            logger.info(
                f"[RuntimeCore] START job_name={job_name}"
            )

            # Runtime Metadata Start
            context.job_name = job_name
            context.start_time = datetime.now()
            context.status = "RUNNING"

            # ------------------------------------
            # Pipeline Load
            # ------------------------------------
            pipeline = self.pipeline_loader.load(
                job_name
            )

            context.job_config = pipeline["job_config"]
            context.input_config = pipeline["input_config"]
            context.output_config = pipeline["output_config"]

            steps = pipeline["steps"]

            if not steps:
                raise ValueError(
                    f"No pipeline found: {job_name}"
                )

            logger.info(
                f"[RuntimeCore] steps loaded: {len(steps)}"
            )

            # ------------------------------------
            # Step Execute
            # ------------------------------------
            for step in steps:

                logger.info(
                    f"[STEP] order={step.step_order} "
                    f"type={step.step_type}"
                )

                context = self.step_executor.execute(
                    step,
                    context
                )

            # Runtime Metadata End
            context.end_time = datetime.now()

            context.duration = (
                context.end_time -
                context.start_time
            ).total_seconds()

            if context.error:

                context.status = "FAILED"

                logger.error(
                    f"[RuntimeCore] FAILED "
                    f"job_name={job_name}"
                )

            else:

                context.status = "SUCCESS"

                logger.info(
                    f"[RuntimeCore] FINISH "
                    f"job_name={job_name}"
                )

            return context

        except Exception as e:

            context.end_time = datetime.now()

            if context.start_time:

                context.duration = (
                    context.end_time -
                    context.start_time
                ).total_seconds()

            context.status = "FAILED"

            context.error_message = str(e)

            logger.exception(
                f"[RuntimeCore ERROR] "
                f"job_name={job_name} "
                f"error={str(e)}"
            )

            raise

        finally:

            try:

                ExecutionLogRepository(
                    self.db
                ).save(
                    context
                )

            except Exception as e:

                logger.exception(
                    f"[EXECUTION LOG FAIL] "
                    f"{str(e)}"
                )

            logger.info(
                "[RuntimeCore] DB CLOSE"
            )

            self.db.close()