import pandas as pd

from app.utils.logger import logger


def find_col(df, keywords):
    """
    컬럼명이 조금 달라도 찾게 만드는 핵심 함수
    """

    for col in df.columns:

        normalized_col = (
            str(col)
            .replace(" ", "")
            .replace("\n", "")
        )

        for key in keywords:

            if key.lower() in normalized_col.lower():
                return col

    return None


def filter_pending(df):

    col_vendor1 = find_col(
        df,
        ["수선업체1", "업체1", "vendor1"]
    )

    col_vendor2 = find_col(
        df,
        ["수선업체2", "업체2", "vendor2"]
    )

    col_done1 = find_col(
        df,
        ["업체완료일1", "완료일1", "done1"]
    )

    col_done2 = find_col(
        df,
        ["업체완료일2", "완료일2", "done2"]
    )

    # 필수 컬럼 체크
    if not col_vendor1 or not col_done1:
        raise Exception(
            "필수 컬럼을 찾을 수 없습니다. 엑셀 구조 확인 필요"
        )

    v1 = df[col_vendor1]
    d1 = df[col_done1]

    v2 = (
        df[col_vendor2]
        if col_vendor2
        else pd.Series([None] * len(df))
    )

    d2 = (
        df[col_done2]
        if col_done2
        else pd.Series([None] * len(df))
    )

    filtered = df[
        (
            (v1.notna()) & 
            (d1.isna())
        )
        | 
        (
            (v2.notna()) & 
            (d2.isna())
        )
    ]

    logger.info(
        f"미처리 건수: {len(filtered)}"
    )

    return filtered


def group_by_vendor(df):

    col_vendor1 = find_col(
        df,
        ["수선업체1", "업체1", "vendor1"]
    )

    col_vendor2 = find_col(
        df,
        ["수선업체2", "업체2", "vendor2"]
    )

    groups = {}

    for _, row in df.iterrows():

        vendors = []

        if (
            col_vendor1 and
            pd.notna(row.get(col_vendor1))
        ):
            vendors.append(
                str(row[col_vendor1]).strip()
            )

        if (
            col_vendor2 and
            pd.notna(row.get(col_vendor2))
        ):
            vendors.append(
                str(row[col_vendor2]).strip()
            )

        for vendor in vendors:

            if vendor not in groups:
                groups[vendor] = []

            groups[vendor].append(row)

    logger.info(
        f"업체 수: {len(groups)}"
    )

    return groups
