from app.constants.rule_logic import RuleLogic
from app.rules.rule_group_model import RuleGroupModel
from app.rules.rule_model import RuleModel


class RuleRepository:

    def __init__(self, db):

        self.db = db

    def find_by_job_name(
        self,
        job_name: str
    ) -> RuleGroupModel:

        sql = """
            SELECT
                g.logic_type,
                r.rule_id,
                r.field_name,
                r.operator,
                r.rule_value
            FROM tb_rule_group g
            JOIN tb_rule r
              ON g.rule_id = r.rule_id
            WHERE g.job_name = %s
              AND r.enabled = 'Y'
            ORDER BY g.execution_order
        """

        rows = self.db.execute(
            sql,
            (job_name,)
        ).fetchall()

        if not rows:

            raise ValueError(
                f"No rules found for job: {job_name}"
            )

        logic_type = RuleLogic(
            rows[0]["logic_type"]
        )

        rules = []

        for row in rows:

            rules.append(
                RuleModel(
                    rule_id=row["rule_id"],
                    field_name=row["field_name"],
                    operator=row["operator"],
                    rule_value=row["rule_value"]
                )
            )

        return RuleGroupModel(
            logic_type=logic_type,
            rules=rules
        )
