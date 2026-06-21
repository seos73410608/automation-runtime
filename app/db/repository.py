from sqlalchemy.orm import Session

from app.db.models import (
    AutomationJob,
    AutomationJobHistory,
    AutomationSchedule,
    ScheduleExecution,
    JobConfig,
    ExecutionPipeline
)


class AutomationRepository:

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    # ==================================================
    # JOB
    # ==================================================

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

    def get_jobs(self):

        return (
            self.db.query(
                AutomationJob
            )
            .order_by(
                AutomationJob.created_at.desc()
            )
            .all()
        )

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

    # ==================================================
    # JOB CONFIG
    # ==================================================

    def get_job_config(
        self,
        job_name: str
    ):

        return (
            self.db.query(
                JobConfig
            )
            .filter(
                JobConfig.job_name == job_name
            )
            .filter(
                JobConfig.enabled == "Y"
            )
            .first()
        )

    # ==================================================
    # PIPELINE
    # ==================================================

    def get_pipeline_steps(
        self,
        job_name: str
    ):

        return (
            self.db.query(
                ExecutionPipeline
            )
            .filter(
                ExecutionPipeline.job_name
                == job_name
            )
            .filter(
                ExecutionPipeline.enabled == "Y"
            )
            .order_by(
                ExecutionPipeline.step_order
            )
            .all()
        )

    # ==================================================
    # Scheduler
    # ==================================================

    def create_schedule(
        self,
        schedule: AutomationSchedule
    ):

        self.db.add(schedule)

        self.db.commit()

        self.db.refresh(schedule)

        return schedule

    def get_schedules(self):

        return (
            self.db.query(
                AutomationSchedule
            )
            .order_by(
                AutomationSchedule.schedule_id.desc()
            )
            .all()
        )

    def get_enabled_schedules(
        self
    ):

        return (
            self.db.query(
                AutomationSchedule
            )
            .filter(
                AutomationSchedule.enabled == "Y"
            )
            .all()
        )

    def find_schedule(
        self,
        schedule_id: int
    ):

        return (
            self.db.query(
                AutomationSchedule
            )
            .filter(
                AutomationSchedule.schedule_id
                == schedule_id
            )
            .first()
        )

    def create_schedule_execution(
        self,
        execution: ScheduleExecution
    ):

        self.db.add(execution)

        self.db.commit()

        self.db.refresh(execution)

        return execution

    def update_schedule_execution(
        self,
        execution_id: int,
        status: str,
        message: str=None
    ):

        execution = (
            self.db.query(
                ScheduleExecution
            )
            .filter(
                ScheduleExecution.execution_id
                == execution_id
            )
            .first()
        )

        if not execution:

            return None

        execution.status = status

        if message:
            execution.message = message

        self.db.commit()

        self.db.refresh(execution)

        return execution

    def get_schedule_executions(
        self,
        schedule_id: int
    ):

        return (
            self.db.query(
                ScheduleExecution
            )
            .filter(
                ScheduleExecution.schedule_id
                == schedule_id
            )
            .order_by(
                ScheduleExecution.created_at.desc()
            )
            .all()
        )
