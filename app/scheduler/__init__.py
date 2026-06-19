from apscheduler.schedulers.background import (
    BackgroundScheduler
)

from app.db.database import SessionLocal
from app.db.repository import AutomationRepository

from app.jobs.repair_pending_job import (
    RepairPendingJob
)


class SchedulerManager:

    def __init__(self):

        self.scheduler = (
            BackgroundScheduler()
        )

    def start(self):

        self.load_schedules()

        self.scheduler.start()

        print(
            "[INFO] Scheduler Started"
        )

    def shutdown(self):

        self.scheduler.shutdown()

        print(
            "[INFO] Scheduler Stopped"
        )

    def load_schedules(self):

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

        finally:

            db.close()

    def register_schedule(
        self,
        schedule
    ):

        cron = (
            schedule.cron_expression
        )

        fields = cron.split()

        if len(fields) != 5:

            print(
                f"[ERROR] Invalid cron: {cron}"
            )

            return

        minute = fields[0]
        hour = fields[1]
        day = fields[2]
        month = fields[3]
        day_of_week = fields[4]

        self.scheduler.add_job(
            func=self.execute_schedule,
            trigger="cron",
            minute=minute,
            hour=hour,
            day=day,
            month=month,
            day_of_week=day_of_week,
            args=[schedule.schedule_id],
            id=str(
                schedule.schedule_id
            ),
            replace_existing=True
        )

        print(
            f"[INFO] Schedule Registered : "
            f"{schedule.schedule_name}"
        )

    def execute_schedule(
        self,
        schedule_id: int
    ):

        db = SessionLocal()

        try:

            repo = AutomationRepository(db)

            schedule = (
                repo.find_schedule(
                    schedule_id
                )
            )

            if not schedule:

                return

            execution = (
                repo.create_schedule_execution(
                    execution=None
                )
            )

            print(
                f"[INFO] Schedule Execute : "
                f"{schedule.schedule_name}"
            )

            if (
                schedule.job_name
                == "repair_pending"
            ):

                RepairPendingJob().execute()

            repo.update_schedule_execution(
                execution.execution_id,
                "SUCCESS"
            )

        except Exception as e:

            print(
                f"[ERROR] {e}"
            )

        finally:

            db.close()