# 📘 JOB_CATALOG.md

# Automation Runtime Job Catalog

---

# 📌 Overview

Automation Runtime의 모든 Job은

**Execution Contract + Execution Pipeline** 으로 정의된다.

Runtime Core는 Job을 직접 실행하지 않는다.

Runtime Core는

* Contract 조회
* Pipeline 조회
* Step 실행

을 수행한다.

---

# 🧠 Core Principle

❌ Job = Python Class

✅ Job = Contract + Pipeline

```text
Input
 ↓
Pipeline
 ↓
Runtime Core
 ↓
Factory Runtime
 ↓
Output
 ↓
History
```

---

# 🏗 Runtime Execution Model

```text
Job Contract
      +
Execution Pipeline
      ↓
Runtime Core
      ↓
Step Executor
      ↓
Factory Runtime
```

---

# 🧾 Production Reference Job

## RepairPending

### Status

✅ Production Reference Job

### Description

수선업체 미처리 건 자동 추출

### Input

AS 접수현황 Excel

### Output

업체별 Excel

ZIP File

Email Delivery

---

### Current Pipeline

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

---

### Current Pipeline Step

| Order | Type         |
| ----- | ------------ |
| 1     | SOURCE       |
| 2     | RULE         |
| 3     | PROCESS      |
| 4     | EXPORT       |
| 5     | EXPORT (ZIP) |
| 6     | DELIVERY     |
| 7     | HISTORY      |

---

### Runtime Components

#### Reader

ExcelReader

#### Rule

RepairPending Rule Group

#### Processor

VendorGroupingProcessor

#### Export

VendorExcelExporter

ZipExporter

#### Delivery

EmailSender

#### History

HistoryWriter

---

# 🧩 Missing Detection Jobs

## InboundMissing

Status: Planned

### Pipeline

```text
SOURCE
 ↓
RULE
 ↓
EXPORT
 ↓
DELIVERY
```

---

## SettlementMissing

Status: Planned

### Pipeline

```text
SOURCE
 ↓
RULE
 ↓
EXPORT
 ↓
DELIVERY
```

---

# 🧩 Aging Analysis Jobs

## AgingRepair

Status: Planned

### Pipeline

```text
SOURCE
 ↓
RULE
 ↓
PROCESS
 ↓
EXPORT
```

---

## AgingInbound

Status: Planned

### Pipeline

```text
SOURCE
 ↓
RULE
 ↓
PROCESS
 ↓
EXPORT
```

---

# 🧩 Validation Jobs

## TcScanMissing

Status: Planned

### Pipeline

```text
SOURCE
 ↓
VALIDATION
 ↓
EXPORT
```

---

## DeliveryMismatch

Status: Planned

### Pipeline

```text
SOURCE
 ↓
COMPARE
 ↓
EXPORT
```

---

# 🧩 Inventory Jobs

## InventoryMismatch

Status: Planned

### Pipeline

```text
SOURCE
 ↓
COMPARE
 ↓
EXPORT
```

---

# 🧩 Reporting Jobs

## VendorSummary

Status: Planned

### Pipeline

```text
SOURCE
 ↓
AGGREGATION
 ↓
EXPORT
```

---

## DailySummary

Status: Planned

### Pipeline

```text
SOURCE
 ↓
AGGREGATION
 ↓
EXPORT
```

---

# ⚙ Factory Catalog

---

## ReaderFactory

### Current

ExcelReader

### Future

CsvReader

MariaDbReader

ApiReader

ShopifyReader

SapReader

---

## ProcessorFactory

### Current

VendorGroupingProcessor

### Future

AggregationProcessor

CompareProcessor

JoinProcessor

ValidationProcessor

---

## ExportFactory

### Current

VendorExcelExporter

ZipExporter

### Future

CsvExporter

PdfExporter

S3Exporter

---

## DeliveryFactory

### Current

EmailSender

### Future

SlackSender

TeamsSender

WebhookSender

---

# 🔁 Execution Contract Model

```json
{
  "input_source": "...",
  "rule_config": "...",
  "processing_config": "...",
  "export_config": "...",
  "delivery_config": "...",
  "schedule_config": "..."
}
```

---

# 🔁 Execution Pipeline Model

```json
[
  {
    "step_order": 1,
    "step_type": "SOURCE"
  },
  {
    "step_order": 2,
    "step_type": "RULE"
  },
  {
    "step_order": 3,
    "step_type": "PROCESS"
  },
  {
    "step_order": 4,
    "step_type": "EXPORT"
  }
]
```

---

# 🧠 Runtime Alignment

| Layer            | Responsibility      |
| ---------------- | ------------------- |
| Job Catalog      | Contract Definition |
| Pipeline Catalog | Execution Flow      |
| Runtime Core     | Orchestration       |
| Step Executor    | Step Routing        |
| ReaderFactory    | Input               |
| ProcessorFactory | Processing          |
| ExportFactory    | Output              |
| DeliveryFactory  | Delivery            |
| History Engine   | Audit               |

---

# 📊 Current Status

| Capability              | Status |
| ----------------------- | ------ |
| Runtime Core            | ✅      |
| Pipeline Runtime        | ✅      |
| Factory Runtime         | ✅      |
| Scheduler Runtime       | ✅      |
| Email Delivery          | ✅      |
| ZIP Export              | ✅      |
| Job Configuration       | 🚧     |
| Rule Configuration      | 🚧     |
| Scheduler Management UI | 🚧     |
| Multi Job Runtime       | 📋     |
| Data Source Runtime     | 📋     |

---

# 🎯 Design Philosophy

❌ Job을 만드는 시스템

✅ Runtime 위에 Contract와 Pipeline을 정의하는 플랫폼

```text
Execution Contract
        +
Execution Pipeline
        +
Runtime Core
        =
Automation Runtime
```
