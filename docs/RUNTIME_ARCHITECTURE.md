📘 RUNTIME_ARCHITECTURE.md (Final - WBS v0.7 반영)
Automation Runtime Architecture
📌 Overview

Automation Runtime은
설정 기반(Configuration-driven) 업무 자동화 Runtime Platform이다.

모든 실행은 코드가 아니라
Runtime Core + Configuration Layer + Execution Pipeline 조합으로 수행된다.

🧠 Core Principle

❗ Job은 코드가 아니라 “설정된 실행 단위”이다.

Input
 ↓
Configuration (Job / Schedule / Rule / Output)
 ↓
Runtime Core
 ↓
Execution Pipeline
 ↓
Output
 ↓
History
🧱 High Level Architecture (Revised)
User / Operator / Scheduler
            ↓
   Runtime Platform Layer (UI + Management)
            ↓
     Configuration Layer
   ┌───────────────────────────────┐
   │ Job Config                    │
   │ Schedule Config              │
   │ Rule Config                  │
   │ Output Config                │
   └───────────────────────────────┘
            ↓
     Runtime Core (Orchestrator)
            ↓
     Execution Pipeline
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
⚙️ Runtime Core
📌 Overview

Runtime Core는
Execution Orchestrator + Configuration Resolver 역할을 수행한다.

📌 Responsibilities
Job 실행 요청 처리
Scheduler 연동
Configuration 기반 실행 구성
Job Lifecycle 관리
Step Execution 제어
Exception 처리
Execution History 기록
📌 Runtime Core Structure
Trigger (User / Scheduler)
        ↓
Runtime Core
        ↓
Configuration Resolver
        ↓
Execution Pipeline Builder
        ↓
Execution Engine
🧩 Configuration Layer (NEW 핵심)
1. Job Configuration (핵심)

👉 기존 Job Registry 대체

Job 정의 (DB 기반)
Output Path 설정
File Naming Rule
Retention Policy
Email Receiver
Job = Execution Template + Configuration
2. Schedule Configuration
DB
TB_AUTOMATION_SCHEDULE
TB_SCHEDULE_EXECUTION
기능
Cron 설정
Enable / Disable
Run Now (즉시 실행)
Execution History
3. Rule Configuration

👉 코드 → 데이터 전환 영역

Rule Group
Rule Definition
Rule Test
Rule Preview
DB
TB_RULE
TB_RULE_GROUP
TB_RULE_EXECUTION
4. Output Configuration
Excel / CSV / ZIP 설정
File naming policy
Storage policy
S3 확장 준비
🧠 Job Registry (DEPRECATED)
❌ 기존 방식
JOB_REGISTRY = {
    "repair_pending": RepairPendingJob,
    "inbound_missing": InboundMissingJob
}
✅ 현재 방식

👉 Job Registry는 “참고용 Catalog” 수준

Job Execution = Configuration 기반 실행
🔄 Execution Flow
Trigger (User / Scheduler)
        ↓
Load Configuration
        ↓
Runtime Core Execution
        ↓
Data Source Runtime
        ↓
Rule Engine (DB Driven)
        ↓
Processing Engine
        ↓
Export Engine
        ↓
Delivery Engine
        ↓
History Engine
🔌 Component Architecture
1. Data Source Runtime
역할

입력 데이터 추상화 계층

지원
Excel
CSV
MariaDB
REST API
Shopify
SAP
표준
All Sources → DataFrame
2. Rule Engine
역할

데이터 조건 평가

Operators
IS_EMPTY
EQUALS
NOT_EQUALS
CONTAINS
STARTS_WITH
ENDS_WITH
GREATER_THAN
LESS_THAN
OLDER_THAN_DAYS
목표

코드 변경 없이 Rule 수정 가능

3. Processing Engine
역할

데이터 변환 처리

Filter
Grouping
Sorting
Join
Aggregation
Compare
4. Export Engine
역할

결과 생성

Excel
CSV
ZIP
DataFrame → File
5. Delivery Engine
역할

결과 전달

Download
Email
예정
Slack
Teams
6. History Engine
역할

실행 이력 저장

DB
TB_AUTOMATION_JOB
TB_AUTOMATION_JOB_HISTORY
TB_SCHEDULE_EXECUTION
Step History
READ_EXCEL
FILTER
GROUP
EXPORT
ZIP
MAIL
ERROR
🔁 Job Lifecycle
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

또는

Failed
🗄 Database Architecture
Schedule Domain
TB_AUTOMATION_SCHEDULE
TB_SCHEDULE_EXECUTION
Job Domain
TB_AUTOMATION_JOB
TB_AUTOMATION_JOB_HISTORY
Rule Domain
TB_RULE
TB_RULE_GROUP
TB_RULE_EXECUTION
File Domain (Future)
TB_FILE_UPLOAD
TB_OUTPUT_FILE
Storage
/uploads/YYYYMMDD/{job_id}
/output/YYYYMMDD/{job_id}
🚀 Runtime Execution Example
RepairPending Job
Excel Upload
    ↓
Data Source Runtime
    ↓
Rule Engine
    ↓
Processing Engine
    ↓
Export Engine
    ↓
ZIP Packaging
    ↓
Delivery Engine (Mail)
    ↓
History Engine
🏁 Future Architecture (v1.0.0)
Scheduler
    ↓
Runtime Platform (UI + Config)
    ↓
Runtime Core
    ↓
Configuration Layer
    ↓
Execution Engine
    ↓
Multi Source Runtime
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
🧭 Roadmap (WBS Alignment)
v0.6.x → Scheduler Runtime (완료)
v0.7.x → Runtime Productization (진행 핵심)
v0.8.x → Rule Engine 고도화
v0.9.x → Data Source Runtime
v1.0.0 → Automation Platform
🎯 Design Philosophy (핵심)

❌ Job을 만드는 시스템이 아니다
✅ Runtime 위에 설정을 쌓는 플랫폼이다