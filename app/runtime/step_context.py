from dataclasses import dataclass
from datetime import datetime
from typing import Any
from typing import Optional


@dataclass
class StepContext:

    # =========================
    # 기본 실행 정보
    # =========================
    job_id: str
    file_name: str
    file_path: str

    # =========================
    # Runtime Data
    # =========================
    data: Any = None

    # =========================
    # Config 기반 Runtime
    # =========================
    config_id: Optional[int] = None
    job_name: Optional[str] = None

    # Job Config
    job_config: Any = None

    # Input Config
    input_config: Any = None

    # Output Config
    output_config: Any = None

    # =========================
    # 실행 시작/종료
    # =========================
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration: float = 0.0

    # =========================
    # 실행 결과 메타
    # =========================
    total_rows: int = 0
    filtered_rows: int = 0
    vendor_count: int = 0
    output_file_count: int = 0

    # =========================
    # 실행 상태
    # =========================
    status: str = "RUNNING"

    # =========================
    # 오류 처리
    # =========================
    error: Optional[str] = None
    error_message: Optional[str] = None
    failed_step: Optional[str] = None

    # =========================
    # 실행 통계
    # =========================
    execution_mode: Optional[str] = None