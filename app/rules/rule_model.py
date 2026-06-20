from dataclasses import dataclass


@dataclass
class RuleModel:

    rule_id: int

    field_name: str

    operator: str

    rule_value: str | None = None
