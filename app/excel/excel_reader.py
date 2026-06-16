import pandas as pd
import glob

from app.config.settings import INPUT_DIR


def get_input_file():

    files = glob.glob(f"{INPUT_DIR}/*.xls*")

    if not files:
        raise Exception("input 폴더에 엑셀 파일이 없습니다.")

    print(f"[INFO] 사용 파일: {files[0]}")

    return files[0]


def read_excel():

    file_path = get_input_file()

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

        print(f"[WARN] fallback 실행: {e}")

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

    print(f"[INFO] 로딩 완료: {len(df)} rows")
    print(f"[INFO] 컬럼: {df.columns.tolist()}")

    return df