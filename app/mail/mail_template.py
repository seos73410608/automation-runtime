def build_subject(job_name):
    return f"[Automation Runtime] {job_name} 결과"


def build_body(
    job_name,
    total_rows,
    filtered_rows,
    vendor_count,
    file_count
):
    return f"""
안녕하세요.

{job_name} 작업이 완료되었습니다.

전체 데이터 수 : {total_rows}
대상 건수 : {filtered_rows}
업체 수 : {vendor_count}
생성 파일 수 : {file_count}

첨부파일 확인 부탁드립니다.

감사합니다.

※ 본 메일은 Automation Runtime에 의해 자동 발송되었습니다.
"""
