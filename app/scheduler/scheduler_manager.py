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
                        status="RUNNING"
                    )
                )
            )

            try:

                print(
                    f"[INFO] Run Job : "
                    f"{schedule.job_name}"
                )

                # TODO
                # 실제 Job 실행 연결
                #
                # if schedule.job_name == "repair_pending":
                #     RepairPendingJob().execute(...)

                repo.update_schedule_execution(
                    execution.execution_id,
                    "SUCCESS"
                )

            except Exception as e:

                repo.update_schedule_execution(
                    execution.execution_id,
                    "FAILED",
                    str(e)
                )

        finally:

            db.close()

    def shutdown(self):

        self.scheduler.shutdown()
