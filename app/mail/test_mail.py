from app.mail.mail_sender import send_mail

if __name__ == "__main__":

    send_mail(
        subject="Automation Runtime SMTP Test",
        body="SMTP 연결 테스트입니다.",
        attachment_path=None
    )
