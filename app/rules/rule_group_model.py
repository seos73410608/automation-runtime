from dataclasses import dataclass

from app.rules.rule_model import RuleModel


@dataclass
class RuleGroupModel:

    job_name: str

    logic_type: str

    rules: list[RuleModel]
