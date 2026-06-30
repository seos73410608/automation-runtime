from app.runtime.runtime_service import RuntimeService
from app.runtime.step_context import StepContext
from app.utils.logger import logger


def main():

    runtime = RuntimeService()

    logger.info(
        "[RUN TEST] START settlement job"
    )

    context = StepContext(
        job_id="settlement-test-001",
        file_name="settlement_sample.xlsx",
        file_path=(
            "sample/settlement_sample.xlsx"
        )
    )

    try:

        result = runtime.execute(
            job_name="settlement",
            job_id=context.job_id,
            file_name=context.file_name,
            file_path=context.file_path
        )

        logger.info(
            f"[RUN TEST] RESULT = {result}"
        )

        print(result)

    except Exception as e:

        logger.exception(
            f"[RUN TEST ERROR] {str(e)}"
        )

        raise

    finally:

        logger.info(
            "[RUN TEST] END"
        )


if __name__ == "__main__":
    main()