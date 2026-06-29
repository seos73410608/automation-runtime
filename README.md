# Automation Runtime

Configuration Driven Automation Runtime Platform

**Current Version: v0.9.0**

---

# Overview

Automation Runtime은 반복적인 업무를 설정(Configuration)만으로 실행할 수 있도록 설계된 Runtime Platform이다.

업무별 Python Script를 만드는 것이 아니라,

* Runtime Core
* Pipeline Runtime
* Factory Runtime
* Rule Runtime
* Scheduler Runtime
* Web Runtime
* Export Runtime
* Delivery Runtime
* History Runtime

위에 새로운 Pipeline과 Configuration만 추가하여 업무를 확장하는 구조를 목표로 한다.

---

# Runtime Architecture

```text
               Web UI
                  │
                  ▼

            Runtime Service

                  │
                  ▼

             Runtime Core

                  │
                  ▼

          Pipeline Loader

                  │
                  ▼

             Step Executor

                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼

   SOURCE       RULE      PROCESS
      │           │           │
      ▼           ▼           ▼

   EXPORT     DELIVERY    HISTORY

                  │
                  ▼

        Execution Log Repository
```

---

# Runtime Pipeline

지원 Step

```
SOURCE
 ↓
RULE
 ↓
PROCESS
 ↓
EXPORT
 ↓
DELIVERY
 ↓
HISTORY
```

RuntimeCore가 모든 Step을 순차적으로 실행하며 StepContext를 공유한다.

---

# Runtime Core

주요 역할

* Pipeline Load
* Step Execute
* Runtime Metadata 관리
* Exception Handling
* Execution Log 저장

---

# Runtime Components

## PipelineLoader

DB에서 Pipeline 정보를 로드한다.

* Job Configuration
* Input Configuration
* Output Configuration
* Step Configuration

---

## StepExecutor

Step Type에 따라 Factory를 호출한다.

지원 Step

* SOURCE
* RULE
* PROCESS
* EXPORT
* DELIVERY
* HISTORY

---

## StepContext

Runtime 전체에서 공유되는 Context

관리 정보

* Job Metadata
* Runtime Status
* Runtime Duration
* Input Data
* Output Data
* Error Information

---

# Factory Runtime

## ReaderFactory

* ExcelReader

지원

* xls
* xlsx

---

## Rule Runtime

지원 Rule

* Repair Pending Rule
* Order Validation Rule

---

## ProcessorFactory

* VendorGroupingProcessor

---

## ExportFactory

* VendorExcelExporter
* ZipExporter

---

## DeliveryFactory

* EmailSender

SMTP 기반 메일 발송 지원

---

## History Runtime

HistoryWriter

운영 Job만 History 저장

테스트 Job은 자동 Skip

---

## Execution Log

ExecutionLogRepository

모든 Runtime 실행 결과 저장

기록 항목

* Job
* Runtime
* Duration
* Status
* Error Message
* Statistics

---

# Built-in Jobs

## Repair Pending

Pipeline

```
SOURCE
 ↓
RULE
 ↓
PROCESS
 ↓
EXPORT
 ↓
ZIP EXPORT
 ↓
DELIVERY
 ↓
HISTORY
```

기능

* Excel Read
* Vendor Grouping
* Vendor Export
* ZIP Export
* Email Delivery
* History Logging

---

## Order Validation

Pipeline

```
SOURCE
 ↓
RULE
 ↓
HISTORY
```

기능

* Excel Read
* Event Validation
* Invalid Data Filtering
* Execution Logging

---

# Technology Stack

## Backend

* Python 3.12
* FastAPI
* SQLAlchemy
* Uvicorn

## Database

* MariaDB

## Scheduler

* APScheduler

## Data

* Pandas
* OpenPyXL
* xlrd

## Delivery

* SMTP
* Gmail

---

# Database

주요 테이블

## Runtime

* TB_EXECUTION_PIPELINE
* TB_RUNTIME_EXECUTION_LOG

## Job

* TB_AUTOMATION_JOB
* TB_AUTOMATION_JOB_STEP
* TB_AUTOMATION_JOB_HISTORY

## Scheduler

* TB_AUTOMATION_SCHEDULE
* TB_SCHEDULE_EXECUTION

---

# Current Features

| Feature                 | Status |
| ----------------------- | ------ |
| Runtime Core            | ✅      |
| Pipeline Runtime        | ✅      |
| Factory Runtime         | ✅      |
| Rule Runtime            | ✅      |
| Execution Log           | ✅      |
| History Runtime         | ✅      |
| Excel Runtime           | ✅      |
| ZIP Export              | ✅      |
| Email Delivery          | ✅      |
| Scheduler Runtime       | ✅      |
| Order Validation        | ✅      |
| Job Configuration UI    | 🚧     |
| Scheduler Management UI | 🚧     |

---

# Version History

## v0.9.0

* Runtime Metadata
* Execution Log
* History Runtime 개선
* Order Validation Runtime
* Rule Runtime 확장
* Runtime 안정화

## v0.8.0

* Pipeline Runtime
* Factory Runtime
* Export Runtime
* Delivery Runtime

## v0.6.0

* Scheduler Runtime

## v0.5.x

* Web Runtime
* Excel Upload

---

# Roadmap

## v0.10.x

* Job Configuration
* Rule Configuration
* Scheduler Management UI
* Runtime Dashboard

## v1.0.0

Automation Platform

* Multi Runtime
* REST Runtime
* CSV Runtime
* Database Runtime
* Slack Delivery
* Teams Delivery
* Monitoring Dashboard

---

# Design Philosophy

```
Configuration
      ↓

Execution Pipeline
      ↓

Runtime Core
      ↓

Factory Runtime
      ↓

Delivery
      ↓

Execution Log
```

Runtime는 변경하지 않는다.

Pipeline과 Configuration만 추가하여 업무를 확장한다.

---

# Core Principle

❌ Job 중심

❌ 업무별 Script

✅ Runtime 중심

✅ Pipeline 기반

✅ Configuration 기반

```
Execution Contract
        +
Execution Pipeline
        +
Runtime Core
        =
Automation Runtime Platform
```
