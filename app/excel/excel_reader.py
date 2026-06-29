import pandas as pd

from app.utils.logger import logger


def read_excel(
    file_path: str,
    header_row: int = 1,
    sheet_name: str = None,
    engine: str = None
):

    if sheet_name is None:
        sheet_name = 0

    ext = file_path.split(".")[-1].lower()

    #
    # engine 미지정이면 확장자로 자동 결정
    #
    if engine is None:

        if ext == "xls":
            engine = "xlrd"

        else:
            engine = "openpyxl"

    try:

        df = pd.read_excel(
            file_path,
            engine=engine,
            header=header_row,
            sheet_name=sheet_name
        )

    except Exception as e:

        logger.warning(
            f"fallback 실행 : {e}"
        )

        df = pd.read_excel(
            file_path,
            header=header_row,
            sheet_name=sheet_name
        )

    df.columns = (
        df.columns
        .astype(str)
        .str.replace("\n", "", regex=False)
        .str.strip()
    )

    logger.info(f"engine={engine}")
    logger.info(f"header_row={header_row}")
    logger.info(f"sheet_name={sheet_name}")
    logger.info(f"rows={len(df)}")
    logger.info(f"columns={df.columns.tolist()}")

    return df