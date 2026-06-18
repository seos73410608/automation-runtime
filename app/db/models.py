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