from app.runtime.job_factory import JobFactory


class RuntimeService:

    def execute(
        self,
        job_name: str,
        job_id: str,
        file_name: str,
        file_path: str
    ):

        job = JobFactory.get(job_name)

        return job.execute(
            job_id=job_id,
            file_name=file_name,
            file_path=file_path
        )
