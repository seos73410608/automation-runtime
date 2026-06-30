from app.rules.rule_group_executor import RuleGroupExecutor
from app.rules.rule_repository import RuleRepository

from app.rules.order_validation_rule_group import (
    validate_order
)

from app.rules.settlement_rule_group import (
    settlement_rule_group
)


class RuleService:

    def __init__(self, db):
        self.rule_repository = RuleRepository(db)

    def execute(self, job_name: str, df):

        # =====================================
        # v0.9.0 Order Validation
        # =====================================
        if job_name == "order_validation":

            return validate_order(df)

        # =====================================
        # v0.9.2 Settlement
        # =====================================
        if job_name == "settlement":

            return settlement_rule_group(df)

        # =====================================
        # 기존 DB Rule Engine
        # =====================================
        rule_groups = self.rule_repository.find_by_job_name(
            job_name
        )

        if not rule_groups:
            return None

        final_mask = None

        for group in rule_groups:

            group_mask = RuleGroupExecutor.execute(
                df,
                group
            )

            if final_mask is None:

                final_mask = group_mask

            else:

                final_mask = final_mask | group_mask

        return final_mask