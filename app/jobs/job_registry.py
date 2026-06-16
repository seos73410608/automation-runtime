from app.jobs.repair_pending_job import RepairPendingJob

from app.jobs.inbound_missing_job import InboundMissingJob

from app.jobs.settlement_missing_job import SettlementMissingJob

from app.jobs.tc_scan_job import TcScanJob

JOB_REGISTRY = {
    "repair_pending": RepairPendingJob,

    "inbound_missing": InboundMissingJob,

    "settlement_missing": SettlementMissingJob,

    "tc_scan": TcScanJob
}