from app.runtime.pipeline_loader import PipelineLoader
from app.runtime.step_executor import StepExecutor
from app.runtime.step_context import StepContext

from app.db.database import SessionLocal
from app.utils.logger import logger


class RuntimeCore:

    def __init__(self):
        self.db = SessionLocal()
        self.pipeline_loader = PipelineLoader(self.db)
        self.step_executor = StepExecutor()

    def execute(self, job_name, context: StepContext):

        try:

            logger.info(f"[RuntimeCore] START job_name={job_name}")

            # 1. pipeline 로딩
            steps = self.pipeline_loader.load(job_name)

            if not steps:
                raise ValueError(f"No pipeline found: {job_name}")

            logger.info(f"[RuntimeCore] steps loaded: {len(steps)}")

            # 2. step 실행 루프
            for step in steps:

                logger.info(
                    f"[STEP] order={step.step_order} type={step.step_type}"
                )

                context = self.step_executor.execute(
                    step,
                    context
                )

            logger.info(f"[RuntimeCore] FINISH job_name={job_name}")

            return context

        except Exception as e:

            logger.exception(
                f"[RuntimeCore ERROR] job_name={job_name} error={str(e)}"
            )

            raise

        finally:
            self.db.close()
