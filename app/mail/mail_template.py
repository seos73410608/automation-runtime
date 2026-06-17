def build_subject(job_name):
    return f"[Automation Runtime] {job_name} 결과"


def build_body(
    job_name,
    vendor_count,
    file_count
):
    return f"""
안녕하세요.

{job_name} 작업이 완료되었습니다.

업체 수 : {vendor_count}
생성 파일 수 : {file_count}

첨부파일 확인 부탁드립니다.

감사합니다.
"""
