import pandas as pd
import os
import zipfile
import glob

# =================================================
# 0. 경로 설정
# =================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
TEMP_DIR = os.path.join(OUTPUT_DIR, "temp")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)


# =================================================
# 1. 입력 파일 자동 탐색 (xls/xlsx 모두 지원)
# =================================================
def get_input_file():
    files = glob.glob(os.path.join(INPUT_DIR, "*.xls*"))

    if not files:
        raise Exception("input 폴더에 엑셀 파일이 없습니다.")

    print(f"[INFO] 사용 파일: {files[0]}")
    return files[0]


# =================================================
# 2. 엑셀 읽기 (자동 엔진 선택)
# =================================================
def read_excel():
    file_path = get_input_file()
    ext = file_path.split(".")[-1].lower()

    try:
        # --------------------------
        # XLS (구버전)
        # --------------------------
        if ext == "xls":
            df = pd.read_excel(file_path, engine="xlrd", header=1)

        # --------------------------
        # XLSX (신버전)
        # --------------------------
        else:
            df = pd.read_excel(file_path, engine="openpyxl", header=1)

    except Exception as e:
        print("[WARN] fallback 실행:", e)
        df = pd.read_excel(file_path, header=1)

    # 컬럼 정리
    df.columns = df.columns.astype(str).str.strip()

    print(f"[INFO] 로딩 완료: {len(df)} rows")
    print(f"[INFO] 컬럼: {df.columns.tolist()}")

    return df
    
# =================================================
# 3. 컬럼 자동 매칭 (입력 표준화 핵심)
# =================================================
def find_col(df, keywords):
    """
    컬럼명이 조금 달라도 찾게 만드는 핵심 함수
    """
    for col in df.columns:
        for key in keywords:
            if key in col.replace(" ", ""):
                return col
    return None


# =================================================
# 4. 미처리 필터 Rule
# =================================================
def filter_pending(df):

    col_vendor1 = find_col(df, ["수선업체1", "업체1", "vendor1"])
    col_vendor2 = find_col(df, ["수선업체2", "업체2", "vendor2"])
    col_done1 = find_col(df, ["업체완료일1", "완료일1", "done1"])
    col_done2 = find_col(df, ["업체완료일2", "완료일2", "done2"])

    # 없는 컬럼 방어
    if not col_vendor1 or not col_done1:
        raise Exception("필수 컬럼을 찾을 수 없습니다. 엑셀 구조 확인 필요")

    v1 = df[col_vendor1]
    d1 = df[col_done1]

    v2 = df[col_vendor2] if col_vendor2 else pd.Series([None] * len(df))
    d2 = df[col_done2] if col_done2 else pd.Series([None] * len(df))

    filtered = df[
        ((v1.notna()) & (d1.isna())) |
        ((v2.notna()) & (d2.isna()))
    ]

    print(f"[INFO] 미처리 건수: {len(filtered)}")
    return filtered


# =================================================
# 5. 업체별 그룹핑
# =================================================
def group_by_vendor(df):

    col_vendor1 = find_col(df, ["수선업체1", "업체1", "vendor1"])
    col_vendor2 = find_col(df, ["수선업체2", "업체2", "vendor2"])

    groups = {}

    for _, row in df.iterrows():
        vendors = []

        if col_vendor1 and pd.notna(row.get(col_vendor1)):
            vendors.append(str(row[col_vendor1]).strip())

        if col_vendor2 and pd.notna(row.get(col_vendor2)):
            vendors.append(str(row[col_vendor2]).strip())

        for v in vendors:
            if v not in groups:
                groups[v] = []
            groups[v].append(row)

    print(f"[INFO] 업체 수: {len(groups)}")
    return groups


# =================================================
# 6. 엑셀 생성
# =================================================
def export_excel(groups):

    files = []

    for vendor, rows in groups.items():

        safe_vendor = "".join(c for c in vendor if c.isalnum() or c in " _-")

        file_path = os.path.join(TEMP_DIR, f"{safe_vendor}.xlsx")

        pd.DataFrame(rows).to_excel(file_path, index=False)

        files.append(file_path)

    print(f"[INFO] 생성 파일 수: {len(files)}")
    return files


# =================================================
# 7. ZIP 생성
# =================================================
def create_zip(files):

    zip_path = os.path.join(OUTPUT_DIR, "result.zip")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for f in files:
            zipf.write(f, os.path.basename(f))

    print(f"[INFO] ZIP 생성 완료: {zip_path}")


# =================================================
# 8. MAIN
# =================================================
def main():

    try:
        df = read_excel()
        filtered = filter_pending(df)
        groups = group_by_vendor(filtered)
        files = export_excel(groups)
        create_zip(files)

        print("[DONE] 전체 처리 완료")

    except Exception as e:
        print("[ERROR]", str(e))


if __name__ == "__main__":
    main()