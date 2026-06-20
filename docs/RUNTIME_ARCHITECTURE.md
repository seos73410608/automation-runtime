RUNTIME_ARCHITECTURE.md
Automation Runtime Architecture
Overview

Automation Runtime은 반복 업무를 자동화하기 위한 Runtime Platform이다.

모든 Job은 공통 Runtime 위에서 실행된다.

새로운 업무가 추가되더라도 Runtime Core는 변경하지 않고 Job만 추가할 수 있도록 설계한다.

High Level Architecture

User / Scheduler

↓

Runtime Core

↓

Job Registry

↓

Data Source Runtime

↓

Rule Engine

↓

Processing Engine

↓

Export Engine

↓

Delivery Engine

↓

History Engine

Runtime Flow

Input

↓

Validation

↓

Rule Evaluation

↓

Processing

↓

Export

↓

Delivery

↓

History

Runtime Core
Overview

Runtime Core는 Automation Runtime의 실행 오케스트레이터 역할을 수행한다.

모든 Job은 Runtime Core를 통해 실행된다.

Responsibilities
Job 실행 요청 처리
Scheduler 연동
Job Lifecycle 관리
Step 실행 순서 제어
Exception 처리
History 기록
Runtime Core Structure

User / Scheduler

↓

Runtime Core

(Execution Orchestrator)

↓

Job Registry

↓

Data Source Runtime

↓

Rule Engine

↓

Processing Engine

↓

Export Engine

↓

Delivery Engine

↓

History Engine

Runtime Core는 직접 데이터를 처리하지 않는다.

Rule Engine, Processing Engine, Export Engine, Delivery Engine을 조합하여 실행 흐름을 제어한다.

Component Architecture
1. Job Registry
역할

등록 가능한 Job 관리

예시
JOB_REGISTRY = {
    "repair_pending": RepairPendingJob,
    "inbound_missing": InboundMissingJob,
    "settlement_missing": SettlementMissingJob,
    "tc_scan": TcScanJob
}
책임
Job 등록
Job 조회
Job 실행
2. Scheduler Runtime
역할

자동 실행 관리

구성
APScheduler
Cron Loader
Schedule Registry
DB

TB_AUTOMATION_SCHEDULE

TB_SCHEDULE_EXECUTION

책임
Cron 등록
자동 실행
실행 이력 저장
3. Data Source Runtime
역할

입력 데이터 추상화

지원 예정
Excel Source
CSV Source
MariaDB Source
REST API Source
Shopify Source
SAP Source
예시
Excel
 ↓
DataFrame
MariaDB
 ↓
DataFrame

모든 Source는 동일한 형태(DataFrame)의 데이터셋을 반환한다.

4. Rule Engine
역할

데이터 필터링 및 조건 평가

예시
{
  "field": "업체완료일1",
  "operator": "IS_EMPTY"
}
지원 예정
IS_EMPTY
EQUALS
NOT_EQUALS
CONTAINS
STARTS_WITH
ENDS_WITH
GREATER_THAN
LESS_THAN
OLDER_THAN_DAYS
DB (Planned)

TB_RULE

TB_RULE_GROUP

TB_RULE_EXECUTION

목표

코드 수정 없이 Rule 변경 가능

5. Processing Engine
역할

데이터 변환 처리

지원 예정
Filter

조건 필터링

Group

업체별 그룹핑

Sort

정렬

Compare

데이터 비교

Join

데이터 결합

Aggregation

집계

6. Export Engine
역할

결과 파일 생성

지원
Excel
CSV
ZIP
예시
DataFrame
 ↓
Excel
7. Delivery Engine
역할

결과 전달

지원
Download
Mail
지원 예정
Slack
Teams
8. History Engine
역할

실행 이력 저장

DB

TB_AUTOMATION_JOB

TB_AUTOMATION_JOB_HISTORY

TB_SCHEDULE_EXECUTION

기록 항목
Job
Step
Status
Message
Execution Time
Job Lifecycle

모든 Job은 동일한 Lifecycle을 따른다.

Job Requested
      ↓
 Validation
      ↓
   Running
      ↓
    Export
      ↓
   Delivery
      ↓
  Completed

      or

    Failed
Status Mapping

TB_AUTOMATION_JOB.status

RUNNING
SUCCESS
FAILED
Step History

TB_AUTOMATION_JOB_HISTORY

READ_EXCEL
FILTER
GROUP
EXPORT
ZIP
MAIL
ERROR
Database Architecture
Schedule Domain
TB_AUTOMATION_SCHEDULE
            │
            ▼
TB_SCHEDULE_EXECUTION
설명
Scheduler 정의
Scheduler 실행 이력
Job Domain
TB_AUTOMATION_JOB
          │
          ▼
TB_AUTOMATION_JOB_HISTORY
설명
Job 실행 정보
Step 실행 이력
File Storage (Current)
uploads/

└── YYYYMMDD/

      └── {job_id}/


output/

└── YYYYMMDD/

      └── {job_id}/
설명
업로드 파일 저장
결과 파일 저장
다운로드 제공
Future Domain
Rule Domain
TB_RULE

TB_RULE_GROUP

TB_RULE_EXECUTION
설명
Rule Engine 관리
Rule 실행 이력
File Domain
TB_FILE_UPLOAD

TB_OUTPUT_FILE
설명
파일 메타데이터 관리
다운로드 이력 관리
Storage 추상화
S3 연계 준비
Runtime Execution Example
RepairPending Job
Excel Upload

      ↓

 Excel Source

      ↓

 Rule Engine

 업체완료일1 IS_EMPTY

        OR

 업체완료일2 IS_EMPTY

      ↓

 Processing Engine

 업체별 그룹핑

      ↓

 Export Engine

 업체별 Excel 생성

      ↓

 ZIP Packaging

      ↓

 Mail Delivery

      ↓

 History Logging
Future Architecture (v1.0.0)
                    Scheduler
                         │
                         ▼

                 Automation Runtime

                         │
                         ▼

                   Runtime Core

                         │
                         ▼

                   Job Registry

                         │
                         ▼

               Data Source Runtime

 Excel / CSV / DB / API / Shopify / SAP

                         │
                         ▼

                    Rule Engine

      Filter / Validation / Compare

                         │
                         ▼

                 Processing Engine

      Group / Join / Sort / Aggregate

                         │
                         ▼

                    Export Engine

               Excel / CSV / ZIP

                         │
                         ▼

                   Delivery Engine

      Download / Mail / Slack / Teams

                         │
                         ▼

                    History Engine
Roadmap
v0.6.x

Scheduler Runtime

v0.7.x

Multi Job Runtime

v0.8.x

Rule Engine

v0.9.x

Data Source Runtime

v1.0.0

Automation Platform

Design Philosophy

업무별 프로그램을 만드는 것이 아니라,

공통 Runtime 위에 Job을 추가하여 업무 자동화를 확장한다.

Input
  ↓
Rule
  ↓
Processing
  ↓
Delivery
  ↓
History

모든 Job은 동일한 Runtime Lifecycle을 따른다.