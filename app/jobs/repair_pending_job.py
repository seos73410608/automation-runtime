from app.excel.excel_reader import read_excel
from app.excel.excel_exporter import export_excel

from app.rules.repair_pending_rule import (
    filter_pending,
    group_by_vendor
)

from app.utils.zip_creator import create_zip


def execute():

    df = read_excel()

    filtered = filter_pending(df)

    groups = group_by_vendor(filtered)

    files = export_excel(groups)

    create_zip(files)

    print("[DONE] 전체 처리 완료")