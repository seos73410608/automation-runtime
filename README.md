# Automation Runtime

설정 기반 업무 자동화를 위한 Python Runtime Platform

**Current Version: v0.8.0**

---

# Overview

Automation Runtime은 반복적인 엑셀 기반 업무를 자동화하기 위해 설계된 Runtime Platform이다.

단순한 개별 스크립트가 아니라,

* Runtime Core
* Pipeline Runtime
* Factory Runtime
* Web Runtime
* Scheduler Runtime
* Rule Engine
* Excel Processing
* Export Runtime
* Delivery Runtime
* Execution History

를 하나의 공통 플랫폼으로 제공한다.

새로운 업무가 추가되더라도 Runtime은 그대로 유지하고 Execution Pipeline만 추가하는 구조를 목표로 한다.

---

# Architecture

```text
                 Web UI
                    │
                    ▼

             Runtime Core

                    │

          Execution Pipeline

                    │

      ┌─────────────┼─────────────┐
      ▼             ▼             ▼

 ReaderFactory ProcessorFactory ExportFactory

                    │

             DeliveryFactory

                    │

              History Engine
```

---

# Core Features

## Runtime Core

Runtime 전체 실행 흐름 제어

* Pipeline 실행
* Context 관리
* Exception 처리
* History 기록

---

## Pipeline Runtime

DB 기반 실행 파이프라인

```text
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

지원 Step

* SOURCE
* RULE
* PROCESS
* EXPORT
* DELIVERY
* HISTORY

---

## Factory Runtime

### ReaderFactory

* ExcelReader

### ProcessorFactory

* VendorGroupingProcessor

### ExportFactory

* VendorExcelExporter
* ZipExporter

### DeliveryFactory

* EmailSender

---

## Web Runtime

사용자가 브라우저를 통해 파일을 업로드하고 즉시 실행할 수 있다.

지원 기능

* Upload
* Execute
* Download
* History 조회

---

## Scheduler Runtime

DB에 등록된 Cron Schedule을 기반으로 자동 실행할 수 있다.

지원 기능

* APScheduler
* Startup Registration
* Schedule Execution History
* Automatic Job Execution

---

## Execution History

모든 실행 이력을 DB에 저장한다.

* Job 실행 이력
* Step 실행 이력
* Scheduler 실행 이력

---

# Technology Stack

## Backend

* Python 3.12
* FastAPI
* Jinja2
* Uvicorn

## Database

* MariaDB
* SQLAlchemy

## Scheduler

* APScheduler

## Data Processing

* Pandas
* OpenPyXL
* xlrd

## Notification

* SMTP
* Gmail App Password

---

# Database Design

## Runtime Domain

TB_EXECUTION_PIPELINE

TB_JOB_CONFIG

---

## Job Domain

TB_AUTOMATION_JOB

TB_AUTOMATION_JOB_HISTORY

---

## Scheduler Domain

TB_AUTOMATION_SCHEDULE

TB_SCHEDULE_EXECUTION

---

# Runtime Execution Flow

```text
User / Scheduler
        ↓
Runtime Core
        ↓
Load Pipeline
        ↓
Execute Step
        ↓
Factory Runtime
        ↓
Output
        ↓
History
```

---

# Production Reference Job

## Repair Pending

Status

Production Reference Job

Pipeline

```text
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

지원 기능

* Excel Read
* Rule Filtering
* Vendor Grouping
* Vendor Excel Export
* ZIP Packaging
* Email Delivery
* History Logging

---

# Current Features

| Feature                 | Status |
| ----------------------- | ------ |
| Runtime Core            | ✅      |
| Pipeline Runtime        | ✅      |
| Factory Runtime         | ✅      |
| Web Runtime             | ✅      |
| Scheduler Runtime       | ✅      |
| Email Delivery          | ✅      |
| ZIP Export              | ✅      |
| Execution History       | ✅      |
| Job Configuration       | 🚧     |
| Rule Configuration      | 🚧     |
| Scheduler Management UI | 🚧     |

---

# Version History

## v0.8.0

* Pipeline Runtime Complete
* Factory Runtime Complete
* ExportFactory
* DeliveryFactory
* DB Pipeline Integration
* Runtime Core Refactoring

## v0.6.0

* APScheduler Integration
* Database-driven Schedule Management
* Scheduler Execution History
* Automatic Job Execution

## v0.5.x

* FastAPI Runtime
* Excel Upload
* Web Execution
* History UI

---

# Roadmap

## v0.8.x

Runtime Productization

* Job Configuration
* Rule Configuration
* Scheduler Management UI
* Operations Center

## v0.9.x

Data Source Runtime

* CSV
* MariaDB
* REST API

## v1.0.0

Automation Platform

* Multi Job Runtime
* Rule Engine
* Data Source Runtime
* Slack Delivery
* Teams Delivery
* Dashboard

---

# Design Philosophy

```text
Input
 ↓
Pipeline
 ↓
Processing
 ↓
Delivery
 ↓
History
```

업무마다 별도의 매크로를 만드는 것이 아니라,

공통 Runtime 위에 Execution Pipeline과 Configuration을 추가하여 확장 가능한 업무 자동화 플랫폼을 구축하는 것을 목표로 한다.

---

## Core Principle

❌ Job 중심 시스템

❌ 업무별 스크립트 생성

✅ Runtime 중심 플랫폼

✅ Pipeline 기반 실행

✅ Configuration 기반 확장

```text
Execution Contract
        +
Execution Pipeline
        +
Runtime Core
        =
Automation Runtime
```
