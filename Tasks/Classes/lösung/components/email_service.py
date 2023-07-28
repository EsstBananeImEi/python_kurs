from email.message import EmailMessage
from smtplib import SMTP_SSL


def create_email_message(mail_to: str, subject: str, content: str) -> EmailMessage:
    message = EmailMessage()
    message.set_content(content)
    message["Subject"] = subject
    message["To"] = mail_to
    return message


def send_email(
    smtp_server: str,
    port: int,
    from_address: str,
    password: str,
    to_address: str,
    subject: str,
    content: str,
) -> None:
    message = create_email_message(to_address, subject, content)  # type: ignore
    with SMTP_SSL(smtp_server, port) as server:  # type: ignore
        # server.login(from_address, password)
        # server.send_message(message, to_address)
        print(f"Email sent to {to_address}")
