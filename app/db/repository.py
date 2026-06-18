from sqlalchemy.orm import Session

from app.db.models import (
    AutomationJob,
    AutomationJobHistory
)


class AutomationRepository:

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def create_job(
        self,
        job: AutomationJob
    ):

        self.db.add(job)

        self.db.commit()

        self.db.refresh(job)

        return job

    def update_job_status(
        self,
        job_id: str,
        status: str
    ):

        job = (
            self.db.query(
                AutomationJob
            )
            .filter(
                AutomationJob.job_id == job_id
            )
            .first()
        )

        if not job:

            return None

        job.status = status

        self.db.commit()

        self.db.refresh(job)

        return job

    def insert_history(
        self,
        history: AutomationJobHistory
    ):

        self.db.add(history)

        self.db.commit()

        self.db.refresh(history)

        return history

    def find_job(
        self,
        job_id: str
    ):

        return (
            self.db.query(
                AutomationJob
            )
            .filter(
                AutomationJob.job_id == job_id
            )
            .first()
        )

    def find_history(
        self,
        job_id: str
    ):

        return (
            self.db.query(
                AutomationJobHistory
            )
            .filter(
                AutomationJobHistory.job_id == job_id
            )
            .order_by(
                AutomationJobHistory.created_at
            )
            .all()
        )