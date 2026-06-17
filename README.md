automation-runtime

업무 자동화 Runtime 플랫폼

현재 버전: v0.2.11

현재는 수선업체 미처리건(Repair Pending) 자동화를 지원하며,

향후

Inbound Missing
Settlement Missing
TC Scan

등의 업무 자동화를 동일 Runtime 위에서 수행할 수 있도록 설계되었습니다.

주요 기능
Repair Pending Automation

AS접수현황 엑셀 파일을 분석하여

추출 조건
수선업체1 존재 + 업체완료일1 미입력
수선업체2 존재 + 업체완료일2 미입력
자동 수행 기능
미처리 건 추출
업체별 그룹핑
업체별 Excel 생성
ZIP 생성
결과 메일 자동 발송
처리 흐름
Excel Input
      ↓
Rule Engine
      ↓
Filtering
      ↓
Vendor Grouping
      ↓
Excel Export
      ↓
ZIP Packaging
      ↓
Mail Delivery
      ↓
Result
프로젝트 구조
app/

├── cli
│   └── argument_parser.py

├── config
│   └── settings.py

├── excel
│   ├── excel_reader.py
│   └── excel_exporter.py

├── jobs
│   ├── base_job.py
│   ├── job_registry.py
│   ├── repair_pending_job.py
│   ├── inbound_missing_job.py
│   ├── settlement_missing_job.py
│   └── tc_scan_job.py

├── mail
│   ├── mail_sender.py
│   ├── mail_template.py
│   └── test_mail.py

├── models
│   └── job_result.py

├── presenters
│   └── job_result_presenter.py

├── rules
│   └── repair_pending_rule.py

├── utils
│   ├── logger.py
│   └── zip_creator.py

├── runner.py
│     CLI Runtime Entry Point

├── main.py
│     Future FastAPI Entry Point
설치
pip install -r requirements.txt
환경 설정

.env

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587

SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password

TO_EMAIL=receiver@gmail.com

Google 계정의 App Password를 사용해야 합니다.

실행 방법
기본 실행
python -m app.runner

또는

실행하기.bat
특정 Job 실행
Repair Pending
python -m app.runner --job repair_pending
Inbound Missing
python -m app.runner --job inbound_missing
Settlement Missing
python -m app.runner --job settlement_missing
TC Scan
python -m app.runner --job tc_scan
실행 결과 예시
[INFO] JOB          : RepairPending
[INFO] TOTAL ROWS   : 3549
[INFO] FILTERED     : 107
[INFO] VENDORS      : 23
[INFO] OUTPUT FILES : 23
[INFO] ZIP FILE     : output/result.zip
[INFO] SUCCESS      : True
[INFO] MESSAGE      : 처리 완료
메일 발송 예시

제목

[Automation Runtime] RepairPending 결과

본문

안녕하세요.

RepairPending 작업이 완료되었습니다.

전체 데이터 수 : 3549
대상 건수 : 107
업체 수 : 23
생성 파일 수 : 23

첨부파일 확인 부탁드립니다.

감사합니다.

※ 본 메일은 Automation Runtime에 의해 자동 발송되었습니다.

첨부파일

result.zip
출력 파일
output/

├── temp/
│   ├── 업체A.xlsx
│   ├── 업체B.xlsx
│   └── ...

└── result.zip
Job Registry

모든 업무 자동화는 Job Registry를 통해 관리됩니다.

JOB_REGISTRY = {
    "repair_pending": RepairPendingJob,
    "inbound_missing": InboundMissingJob,
    "settlement_missing": SettlementMissingJob,
    "tc_scan": TcScanJob
}

새로운 업무 자동화 추가 시

Job 생성
Rule 생성
Registry 등록

만 수행하면 Runtime에 편입됩니다.

버전 이력
v0.1.0
Repair Pending MVP
업체별 Excel 생성
ZIP 생성
v0.2.0
Runtime 구조 분리
Rule / Excel / Job 모듈화
v0.2.1
JobResult 도입
Runtime Settings 분리
Header 자동 인식 개선
v0.2.2
BaseJob 도입
Class 기반 Job 구조 전환
v0.2.3
Job Skeleton 추가
InboundMissingJob
SettlementMissingJob
TcScanJob
v0.2.4
Logger 도입
Console 출력 표준화
v0.2.5
Presenter Layer 분리
Result 출력 책임 분리
v0.2.6
Job Registry 도입
CLI Job 선택 기능 추가
v0.2.7
ArgumentParser 도입
--job 옵션 지원
CLI 인터페이스 표준화
FastAPI 전환 준비
v0.2.8
runner.py 분리
CLI Entry Point 분리
main.py FastAPI 전용 예약
v0.2.9
Repair Pending Template Exporter 개선
업체1/업체2 완료여부 분리 처리
원전미입고 포맷 기반 업체별 파일 생성
업체의뢰일 자동 매핑
실운영 데이터 검증 완료
v0.2.10
Gmail SMTP 연동
.env 지원
SMTP 설정 분리
SMTP 테스트 모듈 추가
v0.2.11
Mail Template 추가
자동 메일 생성
ZIP 첨부파일 전송
결과 메일 자동 발송
End-to-End 업무 자동화 완성
향후 계획
v0.3.0

업무 자동화 확장

Inbound Missing 구현
Settlement Missing 구현
TC Scan 구현
v0.4.0

FastAPI Web Runtime

Job 선택
Excel 업로드
실행 결과 조회
ZIP 다운로드
v0.5.0

Job History

SQLite
MariaDB
v0.6.0

Scheduler

정기 실행
배치 자동화
Windows Task Scheduler 연동
v0.7.0+

Notification 확장

다중 수신자
HTML Mail
Teams 연동
Slack 연동
Runtime 철학

업무별로 다른 엑셀 매크로를 만드는 것이 아니라

Excel Input
      ↓
Rule Engine
      ↓
Grouping
      ↓
Export
      ↓
Delivery
      ↓
Result

공통 Runtime 위에서 다양한 업무 자동화를 수행하는 플랫폼을 목표로 합니다.