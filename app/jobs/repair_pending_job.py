from app.excel.excel_reader import read_excel
from app.excel.excel_exporter import export_excel

from app.rules.repair_pending_rule import (
    filter_pending,
    group_by_vendor
)

from app.utils.zip_creator import create_zip

from app.models.job_result import JobResult


def execute():

    try:

        df = read_excel()

        filtered = filter_pending(df)

        groups = group_by_vendor(filtered)

        files = export_excel(groups)

        zip_path = create_zip(files)

        return JobResult(
            job_name="RepairPending",
            total_rows=len(df),
            filtered_rows=len(filtered),
            vendor_count=len(groups),
            output_file_count=len(files),
            zip_file_path=zip_path,
            success=True,
            message="처리 완료"
        )

    except Exception as e:

        print(f"[ERROR] {e}")

        return JobResult(
            job_name="RepairPending",
            total_rows=0,
            filtered_rows=0,
            vendor_count=0,
            output_file_count=0,
            zip_file_path="",
            success=False,
            message=str(e)
        )