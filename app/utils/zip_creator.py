import os
import zipfile


# 프로젝트 루트
BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_zip(files):

    zip_path = os.path.join(
        OUTPUT_DIR,
        "result.zip"
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