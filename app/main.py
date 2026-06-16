from app.jobs.job_registry import JOB_REGISTRY

from app.presenters.job_result_presenter import (
    print_result
)


def main():

    job_name = "repair_pending"

    job = JOB_REGISTRY[job_name]()

    result = job.execute()

    print_result(result)


if __name__ == "__main__":
    main()
