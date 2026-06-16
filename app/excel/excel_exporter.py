import pandas as pd
import os

from app.config.settings import (
    OUTPUT_DIR,
    TEMP_DIR
)

from app.utils.logger import logger

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)


def export_excel(groups):

    files = []

    for vendor, rows in groups.items():

        safe_vendor = "".join(
            c for c in vendor
            if c.isalnum() or c in " _-"
        )

        file_path = os.path.join(
            TEMP_DIR,
            f"{safe_vendor}.xlsx"
        )

        pd.DataFrame(rows).to_excel(
            file_path,
            index=False
        )

        files.append(file_path)

    logger.info(
        f"생성 파일 수: {len(files)}"
    )

    return files
