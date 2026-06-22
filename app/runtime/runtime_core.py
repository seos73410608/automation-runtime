from app.runtime.pipeline_loader import PipelineLoader
from app.runtime.step_executor import StepExecutor
from app.runtime.step_context import StepContext

from app.db.database import SessionLocal
from app.utils.logger import logger


class RuntimeCore:

    def __init__(self):

        self.db = SessionLocal()

        self.pipeline_loader = PipelineLoader(
            self.db
        )

        # DB 주입
        self.step_executor = StepExecutor(
            self.db
        )

    def execute(self, job_name, context: StepContext):

        try:

            logger.info(
                f"[RuntimeCore] START job_name={job_name}"
            )

            # Pipeline Load
            steps = self.pipeline_loader.load(
                job_name
            )

            if not steps:
                raise ValueError(
                    f"No pipeline found: {job_name}"
                )

            logger.info(
                f"[RuntimeCore] steps loaded: {len(steps)}"
            )

            # Step Loop
            for step in steps:

                logger.info(
                    f"[STEP] order={step.step_order} "
                    f"type={step.step_type}"
                )

                context = self.step_executor.execute(
                    step,
                    context
                )

            logger.info(
                f"[RuntimeCore] FINISH job_name={job_name}"
            )

            return context

        except Exception as e:

            logger.exception(
                f"[RuntimeCore ERROR] "
                f"job_name={job_name} "
                f"error={str(e)}"
            )

            raise

        finally:

            logger.info(
                "[RuntimeCore] DB CLOSE"
            )

            self.db.close()