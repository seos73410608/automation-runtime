import json
import time

from app.services.rule_service import RuleService

from app.mail.mail_template import (
    build_subject,
    build_body
)

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

from app.runtime.factory.reader_factory import (
    ReaderFactory
)

from app.runtime.factory.processor_factory import (
    ProcessorFactory
)

from app.runtime.factory.export_factory import (
    ExportFactory
)

from app.runtime.factory.delivery_factory import (
    DeliveryFactory
)

from app.utils.zip_creator import create_zip

from app.history.history_writer import HistoryWriter

class StepExecutor:

    def __init__(self, db=None):
        self.db = db

    def execute(self, step, context):

        step_type = step.step_type
        config = step.step_config

        start_time = time.time()

        try:

            if isinstance(config, str):
                config = json.loads(config)

        except Exception as e:

            logger.error(
                f"[CONFIG ERROR] "
                f"step={step_type}, "
                f"error={str(e)}"
            )

            config = {}

        logger.info(
            f"[STEP START] "
            f"type={step_type}, "
            f"config={config}"
        )

        try:

            if step_type == STEP_READ_EXCEL or step_type == "SOURCE":
                context = self._run_source(
                    config,
                    context
                )

            elif step_type == STEP_FILTER or step_type == "RULE":
                context = self._run_rule(
                    config,
                    context
                )

            elif step_type == STEP_GROUP or step_type == "PROCESS":
                context = self._run_process(
                    config,
                    context
                )

            elif step_type == STEP_EXPORT:
                context = self._run_export(
                    config,
                    context
                )

            elif step_type == STEP_ZIP:
                context = self._run_zip(
                    config,
                    context
                )

            elif step_type == STEP_MAIL or step_type == "DELIVERY":
                context = self._run_delivery(
                    config,
                    context
                )

            elif step_type == "HISTORY":
                context = self._run_history(
                    config,
                    context
                )

            else:

                logger.warning(
                    f"[STEP UNKNOWN] "
                    f"type={step_type}"
                )

            return context

        except Exception as e:

            logger.exception(
                f"[STEP FAIL] "
                f"type={step_type}, "
                f"error={str(e)}"
            )

            context.error = str(e)
            context.failed_step = step_type

            return context

        finally:

            duration = time.time() - start_time

            logger.info(
                f"[STEP END] "
                f"type={step_type}, "
                f"duration={round(duration, 3)}s"
            )

    # =========================================================
    # SOURCE
    # =========================================================
    def _run_source(self, config, context):

        reader_name = config.get(
            "reader",
            "ExcelReader"
        )

        reader = ReaderFactory.get(
            reader_name
        )

        df = reader(
            context.file_path
        )

        context.data = df

        # v0.8.3
        context.total_rows = len(df)

        logger.info(
            f"[SOURCE] rows={len(df)}"
        )

        return context

    # =========================================================
    # RULE
    # =========================================================
    def _run_rule(self, config, context):

        rule_service = RuleService(
            self.db
        )

        mask = rule_service.execute(
            JOB_REPAIR_PENDING,
            context.data
        )

        context.data = context.data[mask]

        # v0.8.3
        context.filtered_rows = len(
            context.data
        )

        logger.info(
            f"[RULE] rows={len(context.data)}"
        )

        return context

    # =========================================================
    # PROCESS
    # =========================================================
    def _run_process(self, config, context):

        processor_name = config.get(
            "processor",
            "VendorGroupingProcessor"
        )

        processor = ProcessorFactory.get(
            processor_name
        )

        context.data = processor.execute(
            context.data
        )

        # v0.8.3
        context.vendor_count = len(
            context.data
        )

        logger.info(
            f"[PROCESS] vendors={len(context.data)}"
        )

        return context

    # =========================================================
    # EXPORT
    # =========================================================
    def _run_export(self, config, context):

        exporter_name = config.get(
            "exporter"
        )

        output_path = config.get(
            "output_path",
            "output/"
        )

        exporter = ExportFactory.get(
            exporter_name
        )

        context.data = exporter.execute(
            context.data,
            output_path
        )

        if isinstance(
            context.data,
            list
        ):

            context.output_file_count = len(
                context.data
            )

            logger.info(
                f"[EXPORT] files={len(context.data)}"
            )

        else:

            context.output_file_count = 1

            logger.info(
                f"[EXPORT] path={context.data}"
            )

        return context

    # =========================================================
    # ZIP
    # =========================================================
    def _run_zip(self, config, context):

        output_path = config.get(
            "output_path",
            "output/"
        )

        zip_path = create_zip(
            context.data,
            output_path
        )

        context.data = zip_path

        logger.info(
            f"[ZIP] path={zip_path}"
        )

        return context

    # =========================================================
    # DELIVERY
    # =========================================================
    def _run_delivery(self, config, context):

        sender_name = config.get(
            "sender",
            "EmailSender"
        )

        sender = DeliveryFactory.get(
            sender_name
        )

        subject = build_subject(
            JOB_REPAIR_PENDING
        )

        body = build_body(
            job_name=JOB_REPAIR_PENDING,
            total_rows=context.total_rows,
            filtered_rows=context.filtered_rows,
            vendor_count=context.vendor_count,
            file_count=context.output_file_count
        )

        sender.execute(
            subject,
            body,
            context.data
        )

        logger.info(
            f"[MAIL] sent={TO_EMAIL}"
        )

        return context

    # =========================================================
    # HISTORY
    # =========================================================
    def _run_history(self, config, context):

        writer = HistoryWriter(
            self.db
        )

        writer.write(
            context
        )

        logger.info(
            "[HISTORY] saved"
        )

        return context