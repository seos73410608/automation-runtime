from app.rules.rule_group_executor import RuleGroupExecutor
from app.rules.rule_repository import RuleRepository


class RuleService:

    def __init__(self, db):
        self.rule_repository = RuleRepository(db)

    def execute(self, job_name: str, df):

        # 1. DB에서 그룹 리스트 조회
        rule_groups = self.rule_repository.find_by_job_name(job_name)

        if not rule_groups:
            return None

        final_mask = None

        # -----------------------------------
        # 2. Group 단위 실행
        # -----------------------------------
        for group in rule_groups:

            group_mask = RuleGroupExecutor.execute(df, group)

            # 첫 그룹 초기화
            if final_mask is None:
                final_mask = group_mask

            # 그룹 간 OR merge (핵심 변경 포인트)
            else:
                final_mask = final_mask | group_mask

        return final_mask
