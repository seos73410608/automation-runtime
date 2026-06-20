JOB_CATALOG.md
Automation Runtime Job Catalog
Overview

Automation Runtime은 다양한 업무 자동화를 공통 Runtime 위에서 수행하기 위한 플랫폼이다.

각 업무는 Job 단위로 정의되며,

모든 Job은 다음 흐름을 따른다.

Input
↓
Rule Engine
↓
Processing
↓
Delivery
↓
History

Category 1. Missing Detection
RepairPending
설명

수선업체 의뢰 후 완료되지 않은 건 탐지

입력
AS 접수현황 Excel
출력
업체별 Excel
ZIP
Mail
Required Engine
Filter Engine
Group Engine
Export Engine
Mail Engine
Status

Implemented

InboundMissing
설명

입고 예정이나 입고되지 않은 건 탐지

입력
입고 현황 Excel
출력
누락 리스트 Excel
Required Engine
Filter Engine
Export Engine
Status

Planned

SettlementMissing
설명

정산 대상이나 정산되지 않은 건 탐지

입력
정산 데이터
출력
정산 누락 리스트
Required Engine
Filter Engine
Export Engine
Status

Planned

Category 2. Aging Analysis
AgingRepair
설명

30일 이상 미처리 수선 건 탐지

입력
AS 접수현황
출력
장기 미처리 리스트
Required Engine
Filter Engine
Date Engine
Export Engine
Status

Planned

AgingInbound
설명

입고 지연 건 탐지

입력
입고 데이터
출력
입고 지연 리스트
Required Engine
Filter Engine
Date Engine
Export Engine
Status

Planned

Category 3. Validation
TcScanMissing
설명

TC 스캔 누락 건 탐지

입력
TC 스캔 데이터
출력
미스캔 리스트
Required Engine
Validation Engine
Export Engine
Status

Planned

DeliveryMismatch
설명

출고 데이터와 배송 데이터 불일치 탐지

입력
출고 데이터
배송 데이터
출력
불일치 리스트
Required Engine
Join Engine
Compare Engine
Export Engine
Status

Planned

Category 4. Inventory
InventoryMismatch
설명

재고 수량 불일치 탐지

입력
WMS 재고
ERP 재고
출력
재고 차이 리스트
Required Engine
Compare Engine
Export Engine
Status

Planned

Category 5. Reporting
VendorSummary
설명

업체별 처리 현황 집계

입력
처리 결과 데이터
출력
업체별 집계 보고서
Required Engine
Aggregation Engine
Export Engine
Status

Planned

DailySummary
설명

일일 업무 현황 집계

입력
Runtime 실행 데이터
출력
Daily Report
Required Engine
Aggregation Engine
Dashboard Engine
Status

Planned

Engine Catalog
Filter Engine

조건 기반 데이터 필터링

예시

IS_EMPTY
EQUALS
NOT_EQUALS
CONTAINS
Date Engine

날짜 계산

예시

OLDER_THAN_DAYS
BEFORE_DATE
AFTER_DATE
Group Engine

데이터 그룹핑

예시

업체별 그룹
매장별 그룹
Compare Engine

두 데이터셋 비교

예시

재고 비교
주문 비교
Join Engine

다중 데이터셋 조인

예시

출고 + 배송
ERP + WMS
Aggregation Engine

집계

예시

COUNT
SUM
AVG
Delivery Engine

결과 전달

예시

Excel
ZIP
Mail
Dashboard