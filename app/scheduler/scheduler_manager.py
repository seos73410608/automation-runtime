import uuid

from pathlib import Path
from datetime import datetime

from app.db.models import (
    ScheduleExecution
)

from apscheduler.schedulers.background import (
    BackgroundScheduler
)

from apscheduler.triggers.cron import (
    CronTrigger
)

from app.db.database import SessionLocal
from app.db.repository import AutomationRepository

from app.jobs.job_registry import (
    JOB_REGISTRY
)


class SchedulerManager:

    def __init__(self):

        self.scheduler = (
            BackgroundScheduler()
        )

    def start(self):

        db = SessionLocal()

        try:

            repo = AutomationRepository(db)

            schedules = (
                repo.get_enabled_schedules()
            )

            for schedule in schedules:

                self.register_schedule(
                    schedule
                )

            self.scheduler.start()

            print(
                "[INFO] Scheduler started"
            )

        finally:

            db.close()

    def register_schedule(
        self,
        schedule
    ):

        self.scheduler.add_job(
            func=self.execute_schedule,
            trigger=CronTrigger.from_crontab(
                schedule.cron_expression
            ),
            args=[
                schedule.schedule_id
            ],
            id=str(
                schedule.schedule_id
            ),
            replace_existing=True
        )

        print(
            f"[INFO] Register Schedule : "
            f"{schedule.schedule_name}"
        )

    def execute_schedule(
        self,
        schedule_id: int
    ):

        print(
            f"[INFO] Execute Schedule : "
            f"{schedule_id}"
        )

        db = SessionLocal()

        try:

            repo = AutomationRepository(db)

            schedule = (
                repo.find_schedule(
                    schedule_id
                )
            )

            if not schedule:

                print(
                    "[ERROR] Schedule not found"
                )

                return

            execution = (
                repo.create_schedule_execution(
                    ScheduleExecution(
                        schedule_id=schedule_id,
                        status="RUNNING",
                        started_at=datetime.now()
                    )
                )
            )

            try:

                print(
                    f"[INFO] Run Job : "
                    f"{schedule.job_name}"
                )

                job_class = (
                    JOB_REGISTRY.get(
                        schedule.job_name
                    )
                )

                if not job_class:

                    raise Exception(
                        f"Unknown Job : "
                        f"{schedule.job_name}"
                    )

                if not Path(
                    schedule.input_file_path
                ).exists():

                    raise FileNotFoundError(
                        f"Input file not found : "
                        f"{schedule.input_file_path}"
                    )

                job_id = str(
                    uuid.uuid4()
                )

                job_instance = (
                    job_class()
                )

                result = (
                    job_instance.execute(
                        job_id=job_id,
                        file_name=Path(
                            schedule.input_file_path
                        ).name,
                        file_path=(
                            schedule.input_file_path
                        )
                    )
                )

                execution.job_id = job_id
                execution.status = "SUCCESS"
                execution.finished_at = (
                    datetime.now()
                )

                if hasattr(
                    result,
                    "message"
                ):
                    execution.message = (
                        result.message
                    )

                db.commit()

                print(
                    f"[INFO] Schedule Success : "
                    f"{schedule.schedule_name}"
                )

            except Exception as e:

                execution.status = "FAILED"
                execution.finished_at = (
                    datetime.now()
                )
                execution.message = str(e)

                db.commit()

                print(
                    f"[ERROR] {e}"
                )

        finally:

            db.close()

    def shutdown(self):

        self.scheduler.shutdown()
