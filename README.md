# automation-runtime

업무 자동화 Runtime 플랫폼

현재는 수선업체 미처리건(Repair Pending) 자동화를 지원하며,
향후 원전미입고, 정산누락, TC 미스캔 등의 업무 자동화를 동일 Runtime에서 수행할 수 있도록 설계되었습니다.

---

## 현재 지원 기능

### Repair Pending Automation

AS접수현황 엑셀 파일을 분석하여

- 수선업체1 + 업체완료일1 미입력
- 수선업체2 + 업체완료일2 미입력

조건의 미처리 건을 추출하고,

- 업체별 그룹핑
- 업체별 엑셀 생성
- ZIP 파일 생성

을 자동 수행합니다.

---

## 프로젝트 구조

```text
app/

├── config
│   └── settings.py

├── excel
│   ├── excel_reader.py
│   └── excel_exporter.py

├── jobs
│   └── repair_pending_job.py

├── models
│   └── job_result.py

├── rules
│   └── repair_pending_rule.py

├── utils
│   └── file_utils.py

run.py
```

---

## 실행 방법

### 1. 입력 파일 준비

```text
input/
└── A_S접수현황.xls
```

---

### 2. 실행

```text
실행하기.bat
```

또는

```bash
python run.py
```

---

## 실행 결과

예시

```text
==================================
JOB          : RepairPending
TOTAL ROWS   : 3549
FILTERED     : 107
VENDORS      : 23
OUTPUT FILES : 23
ZIP FILE     : output/result.zip
SUCCESS      : True
MESSAGE      : 처리 완료
==================================
```

---

## 출력 파일

```text
output/

├── temp/
│   ├── 업체A.xlsx
│   ├── 업체B.xlsx
│   └── ...

└── result.zip
```

---

## 버전 이력

### v0.1.0

- Repair Pending MVP
- 업체별 엑셀 생성
- ZIP 생성

### v0.2.0

- Runtime 구조 분리
- Rule / Excel / Job 모듈화

### v0.2.1

- JobResult 도입
- Runtime Settings 분리
- Header 자동 인식 개선
- 입력 파일 표준화
- 예외 처리 강화

---

## 향후 계획

### v0.3.0

- FastAPI 웹 UI
- 파일 업로드
- 실행 결과 화면
- ZIP 다운로드

### v0.4.0

- MariaDB Job History

### v0.5.0

- Mail Sender

### v0.6.0

- Scheduler

### v0.7.0+

- 원전미입고 자동화
- 정산누락 자동화
- TC 미스캔 자동화

---

## 목표

업무별로 다른 엑셀 매크로를 만드는 것이 아니라

```text
Excel Input
↓
Rule Engine
↓
Grouping
↓
Excel Export
↓
ZIP Export
```

공통 Runtime 위에서 다양한 업무 자동화를 수행하는 플랫폼으로 확장한다.