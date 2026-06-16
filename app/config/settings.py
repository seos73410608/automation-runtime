import os


# 프로젝트 루트
BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

# 입출력 경로
INPUT_DIR = os.path.join(BASE_DIR, "input")

OUTPUT_DIR = os.path.join(BASE_DIR, "output")

TEMP_DIR = os.path.join(
    OUTPUT_DIR,
    "temp"
)

# 결과 ZIP 파일명
RESULT_ZIP_NAME = "result.zip"

# Job 이름
JOB_REPAIR_PENDING = "RepairPending"

JOB_INBOUND_MISSING = "InboundMissing"

JOB_SETTLEMENT_MISSING = "SettlementMissing"

JOB_TC_SCAN = "TcScan"