import os

from dotenv import load_dotenv

# ==========================================
# ENV
# ==========================================

load_dotenv()

# ==========================================
# PROJECT PATH
# ==========================================

BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

INPUT_DIR = os.path.join(
    BASE_DIR,
    "input"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "output"
)

UPLOAD_DIR = os.path.join(
    BASE_DIR,
    "uploads"
)

# ==========================================
# RESULT FILE
# ==========================================

RESULT_ZIP_NAME = "result.zip"

# ==========================================
# JOB NAME
# ==========================================

JOB_REPAIR_PENDING = "repair_pending"

JOB_INBOUND_MISSING = "InboundMissing"

JOB_SETTLEMENT_MISSING = "SettlementMissing"

JOB_TC_SCAN = "TcScan"

# ==========================================
# MAIL
# ==========================================

SMTP_HOST = os.getenv("SMTP_HOST")

SMTP_PORT = int(
    os.getenv(
        "SMTP_PORT",
        "587"
    )
)

SMTP_USER = os.getenv("SMTP_USER")

SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

TO_EMAIL = os.getenv("TO_EMAIL")

# ==========================================
# DATABASE
# ==========================================
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
