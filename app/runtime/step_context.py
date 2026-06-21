from dataclasses import dataclass


@dataclass
class StepContext:

    job_id: str
    file_name: str
    file_path: str
    data: any = None
