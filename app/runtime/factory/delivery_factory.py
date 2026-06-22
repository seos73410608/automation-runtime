from app.mail.mail_sender import send_mail


class EmailSender:

    def execute(
        self,
        subject,
        body,
        attachment_path
    ):
        send_mail(
            subject=subject,
            body=body,
            attachment_path=attachment_path
        )


class DeliveryFactory:

    @staticmethod
    def get(sender_name):

        if sender_name == "EmailSender":
            return EmailSender()

        raise ValueError(
            f"Unknown sender: {sender_name}"
        )