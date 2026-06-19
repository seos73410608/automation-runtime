import pandas as pd
import os

from app.utils.logger import logger

EXPORT_COLUMNS = [
    "현재수선현황",
    "완료예정일",
    "특이사항",
    "업체",
    "업체의뢰일",
    "판매전후",
    "수선결과",
    "전표번호",
    "접수매장",
    "고객명",
    "상품코드",
    "상품명",
    "색상",
    "사이즈",
    "AS제품상태",
]


def export_excel(
    groups,
    output_dir: str
):

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    files = []

    for vendor, rows in groups.items():

        safe_vendor = "".join(
            c for c in vendor
            if c.isalnum() or c in " _-"
        )

        file_path = os.path.join(
            output_dir,
            f"{safe_vendor}.xlsx"
        )

        export_rows = []

        for row in rows:

            vendor_no = row.get(
                "_target_vendor_no",
                1
            )

            request_date = ""

            if vendor_no == 1:

                request_date = row.get(
                    "업체의뢰일1",
                    ""
                )

            elif vendor_no == 2:

                request_date = row.get(
                    "업체의뢰일2",
                    ""
                )

            export_rows.append({
                "현재수선현황": "",
                "완료예정일": "",
                "특이사항": "",
                "업체": vendor,
                "업체의뢰일": request_date,
                "판매전후": row.get("판매전후", ""),
                "수선결과": row.get("수선결과", ""),
                "전표번호": row.get("전표번호", ""),
                "접수매장": row.get("접수매장", ""),
                "고객명": row.get("고객명", ""),
                "상품코드": row.get("상품코드", ""),
                "상품명": row.get("상품명", ""),
                "색상": row.get("색상", ""),
                "사이즈": row.get("사이즈", ""),
                "AS제품상태": row.get("AS제품상태", ""),
            })

        df = pd.DataFrame(
            export_rows,
            columns=EXPORT_COLUMNS
        )

        df.to_excel(
            file_path,
            index=False
        )

        files.append(
            file_path
        )

        logger.info(
            f"{vendor} 파일 생성 완료 ({len(df)}건)"
        )

    logger.info(
        f"생성 파일 수: {len(files)}"
    )

    return files