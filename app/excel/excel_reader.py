import pandas as pd

from app.utils.logger import logger


def read_excel(file_path: str):

    ext = file_path.split(".")[-1].lower()

    try:

        # XLS (구버전)
        if ext == "xls":

            df = pd.read_excel(
                file_path,
                engine="xlrd",
                header=1
            )

        # XLSX (신버전)
        else:

            df = pd.read_excel(
                file_path,
                engine="openpyxl",
                header=1
            )

    except Exception as e:

        logger.warning(
            f"fallback 실행: {e}"
        )

        df = pd.read_excel(
            file_path,
            header=1
        )

    # 컬럼 정리
    df.columns = (
        df.columns
        .astype(str)
        .str.replace("\n", "", regex=False)
        .str.strip()
    )

    logger.info(
        f"로딩 완료: {len(df)} rows"
    )

    logger.info(
        f"컬럼: {df.columns.tolist()}"
    )

    return df