from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

from app.db.database import Base


class AutomationJob(Base):

    __tablename__ = "tb_automation_job"

    job_id = Column(
        String(64),
        primary_key=True
    )

    file_name = Column(
        String(255),
        nullable=False
    )

    status = Column(
        String(20),
        nullable=False
    )

    total_rows = Column(
        Integer,
        default=0
    )

    vendor_count = Column(
        Integer,
        default=0
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    started_at = Column(
        DateTime,
        nullable=True
    )

    finished_at = Column(
        DateTime,
        nullable=True
    )


class AutomationJobHistory(Base):

    __tablename__ = "tb_automation_job_history"

    history_id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    job_id = Column(
        String(64),
        ForeignKey(
            "tb_automation_job.job_id"
        ),
        nullable=False
    )

    step_name = Column(
        String(50),
        nullable=False
    )

    status = Column(
        String(20),
        nullable=False
    )

    message = Column(
        Text
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )


class AutomationSchedule(Base):
    
    __tablename__ = "tb_automation_schedule"

    schedule_id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    schedule_name = Column(
        String(100),
        nullable=False
    )

    job_name = Column(
        String(50),
        nullable=False
    )

    cron_expression = Column(
        String(100),
        nullable=False
    )

    input_file_path = Column(
        String(500),
        nullable=True
    )

    enabled = Column(
        String(1),
        nullable=False,
        server_default="Y"
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )


class ScheduleExecution(Base):

    __tablename__ = "tb_schedule_execution"

    execution_id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    schedule_id = Column(
        BigInteger,
        ForeignKey(
            "tb_automation_schedule.schedule_id"
        ),
        nullable=False
    )

    job_id = Column(
        String(64)
    )

    started_at = Column(
        DateTime
    )

    finished_at = Column(
        DateTime
    )

    status = Column(
        String(20)
    )

    message = Column(
        Text
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )