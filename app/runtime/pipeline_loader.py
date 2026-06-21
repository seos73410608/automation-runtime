from app.db.models import AutomationPipeline


class PipelineLoader:

    def __init__(self, db):
        self.db = db

    def load(self, job_name: str):

        """
        job_name 기준으로 pipeline step 로딩
        """

        return (
            self.db.query(AutomationPipeline)
            .filter(
                AutomationPipeline.job_name == job_name
            )
            .order_by(
                AutomationPipeline.step_order.asc()
            )
            .all()
        )
