import smtplib

from email.message import EmailMessage

from app.utils.logger import logger

from app.config.settings import (
    SMTP_HOST,
    SMTP_PORT,
    SMTP_USER,
    SMTP_PASSWORD,
    TO_EMAIL
)


def send_mail(
    subject,
    body,
    attachment_path=None
):

    try:

        logger.info(
            f"메일 발송 시작 : {TO_EMAIL}"
        )

        msg = EmailMessage()

        msg["Subject"] = subject
        msg["From"] = SMTP_USER
        msg["To"] = TO_EMAIL

        msg.set_content(body)

        if attachment_path:

            logger.info(
                f"첨부파일 추가 : {attachment_path}"
            )

            with open(
                attachment_path,
                "rb"
            ) as f:

                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="zip",
                    filename="result.zip"
                )

        with smtplib.SMTP(
            SMTP_HOST,
            SMTP_PORT
        ) as server:

            server.starttls()

            server.login(
                SMTP_USER,
                SMTP_PASSWORD
            )

            server.send_message(msg)

        logger.info(
            "메일 발송 완료"
        )

        return True

    except Exception as e:

        logger.exception(
            f"메일 발송 실패 : {e}"
        )

        return False
