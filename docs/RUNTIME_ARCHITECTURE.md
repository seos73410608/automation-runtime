# 📘 RUNTIME_ARCHITECTURE.md

## Automation Runtime Architecture

---

# 📌 Overview

Automation Runtime은

**Configuration Driven + Pipeline Driven Runtime Platform**

이다.

모든 업무는 동일한 Runtime Core 위에서 동작하며,

Job 별 로직은 Runtime 변경 없이

DB Configuration + Execution Pipeline 으로 정의된다.

---

# 🧠 Core Principle

기존

Job
→ Code
→ Execute

현재

Job
→ Pipeline Configuration
→ Runtime Core
→ Factory Runtime
→ Execute

즉

❌ Job 중심

✅ Runtime 중심

---

# 🏗 Runtime Layers

User / Scheduler
↓
Runtime Platform
↓
Runtime Service
↓
Runtime Core
↓
Pipeline Loader
↓
Step Executor
↓
Factory Layer
↓
Business Components

---

# ⚙ Runtime Core

## 역할

Runtime 전체 오케스트레이션

### Responsibilities

* Pipeline Load
* Step Routing
* Step Execution
* Context Management
* Error Handling
* Logging
* History Management

---

## Runtime Flow

Trigger
↓
RuntimeService
↓
RuntimeCore
↓
PipelineLoader
↓
ExecutionPipeline
↓
StepExecutor
↓
Factories
↓
Business Components

---

# 🧩 Execution Pipeline

## DB

TB_EXECUTION_PIPELINE

---

예시

STEP 1
SOURCE

↓

STEP 2
RULE

↓

STEP 3
PROCESS

↓

STEP 4
EXPORT

↓

STEP 5
ZIP

↓

STEP 6
DELIVERY

↓

STEP 7
HISTORY

---

Pipeline 수정 시

코드 변경 없이

실행 순서 변경 가능

---

# 🏭 Factory Runtime (v0.8.0)

## 목적

StepExecutor의 if/else 제거

확장성 확보

---

## Reader Factory

ReaderFactory

지원

* ExcelReader
* CsvReader (예정)
* DBReader (예정)
* ApiReader (예정)

---

## Processor Factory

ProcessorFactory

지원

* VendorGroupingProcessor
* AgingProcessor (예정)
* CompareProcessor (예정)

---

## Export Factory

ExportFactory

지원

* VendorExcelExporter
* ZipExporter

---

## Delivery Factory

DeliveryFactory

지원

* EmailSender

예정

* SlackSender
* TeamsSender

---

# 🔄 Step Executor

현재 Runtime의 핵심 Router

SOURCE
↓
ReaderFactory

RULE
↓
RuleService

PROCESS
↓
ProcessorFactory

EXPORT
↓
ExportFactory

DELIVERY
↓
DeliveryFactory

HISTORY
↓
History Service

---

# 🧠 Context Architecture

## StepContext

Runtime 전체 상태 관리

보유 정보

* job_id
* file_name
* file_path
* data

---

Data 흐름

Excel DataFrame

↓

Filtered DataFrame

↓

Vendor Groups

↓

Excel Files

↓

ZIP File

↓

Mail Attachment

---

# 📚 Rule Engine

현재

DB Driven Rule Engine

---

구조

TB_RULE_GROUP

↓

TB_RULE

↓

RuleRepository

↓

RuleService

↓

Mask

↓

DataFrame Filtering

---

지원

* EQUALS
* NOT_EQUALS
* CONTAINS
* IS_EMPTY

예정

* GREATER_THAN
* LESS_THAN
* OLDER_THAN_DAYS

---

# 📦 Export Runtime

## VendorExcelExporter

입력

Vendor Groups

출력

Vendor Excel Files

---

## ZipExporter

입력

Excel Files

출력

result.zip

---

# 📧 Delivery Runtime

## EmailSender

입력

ZIP File

출력

SMTP Delivery

---

현재

ZIP 첨부 자동 발송 완료

---

# 🗄 Database Architecture

## Runtime

TB_JOB_CONFIG

TB_EXECUTION_PIPELINE

---

## Scheduler

TB_AUTOMATION_SCHEDULE

TB_SCHEDULE_EXECUTION

---

## Rule

TB_RULE

TB_RULE_GROUP

---

## History

TB_AUTOMATION_JOB

TB_AUTOMATION_JOB_HISTORY

---

# 🚀 Runtime Execution Example

repair_pending

SOURCE
↓
ExcelReader

RULE
↓
RuleService

PROCESS
↓
VendorGroupingProcessor

EXPORT
↓
VendorExcelExporter

EXPORT
↓
ZipExporter

DELIVERY
↓
EmailSender

HISTORY
↓
HistoryWriter

---

# 🧭 Runtime Roadmap

## v0.8.0 (완료)

* Runtime Core
* Pipeline Runtime
* Factory Runtime
* DB Driven Pipeline
* ZIP Export
* Email Delivery

---

## v0.9.0

* Scheduler UI
* Schedule Management
* Run Now
* Execution Monitoring

---

## v0.9.x

* Rule Management UI
* Rule Preview
* Rule Testing

---

## v1.0.0

* Multi Job Runtime
* Multi Source Runtime
* Rule Engine Complete
* Slack Delivery
* Teams Delivery
* Runtime Platform

---

# 🎯 Design Philosophy

❌ Job을 개발하는 시스템

❌ 업무별 프로그램

✅ Runtime Platform

✅ Configuration Driven System

✅ Pipeline Driven Architecture

---

모든 업무는

Runtime Core

*

Execution Pipeline

*

Factory Runtime

위에서 동작한다.
