from app.scheduler.scheduler_manager import (
    SchedulerManager
)


def main():

    scheduler = SchedulerManager()

    scheduler.execute_schedule(
        schedule_id=1
    )


if __name__ == "__main__":

    main()
