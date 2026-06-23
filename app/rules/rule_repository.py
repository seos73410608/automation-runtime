from collections import defaultdict

from sqlalchemy import text

from app.constants.rule_logic import RuleLogic
from app.rules.rule_group_model import RuleGroupModel
from app.rules.rule_model import RuleModel


class RuleRepository:

    def __init__(self, db):
        self.db = db

    def find_by_job_name(self, job_name: str) -> list[RuleGroupModel]:

        # -----------------------------------
        # 1. JobConfig 조회
        # -----------------------------------
        config_sql = """
            SELECT config_id
            FROM tb_job_config
            WHERE job_name = :job_name
            LIMIT 1
        """

        config_row = self.db.execute(
            text(config_sql),
            {"job_name": job_name}
        ).mappings().first()

        if not config_row:
            raise ValueError(
                f"JobConfig not found: {job_name}"
            )

        config_id = config_row["config_id"]

        # -----------------------------------
        # 2. Rule 조회
        # -----------------------------------
        sql = """
            SELECT
                g.group_id,
                g.group_name,
                g.logic_type,
                g.execution_order AS group_order,

                d.detail_id,
                d.execution_order AS rule_order,

                r.rule_id,
                r.field_name,
                r.operator,
                r.rule_value

            FROM tb_rule_group g

            JOIN tb_rule_group_detail d
                ON g.group_id = d.group_id

            JOIN tb_rule r
                ON d.rule_id = r.rule_id

            WHERE g.config_id = :config_id
              AND g.enabled = 'Y'
              AND r.enabled = 'Y'

            ORDER BY
                g.execution_order,
                g.group_id,
                d.execution_order
        """

        result_proxy = self.db.execute(
            text(sql),
            {"config_id": config_id}
        )

        rows = result_proxy.mappings().all()

        if not rows:
            raise ValueError(
                f"No rules found for job: {job_name}"
            )

        grouped = defaultdict(list)
        group_meta = {}

        for row in rows:

            group_id = row["group_id"]

            if group_id not in group_meta:

                group_meta[group_id] = {
                    "group_name": row["group_name"],
                    "logic_type": RuleLogic(
                        row["logic_type"]
                    ),
                    "execution_order": row["group_order"]
                }

            grouped[group_id].append(
                RuleModel(
                    rule_id=row["rule_id"],
                    field_name=row["field_name"],
                    operator=row["operator"],
                    rule_value=row["rule_value"]
                )
            )

        result = []

        for group_id in sorted(
            group_meta,
            key=lambda x: group_meta[x]["execution_order"]
        ):

            meta = group_meta[group_id]

            result.append(
                RuleGroupModel(
                    job_name=job_name,
                    group_id=group_id,
                    group_name=meta["group_name"],
                    logic_type=meta["logic_type"],
                    rules=grouped[group_id]
                )
            )

        return result