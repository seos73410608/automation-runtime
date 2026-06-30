import os

import pandas as pd

from app.utils.logger import logger


def export_settlement_excel(
    df: pd.DataFrame,
    output_path: str
) -> str:

    if df is None or df.empty:

        raise ValueError(
            "Settlement dataframe is empty."
        )

    os.makedirs(
        output_path,
        exist_ok=True
    )

    file_path = os.path.join(
        output_path,
        "settlement_report.xlsx"
    )

    df.to_excel(
        file_path,
        index=False
    )

    logger.info(
        "[SETTLEMENT EXPORT] "
        f"rows={len(df)}, "
        f"path={file_path}"
    )

    return file_path