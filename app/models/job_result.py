from dataclasses import dataclass

@dataclass
class JobResult:

    job_name: str

    total_rows: int

    filtered_rows: int

    vendor_count: int

    output_file_count: int

    zip_file_path: str

    success: bool

    message: str