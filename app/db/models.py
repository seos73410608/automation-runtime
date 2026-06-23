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


class JobConfig(Base):

    __tablename__ = "tb_job_config"

    config_id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    job_name = Column(
        String(100),
        nullable=False
    )

    input_source_type = Column(
        String(50),
        nullable=False
    )

    output_format = Column(
        String(20)
    )

    output_path = Column(
        String(500)
    )

    file_name_pattern = Column(
        String(255)
    )

    retention_days = Column(
        Integer
    )

    email_enabled = Column(
        String(1)
    )

    email_receiver = Column(
        String(255)
    )

    enabled = Column(
        String(1)
    )

    description = Column(
        String(500)
    )

    version = Column(
        String(20)
    )

    execution_mode = Column(
        String(20)
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


class ExecutionPipeline(Base):

    __tablename__ = "tb_execution_pipeline"

    pipeline_id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    step_order = Column(
        Integer,
        nullable=False
    )

    step_type = Column(
        String(50),
        nullable=False
    )

    step_config = Column(
        Text
    )

    enabled = Column(
        String(1)
    )

    config_id = Column(
        BigInteger,
        ForeignKey(
            "tb_job_config.config_id"
        )
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

    cron_expression = Column(
        String(100),
        nullable=False
    )

    input_file_path = Column(
        String(500),
        nullable=True
    )

    config_id = Column(
        BigInteger,
        ForeignKey(
            "tb_job_config.config_id"
        )
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