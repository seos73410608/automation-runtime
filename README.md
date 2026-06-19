automation-runtime

업무 자동화 Runtime 플랫폼

현재 버전: v0.5.3

프로젝트 소개

automation-runtime은 반복적인 엑셀 기반 업무를 자동화하기 위한 Runtime 플랫폼입니다.

단순히 하나의 매크로 프로그램을 만드는 것이 아니라,

Excel 업로드
Rule 기반 데이터 처리
업체별 파일 생성
ZIP 패키징
메일 발송
실행 이력 관리

를 공통 Runtime 위에서 수행할 수 있도록 설계되었습니다.

현재는 Repair Pending 업무를 지원하며,
향후 다양한 업무 자동화를 동일 플랫폼에 추가할 수 있습니다.

주요 기능
Repair Pending Automation

AS 접수현황 파일을 분석하여 미처리 건을 추출합니다.

추출 조건
업체1 미처리
수선업체1 존재
AND
업체완료일1 미입력
업체2 미처리
수선업체2 존재
AND
업체완료일2 미입력
자동 수행 기능
Excel 업로드

사용자가 웹 화면에서 엑셀 업로드

↓

Rule Engine

업무 규칙 적용

↓

Filtering

미처리 건 추출

↓

Vendor Grouping

업체별 그룹핑

↓

Excel Export

업체별 엑셀 생성

↓

ZIP Packaging

결과 ZIP 생성

↓

Mail Delivery

결과 메일 발송

↓

History Management

실행 이력 저장

↓

Download

ZIP 다운로드

시스템 화면
작업 실행
/

기능

Job 선택
Excel 업로드
실행
실행 이력
/history

기능

전체 실행 이력 조회
상태 확인
ZIP 다운로드
상세보기 이동
Job 상세
/job/{job_id}

기능

Job 정보 조회
Step History 조회
ZIP 다운로드
기술 스택
Backend
Python 3.12
FastAPI
Jinja2
Uvicorn
Database
MariaDB
SQLAlchemy
Excel
Pandas
OpenPyXL
xlrd
Mail
SMTP
Gmail App Password
프로젝트 구조
app/

├── config
│   └── settings.py

├── constants
│   ├── job_status.py
│   └── job_step.py

├── db
│   ├── database.py
│   ├── models.py
│   └── repository.py

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
│   └── mail_template.py

├── models
│   └── job_result.py

├── rules
│   └── repair_pending_rule.py

├── templates
│   ├── index.html
│   ├── result.html
│   ├── history.html
│   └── job_detail.html

├── utils
│   ├── logger.py
│   └── zip_creator.py

└── main.py
데이터베이스
TB_AUTOMATION_JOB

작업 실행 정보

컬럼	설명
job_id	작업 ID
file_name	업로드 파일
status	상태
total_rows	전체 건수
vendor_count	업체 수
created_at	생성일시
updated_at	수정일시
TB_AUTOMATION_JOB_HISTORY

단계별 처리 이력

컬럼	설명
history_id	PK
job_id	Job ID
step_name	처리 단계
status	상태
message	상세 메시지
created_at	생성일시
환경 설정

.env

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587

SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password

TO_EMAIL=receiver@gmail.com

DB_HOST=localhost
DB_PORT=3306
DB_NAME=automation_runtime

DB_USER=runtime_app
DB_PASSWORD=runtime_app_1234
설치
pip install -r requirements.txt
실행
FastAPI 실행
uvicorn app.main:app --reload
접속
http://127.0.0.1:8000
출력 구조

현재 버전부터 Job 단위로 결과를 보관합니다.

output/

└── 20260619
    └── b903a9db-9062-4567-8525-596e887872ee

        ├── excel
        │   ├── 업체A.xlsx
        │   ├── 업체B.xlsx
        │   └── ...

        └── result.zip
Job 상태
RUNNING
SUCCESS
FAILED
처리 단계
READ_EXCEL
FILTER
GROUP
EXPORT
ZIP
MAIL
현재 지원 Job
Job	상태
Repair Pending	완료
Inbound Missing	예정
Settlement Missing	예정
TC Scan	예정
버전 이력
v0.5.3
Job별 ZIP 다운로드
실행 이력 UI 개선
상세 화면 다운로드 지원
Job Output 구조 개선
날짜/JobID 기반 결과 보관
v0.5.2
Upload 파일 보관
Output 보관 구조 개선
v0.5.1
Job History
Step History
MariaDB 연동
메일 발송 이력 관리
v0.5.0
FastAPI Web Runtime
Excel 업로드
Web 실행
결과 화면
향후 계획
v0.6.0

Scheduler

정기 실행
자동 배치
Windows Task Scheduler 연동
v0.7.0

Multi Job

Inbound Missing
Settlement Missing
TC Scan
v0.8.0

Notification 확장

HTML Mail
다중 수신자
Teams
Slack
Runtime 철학
Excel Input
      ↓
Rule Engine
      ↓
Filtering
      ↓
Grouping
      ↓
Export
      ↓
Delivery
      ↓
History
      ↓
Result

업무마다 새로운 매크로를 만드는 것이 아니라,

공통 Runtime 위에 Rule만 추가하여 다양한 업무 자동화를 수행하는 플랫폼을 목표로 합니다.