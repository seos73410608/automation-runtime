from app.cli.argument_parser import parse_args

from app.jobs.job_registry import JOB_REGISTRY

from app.presenters.job_result_presenter import (
    print_result
)

from app.utils.logger import logger


def main():

    args = parse_args()

    job_name = args.job

    if job_name not in JOB_REGISTRY:

        logger.error(
            f"지원하지 않는 Job: {job_name}"
        )

        logger.info("사용 가능 Job 목록")

        for name in JOB_REGISTRY:
            logger.info(f" - {name}")

        return

    job = JOB_REGISTRY[job_name]()

    result = job.execute()

    print_result(result)


if __name__ == "__main__":
    main()
