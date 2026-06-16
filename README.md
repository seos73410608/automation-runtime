automation-runtime

업무 자동화 Runtime 플랫폼

현재는 수선업체 미처리건(Repair Pending) 자동화를 지원하며,
향후 원전미입고(Inbound Missing), 정산누락(Settlement Missing), TC 미스캔(TC Scan) 등의 업무 자동화를 동일 Runtime 위에서 수행할 수 있도록 설계되었습니다.

현재 지원 기능
Repair Pending Automation

AS접수현황 엑셀 파일을 분석하여

수선업체1 존재 + 업체완료일1 미입력
수선업체2 존재 + 업체완료일2 미입력

조건의 미처리 건을 추출하고,

업체별 그룹핑
업체별 Excel 생성
ZIP 생성

을 자동 수행합니다.

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

실행하기.bat
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
Web Runtime 전환 준비 완료
향후 계획
v0.3.0

FastAPI Web Runtime

Job 선택 화면
Excel 업로드
실행 결과 조회
ZIP 다운로드
기존 Job Registry 재사용
기존 JobResult 재사용
v0.4.0

Job History 저장

SQLite 또는 MariaDB
v0.5.0

Mail Sender

자동 메일 발송
첨부파일 전송
v0.6.0

Scheduler

정기 실행
배치 자동화
v0.7.0+

업무 자동화 확장

원전미입고
정산누락
TC 미스캔
기타 운영 업무
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
Result

공통 Runtime 위에서 다양한 업무 자동화를 수행하는 플랫폼을 목표로 합니다.