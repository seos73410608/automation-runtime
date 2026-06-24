from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ExecutionLogModel:

    job_id: str

    config_id: Optional[int]
    job_name: Optional[str]

    file_name: Optional[str]
    execution_mode: Optional[str]

    start_time: datetime
    end_time: datetime

    duration: float

    total_rows: int
    filtered_rows: int
    vendor_count: int
    output_file_count: int

    status: str

    error_message: Optional[str]