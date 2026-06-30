from app.excel.excel_exporter import export_excel
from app.excel.settlement_excel_exporter import (
    export_settlement_excel
)

from app.utils.zip_creator import create_zip


class VendorExcelExporter:

    def execute(self, data, output_path):
        return export_excel(data, output_path)


class SettlementExcelExporter:

    def execute(self, data, output_path):
        return export_settlement_excel(
            data,
            output_path
        )


class ZipExporter:

    def execute(self, data, output_path):
        return create_zip(data, output_path)


class ExportFactory:

    @staticmethod
    def get(exporter_name):

        if exporter_name == "VendorExcelExporter":
            return VendorExcelExporter()

        if exporter_name == "SettlementExcelExporter":
            return SettlementExcelExporter()

        if exporter_name == "ZipExporter":
            return ZipExporter()

        raise ValueError(
            f"Unknown exporter: {exporter_name}"
        )