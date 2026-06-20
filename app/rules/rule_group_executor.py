from app.constants.rule_logic import RuleLogic
from app.rules.rule_executor import RuleExecutor
from app.rules.rule_group_model import RuleGroupModel


class RuleGroupExecutor:

    @staticmethod
    def execute(df, rule_group: RuleGroupModel):

        if not rule_group.rules:
            raise ValueError(
                "RuleGroup must contain at least one rule."
            )

        result_mask = RuleExecutor.execute(
            df,
            rule_group.rules[0]
        )

        for rule in rule_group.rules[1:]:

            current_mask = RuleExecutor.execute(
                df,
                rule
            )

            if rule_group.logic_type == RuleLogic.AND:

                result_mask = (
                    result_mask & 
                    current_mask
                )

            elif rule_group.logic_type == RuleLogic.OR:

                result_mask = (
                    result_mask | 
                    current_mask
                )

            else:

                raise ValueError(
                    f"Unsupported logic type: "
                    f"{rule_group.logic_type}"
                )

        return result_mask
