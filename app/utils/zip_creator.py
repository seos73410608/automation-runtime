import os
import zipfile

from app.config.settings import (
    RESULT_ZIP_NAME
)

from app.utils.logger import logger


def create_zip(
    files,
    output_dir: str
):

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    zip_path = os.path.join(
        output_dir,
        RESULT_ZIP_NAME
    )

    with zipfile.ZipFile(
        zip_path,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zipf:

        for file in files:

            zipf.write(
                file,
                os.path.basename(file)
            )

    logger.info(
        f"ZIP 생성 완료: {zip_path}"
    )

    return zip_path