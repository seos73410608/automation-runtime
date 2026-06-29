from app.runtime.runtime_core import RuntimeCore
from app.runtime.step_context import StepContext


class OrderValidationJob:

    def execute(
        self,
        file_path: str
    ):

        context = StepContext(
            job_id="order-validation-001",
            file_name="주문잡_20260625.xlsx",
            file_path=file_path
        )

        runtime = RuntimeCore()

        return runtime.execute(
            "order_validation",
            context
        )