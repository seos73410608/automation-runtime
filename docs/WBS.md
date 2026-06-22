# Automation Runtime WBS

## Project

Automation Runtime

---

# 📌 Overview

Start Date: 2026-06-15

Current Version: v0.8.0

Target Version: v1.0.0

Target Date: 2026 Q4

---

# 🧱 Phase 1. Runtime Core

기간: 2026-06-15 ~ 2026-06-18

버전: v0.1.0 ~ v0.4.x

상태: ✅ 완료

## 목표

업무 자동화 Runtime 구축

## 산출물

* Project Structure
* BaseJob Framework
* Excel Reader
* Rule Filter
* Vendor Grouping
* Excel Export
* ZIP Packaging
* Logging
* JobResult
* RepairPendingJob

---

# 🌐 Phase 2. Web Runtime

기간: 2026-06-18 ~ 2026-06-19

버전: v0.5.0

상태: ✅ 완료

## 산출물

* FastAPI
* Upload UI
* Execution UI
* Result UI
* Download UI

---

# 📧 Phase 3. Notification Runtime

기간: 2026-06-19

버전: v0.5.1

상태: ✅ 완료

## 산출물

* SMTP
* Mail Template
* ZIP Attachment
* Environment Configuration

---

# 📊 Phase 4. Runtime Monitoring

기간: 2026-06-19 ~ 2026-06-20

버전: v0.5.2 ~ v0.5.4

상태: ✅ 완료

## 산출물

* MariaDB
* SQLAlchemy
* Job History
* Step History
* History UI
* Detail UI
* 날짜별 파일 관리

---

# ⏱ Phase 5. Scheduler Runtime

기간: 2026-06-20

버전: v0.6.0

상태: ✅ 완료

## 산출물

* APScheduler
* Cron Loader
* Schedule Registry
* Execution History
* Startup Registration

---

# ⚙️ Phase 6. Runtime Pipeline Engine

기간: 2026-06-21

버전: v0.7.2

상태: ✅ 완료

## 목표

Job 중심 구조 제거

Pipeline 기반 Runtime 구축

## 산출물

* RuntimeCore
* PipelineLoader
* StepExecutor
* StepContext
* TB_EXECUTION_PIPELINE
* DB Driven Execution

---

# 🧩 Phase 7. Runtime Factory Architecture

기간: 2026-06-22

버전: v0.7.3 ~ v0.8.0

상태: ✅ 완료

## 목표

실행 컴포넌트 Factory 기반 전환

## 산출물

### ReaderFactory

* ExcelReader

### ProcessorFactory

* VendorGroupingProcessor

### ExportFactory

* VendorExcelExporter
* ZipExporter

### DeliveryFactory

* EmailSender

## 결과

Pipeline 설정 기반 Runtime 실행

예시:

SOURCE
↓
RULE
↓
PROCESS
↓
EXPORT
↓
DELIVERY

---

# 🚧 Phase 8. Runtime Productization

기간: 2026-07

버전: v0.9.0

상태: 예정

## 목표

RepairPending Runtime 완전 제품화

### JobFactory 제거

현재

RuntimeService
↓
JobFactory
↓
RepairPendingJob
↓
RuntimeCore

변경

RuntimeService
↓
RuntimeCore
↓
Pipeline

### HistoryFactory

* HistoryWriter

### RuleFactory

* Rule Runtime 분리

---

# 🚧 Phase 9. Scheduler Management

기간: 2026-07

버전: v0.9.x

상태: 예정

## 기능

### Schedule Management

* 등록
* 수정
* 삭제
* 활성화
* 비활성화

### Execution Monitoring

* 실행 이력
* 마지막 결과
* Run Now

---

# 🚀 Phase 10. Multi Job Runtime

기간: 2026-08

버전: v0.9.x

상태: 예정

## 목표

여러 업무 Runtime 지원

### Job Catalog

* RepairPending
* InboundMissing
* SettlementMissing
* TcScanMissing
* AgingRepair
* AgingInbound
* DeliveryMismatch
* VendorSummary

---

# 🧠 Phase 11. Rule Engine

기간: 2026-08 ~ 2026-09

버전: v1.0.0-rc

상태: 예정

## 목표

코드 없는 Rule 관리

### Operator

* IS_EMPTY
* EQUALS
* NOT_EQUALS
* CONTAINS
* GREATER_THAN
* LESS_THAN
* OLDER_THAN_DAYS

### UI

* Rule 등록
* Rule 수정
* Rule 테스트
* Preview

---

# 🔌 Phase 12. Data Source Runtime

기간: 2026-10

버전: v1.0.0-rc

상태: 예정

## Source Adapter

* Excel
* CSV
* MariaDB
* REST API

---

# 🏁 Phase 13. Automation Platform

기간: 2026 Q4

버전: v1.0.0

상태: 목표

## Platform Features

### Runtime

* Multi Job Runtime
* Rule Engine
* Scheduler Runtime
* Source Runtime

### Delivery

* Email
* Slack
* Teams

### Dashboard

* Job Dashboard
* Schedule Dashboard
* Execution Dashboard

### Storage

* File Metadata
* S3 Integration

---

# 🎯 Success Criteria

## 기술 목표

* Job 추가 시 Runtime 수정 없음
* Rule 변경 시 코드 수정 없음
* Source 변경 시 Job 수정 없음
* Delivery 변경 시 Job 수정 없음

## 플랫폼 목표

Input
↓
Rule
↓
Processing
↓
Delivery
↓
History

---

# 🧠 최종 구조

RuntimeCore
↓
Pipeline
↓
Factory
↓
Component

모든 업무는 동일한 Runtime Lifecycle 위에서 동작한다.
