from app.runtime.runtime_core import RuntimeCore
from app.runtime.step_context import StepContext


class RuntimeService:

    def __init__(self):
        self.runtime_core = RuntimeCore()

    def execute(
        self,
        job_name: str,
        job_id: str,
        file_name: str,
        file_path: str
    ):

        context = StepContext(
            job_id=job_id,
            file_name=file_name,
            file_path=file_path
        )

        return self.runtime_core.execute(
            job_name,
            context
        )