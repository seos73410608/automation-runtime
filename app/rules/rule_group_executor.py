import pandas as pd

from app.constants.rule_logic import RuleLogic
from app.rules.rule_executor import RuleExecutor
from app.rules.rule_group_model import RuleGroupModel


class RuleGroupExecutor:

    @staticmethod
    def execute(df: pd.DataFrame, rule_group: RuleGroupModel):

        if not rule_group.rules:
            raise ValueError(
                "RuleGroup must contain at least one rule."
            )

        # 🔥 안전한 초기 mask (의존성 제거)
        result_mask = pd.Series(
            [True] * len(df),
            index=df.index
        )

        logic_type = rule_group.logic_type

        # Enum / string 둘 다 대응
        if isinstance(logic_type, RuleLogic):
            logic_type = logic_type.value

        logic_type = logic_type.upper()

        for rule in rule_group.rules:

            current_mask = RuleExecutor.execute(df, rule)

            if logic_type == RuleLogic.AND.value:

                result_mask = result_mask & current_mask

            elif logic_type == RuleLogic.OR.value:

                result_mask = result_mask | current_mask

            else:

                raise ValueError(
                    f"Unsupported logic type: {rule_group.logic_type}"
                )

        return result_mask
