from app.rules.rule_group_executor import RuleGroupExecutor
from app.repositories.rule_repository import RuleRepository


class RuleService:

    def __init__(self, db):

        self.rule_repository = RuleRepository(db)

    def execute(
        self,
        job_name: str,
        df
    ):

        rule_group = (
            self.rule_repository.find_by_job_name(
                job_name
            )
        )

        return RuleGroupExecutor.execute(
            df,
            rule_group
        )
