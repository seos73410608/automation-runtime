import os
import zipfile

from app.config.settings import (
    OUTPUT_DIR,
    RESULT_ZIP_NAME
)

os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_zip(files):

    zip_path = os.path.join(
        OUTPUT_DIR,
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

    print(f"[INFO] ZIP 생성 완료: {zip_path}")

    return zip_path