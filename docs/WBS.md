📘 WBS.md (Revised)
Project

Automation Runtime

📌 Overview
Start Date: 2026-06-15
Target Version: v1.0.0
Target Date: 2026 Q4
🧱 Phase 1. Runtime Core (완료)
기간: 2026-06-15 ~ 2026-06-18
버전: v0.1.0 ~ v0.4.x
상태: ✅ 완료
목표

업무 자동화 공통 Runtime 구축

산출물
Project Structure
BaseJob Framework
Excel Reader
Rule Filter
Vendor Grouping
Excel Export
ZIP Packaging
Logging
JobResult Model
RepairPendingJob
🌐 Phase 2. Web Runtime (완료)
기간: 2026-06-18 ~ 2026-06-19
버전: v0.5.0
상태: ✅ 완료
목표

사용자 실행 인터페이스 구축

산출물
FastAPI Runtime
Upload UI
Execution UI
Result UI
Download UI
📧 Phase 3. Notification Runtime (완료)
기간: 2026-06-19
버전: v0.5.1
상태: ✅ 완료
목표

결과 전달 자동화

산출물
SMTP
Mail Template
ZIP Attachment
Environment Configuration
📊 Phase 4. Runtime Monitoring (완료)
기간: 2026-06-19 ~ 2026-06-20
버전: v0.5.2 ~ v0.5.4
상태: ✅ 완료
목표

실행 이력 및 운영 추적

산출물
MariaDB
SQLAlchemy
Job History
Step History
History UI
Detail UI
날짜별 파일 관리
다운로드 이력 구조
⏱ Phase 5. Scheduler Runtime (완료)
기간: 2026-06-20
버전: v0.6.0
상태: ✅ 완료
목표

무인 자동 실행 Runtime

산출물
APScheduler
Schedule Registry
Cron Loader
Schedule Execution History
Startup Registration
Scheduler Integration
⚙️ Phase 6. Scheduler Management (진행 예정)
기간: 2026-06 ~ 2026-07
버전: v0.7.0 ~ v0.7.1
상태: 🚧 진행 예정
🎯 목표

Scheduler를 운영 가능한 제품 UI로 전환

📦 핵심 기능
Schedule Management
Schedule 목록 조회
Schedule 등록
Schedule 수정
Schedule 삭제
Schedule 활성/비활성
Execution Monitoring
실행 이력 조회
마지막 실행 결과 조회
Run Now (즉시 실행)
DB
TB_AUTOMATION_SCHEDULE
TB_SCHEDULE_EXECUTION
🧩 Phase 7. Runtime Productization (NEW 핵심)
기간: 2026-07
버전: v0.7.2 ~ v0.7.4
상태: 📋 계획
🎯 목표

RepairPending Runtime을 설정 기반 제품으로 전환

7.1 Job Configuration
수신자 관리
출력 경로 설정
파일명 정책
보관 기간 설정

👉 코드 변경 없이 운영 설정 가능

7.2 Rule Management UI
Rule 조회
Rule 수정
Rule 테스트
Rule Preview (데이터 기준 결과 확인)

👉 Rule을 “코드 → 데이터”로 전환

7.3 Operations Center
실패 이력 조회
재실행 기능
오류 로그 확인
실행 통계

👉 운영 시스템화

🚀 Phase 8. Multi Job Runtime
기간: 2026-08
버전: v0.8.x
상태: 📋 계획
목표

여러 Job 확장 지원 (단, Productization 이후)

Job Catalog
RepairPending (Reference Job)
InboundMissing
SettlementMissing
TcScanMissing
AgingRepair
AgingInbound
DeliveryMismatch
VendorSummary
UI
Job 선택 화면
Job 실행 화면
🧠 Phase 9. Rule Engine (고도화)
기간: 2026-08 ~ 2026-09
버전: v0.8.x
상태: 📋 계획
목표

코드 없는 Rule Engine 완성

Rule Operator
IS_EMPTY
EQUALS
NOT_EQUALS
CONTAINS
GREATER_THAN
LESS_THAN
OLDER_THAN_DAYS
Rule UI
Rule 등록
Rule 수정
Rule 테스트
🔌 Phase 10. Data Source Runtime
기간: 2026-10
버전: v0.9.x
상태: 📋 계획
목표

데이터 입력 구조 추상화

Source Adapter
Excel
CSV
MariaDB
REST API
Shopify
SAP
Output
DataFrame 기반 표준화
🏁 Phase 11. Automation Platform
기간: 2026 Q4
버전: v1.0.0
상태: 🎯 목표
목표

범용 업무 자동화 플랫폼

Platform Features
Multi Job Runtime
Rule Engine
Scheduler Runtime
Data Source Runtime
Delivery Expansion
Delivery Channels
Email
Slack
Teams
Dashboard
Job Dashboard
Schedule Dashboard
Execution Dashboard
Storage
File Metadata
S3 Integration
🎯 Success Criteria
🧠 기술 목표
Job 추가 시 Runtime 수정 없음
Rule 변경 시 코드 수정 없음
Source 변경 시 Job 수정 없음
🏢 운영 목표
수동 엑셀 작업 제거
반복 업무 자동화
실행 이력 추적 가능
🧩 플랫폼 목표
Input
 ↓
Rule
 ↓
Processing
 ↓
Delivery
 ↓
History
🧠 핵심 구조 정의

모든 업무는 동일한 Runtime Lifecycle 위에서 동작한다.

🔥 최종 정리

이 WBS의 핵심 변화는 하나다:

❌ BEFORE
Job 중심 구조
기능 확장 중심
✅ AFTER
Runtime Productization 중심
운영 가능한 시스템 중심
설정 기반 구조로 전환