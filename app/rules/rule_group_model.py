from dataclasses import dataclass

from app.rules.rule_model import RuleModel


@dataclass
class RuleGroupModel:

    group_id: int

    group_name: str

    job_name: str

    logic_type: str

    rules: list[RuleModel]
