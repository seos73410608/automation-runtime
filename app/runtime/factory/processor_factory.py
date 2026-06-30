from app.rules.repair_pending_rule import (
    group_by_vendor
)

from app.processors.settlement_aggregation_processor import (
    SettlementAggregationProcessor
)


class VendorGroupingProcessor:

    def execute(self, data):

        return group_by_vendor(data)


class ProcessorFactory:

    @staticmethod
    def get(processor_name):

        if processor_name == "VendorGroupingProcessor":

            return VendorGroupingProcessor()

        elif processor_name == "SettlementAggregationProcessor":

            return SettlementAggregationProcessor()

        raise ValueError(
            f"Unknown processor: {processor_name}"
        )