Automation Runtime

업무 자동화를 위한 Python 기반 Runtime Platform

Current Version: v0.6.0

Overview

Automation Runtime은 반복적인 엑셀 기반 업무를 자동화하기 위해 설계된 Runtime 플랫폼이다.

단순한 개별 스크립트가 아니라,

Web UI 실행
Scheduler 기반 자동 실행
Job Registry
Rule Engine
Excel Processing
File Packaging
Mail Delivery
Execution History

를 하나의 공통 플랫폼으로 제공한다.

새로운 업무가 추가되더라도 Runtime은 그대로 유지하고 Job만 추가하는 구조를 목표로 한다.

Architecture
                 Web UI
                    │
                    ▼
            Automation Runtime
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼

  Job Registry   Scheduler    History DB

      ▼
  Rule Engine

      ▼
 Excel Processing

      ▼
 Export / ZIP

      ▼
 Mail Delivery
Core Features
Web Runtime

사용자가 브라우저를 통해 파일을 업로드하고 즉시 실행할 수 있다.

Scheduler Runtime

DB에 등록된 Cron Schedule을 기반으로 자동 실행할 수 있다.

Job Registry

새로운 업무를 플러그인 형태로 등록할 수 있다.

JOB_REGISTRY = {
    "repair_pending": RepairPendingJob,
    "inbound_missing": InboundMissingJob,
    "settlement_missing": SettlementMissingJob,
    "tc_scan": TcScanJob
}
Execution History

모든 실행 이력을 DB에 저장한다.

Job 실행 이력
Step 실행 이력
Scheduler 실행 이력
Technology Stack
Backend
Python 3.12
FastAPI
Jinja2
Uvicorn
Database
MariaDB
SQLAlchemy
Scheduler
APScheduler
Data Processing
Pandas
OpenPyXL
xlrd
Notification
SMTP
Gmail App Password
Database Design
TB_AUTOMATION_JOB

Job 실행 이력

TB_AUTOMATION_JOB_HISTORY

Step 실행 이력

TB_AUTOMATION_SCHEDULE

Cron Schedule 관리

TB_SCHEDULE_EXECUTION

Scheduler 실행 이력

Scheduler Flow
TB_AUTOMATION_SCHEDULE
            │
            ▼
      APScheduler
            │
            ▼
      Job Registry
            │
            ▼
       Job Execute
            │
            ▼
     History Logging
Supported Jobs
Job	Status
Repair Pending	Implemented
Inbound Missing	Planned
Settlement Missing	Planned
TC Scan	Planned
Version History
v0.6.0
APScheduler Integration
Database-driven Schedule Management
Scheduler Execution History
Automatic Job Execution
Job Registry Integration
v0.5.3
ZIP Download
Job Output Management
History UI Improvement
v0.5.0
FastAPI Runtime
Excel Upload
Web Execution
Roadmap
v0.7.0
Multi Job Expansion
Additional Automation Workflows
v0.8.0
Notification Expansion
Teams Integration
Slack Integration
v1.0.0
Production Deployment
User Authentication
Job Management Console
Dashboard
Design Philosophy
Input
  ↓
Rule Engine
  ↓
Processing
  ↓
Delivery
  ↓
History

업무마다 별도의 매크로를 만드는 것이 아니라,

공통 Runtime 위에 업무 규칙(Job)만 추가하여 확장 가능한 업무 자동화 플랫폼을 구축하는 것을 목표로 한다.