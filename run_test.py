from app.runtime.runtime_service import RuntimeService
from app.runtime.step_context import StepContext
from app.utils.logger import logger


def main():

    runtime = RuntimeService()

    logger.info("[RUN TEST] START repair_pending job")

    context = StepContext(
        job_id="test-006",
        file_name="A_S접수현황.xls",
        file_path="C:/SeoS/Claude/sample/A_S접수현황.xls"
    )

    try:

        result = runtime.execute(
            job_name="repair_pending",
            job_id=context.job_id,
            file_name=context.file_name,
            file_path=context.file_path
        )

        logger.info(f"[RUN TEST] RESULT = {result}")

        print(result)

    except Exception as e:

        logger.exception(f"[RUN TEST ERROR] {str(e)}")

        raise

    finally:

        logger.info("[RUN TEST] END")


if __name__ == "__main__":
    main()
