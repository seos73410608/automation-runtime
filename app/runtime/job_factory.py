from app.jobs.repair_pending_job import RepairPendingJob


class JobFactory:

    JOBS = {
        "repair_pending": RepairPendingJob
    }

    @classmethod
    def get(cls, job_name: str):

        job_class = cls.JOBS.get(job_name)

        if not job_class:
            raise ValueError(
                f"지원하지 않는 Job : {job_name}"
            )

        return job_class()
