def build_subject(job_name):
    return f"[Automation Runtime] {job_name} 작업 완료"


def build_body(
    job_name,
    total_rows,
    filtered_rows,
    vendor_count,
    file_count
):
    return f"""
안녕하세요.

Automation Runtime 작업이 완료되었습니다.

=========================================
작업명
=========================================
{job_name}

=========================================
처리 결과
=========================================
전체 데이터 수 : {total_rows}
대상 건수     : {filtered_rows}
업체 수       : {vendor_count}
생성 파일 수  : {file_count}

=========================================
첨부파일
=========================================
업체별 결과 파일이 ZIP 형태로 첨부되어 있습니다.

감사합니다.

※ 본 메일은 Automation Runtime에 의해 자동 발송되었습니다.
"""
