📘 JOB_CATALOG.md (Final - Runtime Productization 반영)
Automation Runtime Job Catalog
📌 Overview

Automation Runtime의 모든 Job은
Configuration 기반 Execution Contract이다.

각 Job은 Runtime Core 위에서 동일한 Lifecycle을 따른다.

Input
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
🧠 Core Principle

❗ Job은 코드가 아니라 “Runtime Execution Contract”이다

Job = Input + Rule + Processing + Output + Delivery + History
🧩 Category 1. Missing Detection
🧾 RepairPending (REFERENCE JOB - PRODUCTION)
📌 설명

수선업체 의뢰 후 미완료 건 탐지 (Reference Job)

📥 입력
AS 접수현황 Excel
📤 출력
업체별 Excel
ZIP File
Mail Delivery
⚙️ Required Engines
Filter Engine
Group Engine
Export Engine
Delivery Engine
History Engine
📊 Status
Implemented (Reference Job - Production Baseline)
🧾 InboundMissing
📌 설명

입고 예정 대비 미입고 데이터 탐지

📥 입력
입고 현황 Excel
📤 출력
누락 리스트 Excel
⚙️ Required Engines
Filter Engine
Export Engine
History Engine
📊 Status

Planned

🧾 SettlementMissing
📌 설명

정산 대상 대비 미정산 데이터 탐지

📥 입력
정산 데이터
📤 출력
정산 누락 리스트
⚙️ Required Engines
Filter Engine
Export Engine
📊 Status

Planned

🧩 Category 2. Aging Analysis
🧾 AgingRepair
📌 설명

30일 이상 미처리 수선 건 분석

📥 입력
AS 접수현황
⚙️ Engines
Filter Engine
Date Engine
Export Engine
📊 Status

Planned

🧾 AgingInbound

입고 지연 분석 Job

📥 입력
입고 데이터
⚙️ Engines
Filter Engine
Date Engine
Export Engine
📊 Status

Planned

🧩 Category 3. Validation
🧾 TcScanMissing
📌 설명

TC 스캔 누락 검증

📥 입력
TC Scan Data
⚙️ Engines
Validation Engine
Filter Engine
Export Engine
📊 Status

Planned

🧾 DeliveryMismatch
📌 설명

출고 vs 배송 데이터 불일치 검증

📥 입력
출고 데이터
배송 데이터
⚙️ Engines
Join Engine
Compare Engine
Export Engine
📊 Status

Planned

🧩 Category 4. Inventory
🧾 InventoryMismatch
📌 설명

ERP vs WMS 재고 불일치 검증

📥 입력
ERP 재고
WMS 재고
⚙️ Engines
Compare Engine
Export Engine
📊 Status

Planned

🧩 Category 5. Reporting
🧾 VendorSummary
📌 설명

업체별 처리 현황 집계

📥 입력
Execution Result Data
⚙️ Engines
Aggregation Engine
Export Engine
📊 Status

Planned

🧾 DailySummary
📌 설명

일일 운영 리포트 생성

📥 입력
Runtime Execution Logs
⚙️ Engines
Aggregation Engine
Dashboard Engine
📊 Status

Planned

⚙️ Engine Catalog (Aligned with Architecture)
1. Filter Engine
IS_EMPTY
EQUALS
NOT_EQUALS
CONTAINS
STARTS_WITH
ENDS_WITH
2. Date Engine
OLDER_THAN_DAYS
BEFORE_DATE
AFTER_DATE
3. Group Engine
업체별 그룹
매장별 그룹
Job Key 기반 그룹핑
4. Compare Engine
ERP vs WMS
주문 vs 배송
Snapshot 비교
5. Join Engine
Multi Dataset Merge
Inner / Left Join
6. Aggregation Engine
COUNT
SUM
AVG
7. Validation Engine
Format Check
Null Check
Business Rule Validation
8. Delivery Engine
Excel Export
CSV Export
ZIP Packaging
Mail Delivery
Dashboard Publishing (Future)
🔁 Execution Contract Model (IMPORTANT)
Job Execution Contract = {
  input_source,
  rule_config,
  processing_config,
  export_config,
  delivery_config,
  schedule_config
}

👉 Job = Execution Contract (NOT code)

🧠 Runtime Alignment (Architecture Mapping)
Layer	Role
Job Catalog	Execution Contract Definition
Runtime Core	Orchestration Engine
Configuration Layer	Runtime Behavior Definition
Rule Engine	Decision Layer
Processing Engine	Transformation Layer
Delivery Engine	Output Layer
History Engine	Audit Layer
🚀 Execution Flow (Final)
Trigger (User / Scheduler)
        ↓
Load Job Contract
        ↓
Runtime Core Execution
        ↓
Data Source Runtime
        ↓
Rule Engine (Config Driven)
        ↓
Processing Engine
        ↓
Export Engine
        ↓
Delivery Engine
        ↓
History Engine
🧠 Key Architectural Shift
❌ BEFORE
Job = Python Class
Job = 기능 단위 코드
✅ AFTER
Job = Execution Contract (DB / Config)
Runtime Core = 실행 엔진
Engine = 재사용 가능한 기능 단위
📊 Status Summary
Job	Status
RepairPending	Production Reference
InboundMissing	Planned
SettlementMissing	Planned
TcScanMissing	Planned
AgingRepair	Planned
DeliveryMismatch	Planned
InventoryMismatch	Planned
VendorSummary	Planned
DailySummary	Planned
🎯 Design Philosophy (Final)

❌ Job을 만드는 시스템이 아니다
✅ Runtime 위에 Execution Contract를 쌓는 플랫폼이다