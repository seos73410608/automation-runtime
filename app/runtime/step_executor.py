import json
import time

from app.excel.excel_reader import read_excel
from app.excel.excel_exporter import export_excel

from app.services.rule_service import RuleService
from app.rules.repair_pending_rule import group_by_vendor

from app.utils.zip_creator import create_zip
from app.mail.mail_sender import send_mail
from app.mail.mail_template import build_subject, build_body

from app.config.settings import (
    JOB_REPAIR_PENDING,
    TO_EMAIL
)

from app.constants.job_step import (
    STEP_READ_EXCEL,
    STEP_FILTER,
    STEP_GROUP,
    STEP_EXPORT,
    STEP_ZIP,
    STEP_MAIL
)

from app.utils.logger import logger


class StepExecutor:

    def __init__(self, db=None):
        self.db = db

    def execute(self, step, context):

        step_type = step.step_type
        config = step.step_config

        start_time = time.time()

        # =========================
        # CONFIG PARSE (SAFE)
        # =========================
        try:
            if isinstance(config, str):
                config = json.loads(config)
        except Exception as e:
            logger.error(f"[CONFIG ERROR] step={step_type}, error={str(e)}")
            config = {}

        logger.info(f"[STEP START] type={step_type}, config={config}")

        try:

            # =========================
            # ROUTER
            # =========================
            if step_type == STEP_READ_EXCEL or step_type == "SOURCE":
                context = self._run_source(config, context)

            elif step_type == STEP_FILTER or step_type == "RULE":
                context = self._run_rule(config, context)

            elif step_type == STEP_GROUP or step_type == "PROCESS":
                context = self._run_process(config, context)

            elif step_type == STEP_EXPORT:
                context = self._run_export(config, context)

            elif step_type == STEP_ZIP:
                context = self._run_zip(config, context)

            elif step_type == STEP_MAIL or step_type == "DELIVERY":
                context = self._run_delivery(config, context)

            elif step_type == "HISTORY":
                context = self._run_history(config, context)

            else:
                logger.warning(f"[STEP UNKNOWN] type={step_type}")

            return context

        except Exception as e:

            logger.exception(f"[STEP FAIL] type={step_type}, error={str(e)}")

            # STEP6 핵심: context 안정성 유지
            context.error = str(e)
            context.failed_step = step_type

            return context

        finally:

            duration = time.time() - start_time
            logger.info(f"[STEP END] type={step_type}, duration={round(duration, 3)}s")

    # =========================================================
    # 1. SOURCE
    # =========================================================
    def _run_source(self, config, context):

        df = read_excel(context.file_path)

        context.data = df

        logger.info(f"[SOURCE] rows={len(df)}")

        return context

    # =========================================================
    # 2. RULE
    # =========================================================
    def _run_rule(self, config, context):

        rule_service = RuleService(self.db)

        mask = rule_service.execute(
            JOB_REPAIR_PENDING,
            context.data
        )

        context.data = context.data[mask]

        logger.info(f"[RULE] rows={len(context.data)}")

        return context

    # =========================================================
    # 3. PROCESS
    # =========================================================
    def _run_process(self, config, context):

        context.data = group_by_vendor(context.data)

        logger.info(f"[PROCESS] vendors={len(context.data)}")

        return context

    # =========================================================
    # 4. EXPORT
    # =========================================================
    def _run_export(self, config, context):

        output_path = config.get("output_path", "output/")

        files = export_excel(
            context.data,
            output_path
        )

        context.data = files

        logger.info(f"[EXPORT] files={len(files)}")

        return context

    # =========================================================
    # 5. ZIP
    # =========================================================
    def _run_zip(self, config, context):

        output_path = config.get("output_path", "output/")

        zip_path = create_zip(
            context.data,
            output_path
        )

        context.data = zip_path

        logger.info(f"[ZIP] path={zip_path}")

        return context

    # =========================================================
    # 6. DELIVERY
    # =========================================================
    def _run_delivery(self, config, context):

        subject = build_subject(JOB_REPAIR_PENDING)

        body = build_body(
            job_name=JOB_REPAIR_PENDING,
            total_rows=getattr(context, "total_rows", 0),
            filtered_rows=getattr(context, "filtered_rows", 0),
            vendor_count=getattr(context, "vendor_count", 0),
            file_count=len(context.data) if isinstance(context.data, list) else 1
        )

        send_mail(
            subject=subject,
            body=body,
            attachment_path=context.data
        )

        logger.info(f"[MAIL] sent={TO_EMAIL}")

        return context

    # =========================================================
    # 7. HISTORY
    # =========================================================
    def _run_history(self, config, context):

        logger.info("[HISTORY] executed (stub)")

        return context
