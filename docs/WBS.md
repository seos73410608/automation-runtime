WBS.md
Project

Automation Runtime

Start Date

2026-06-15

Target Version

v1.0.0

Target Date

2026 Q4

Phase 1. Runtime Core
기간

2026-06-15 ~ 2026-06-18

버전

v0.1.0 ~ v0.4.x

목표

업무 자동화 공통 Runtime 구축

완료
Project Structure
BaseJob Framework
Excel Reader
Rule Filter
Vendor Grouping
Excel Export
ZIP Packaging
Logging
JobResult Model
산출물
RepairPendingJob
상태

✅ 완료

Phase 2. Web Runtime
기간

2026-06-18 ~ 2026-06-19

버전

v0.5.0

목표

사용자 실행 인터페이스 구축

완료
FastAPI Runtime
Upload UI
Execution UI
Result UI
Download UI
상태

✅ 완료

Phase 3. Notification Runtime
기간

2026-06-19

버전

v0.5.1

목표

결과 전달 자동화

완료
SMTP
Mail Template
ZIP Attachment
Environment Configuration
상태

✅ 완료

Phase 4. Runtime Monitoring
기간

2026-06-19 ~ 2026-06-20

버전

v0.5.2 ~ v0.5.4

목표

실행 이력 및 운영 추적

완료
MariaDB
SQLAlchemy
Job History
Step History
History UI
Detail UI
날짜별 파일 관리
다운로드 이력 구조
상태

✅ 완료

Phase 5. Scheduler Runtime
기간

2026-06-20

버전

v0.6.0

목표

무인 자동 실행

완료
APScheduler
Schedule Registry
Cron Loader
Schedule Execution History
Startup Registration
Scheduler Integration
상태

✅ 완료

Phase 6. Scheduler Management
기간

2026-06

버전

v0.6.x

목표

웹 기반 스케줄 관리

예정
Schedule UI
Schedule 목록 조회
Schedule 등록
Schedule 수정
Schedule 삭제
Execution Monitoring
실행 이력 조회
마지막 실행 결과 조회
DB

TB_AUTOMATION_SCHEDULE

TB_SCHEDULE_EXECUTION

상태

🚧 진행 예정

Phase 7. Multi Job Runtime
기간

2026-07

버전

v0.7.x

목표

여러 업무 자동화 지원

예정
Job Registry 확장
RepairPending
InboundMissing
SettlementMissing
TcScanMissing
Job Catalog 기반 확장
AgingRepair
AgingInbound
DeliveryMismatch
VendorSummary
UI
Job 선택 화면
Job 실행 화면
상태

📋 계획

Phase 8. Rule Engine
기간

2026-08 ~ 2026-09

버전

v0.8.x

목표

코드 없는 Rule 기반 처리

예정
Rule Model

TB_RULE

TB_RULE_GROUP

TB_RULE_EXECUTION

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
상태

📋 계획

Phase 9. Data Source Runtime
기간

2026-10

버전

v0.9.x

목표

데이터 입력 추상화

예정
Source Adapter
Excel
CSV
MariaDB
REST API
External Source
Shopify
SAP
Output Standardization
DataFrame 기반 통합
상태

📋 계획

Phase 10. Automation Platform
기간

2026 Q4

버전

v1.0.0

목표

범용 업무 자동화 플랫폼

예정
Platform Features
Multi Job Runtime
Rule Engine
Scheduler Runtime
Data Source Runtime
Delivery Expansion
Mail
Slack
Teams
Dashboard
Job Dashboard
Schedule Dashboard
Execution Dashboard
Storage
File Metadata
S3 Integration
상태

📋 목표

Success Criteria
기술 목표
Job 추가 시 Runtime 수정 없음
Rule 변경 시 코드 수정 없음
Source 변경 시 Job 수정 없음
운영 목표
수동 엑셀 작업 제거
반복 업무 자동화
실행 이력 추적 가능
플랫폼 목표
Input
 ↓
Rule
 ↓
Processing
 ↓
Delivery
 ↓
History

모든 업무가 동일한 Runtime Lifecycle 위에서 동작한다.