import pandas as pd

from app.constants.rule_operator import RuleOperator
from app.rules.rule_model import RuleModel


class RuleExecutor:

    @staticmethod
    def execute(
        df: pd.DataFrame,
        rule: RuleModel
    ):

        field = rule.field_name
        operator = rule.operator
        value = rule.rule_value

        if field not in df.columns:
            raise ValueError(
                f"Field not found: {field}"
            )

        if operator == RuleOperator.IS_EMPTY:
            return df[field].isna()

        if operator == RuleOperator.IS_NOT_EMPTY:
            return df[field].notna()

        if operator == RuleOperator.EQUALS:
            return df[field] == value

        if operator == RuleOperator.NOT_EQUALS:
            return df[field] != value

        if operator == RuleOperator.CONTAINS:
            return (
                df[field]
                .fillna("")
                .astype(str)
                .str.contains(
                    str(value),
                    na=False
                )
            )

        raise ValueError(
            f"Unsupported operator: {operator}"
        )
