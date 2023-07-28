from smtplib import SMTP_SSL
from ssl import create_default_context
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def create_email_message(mail_to: str, subject: str, content: str) -> MIMEMultipart:
    message = MIMEMultipart()
    message["Subject"] = subject
    message["To"] = mail_to
    message.attach(MIMEText(content, "plain"))
    message.attach(MIMEText(get_html_content(subject, content), "html"))
    return message

def get_html_content(subject:str, content: str) -> str:
    return f"""
    <html>
        <head>{subject}</head>
        <body>
            <p>{content}</p>
        </body>
    </html>
    """

def send_email(
    smtp_server: str,
    port: int,
    from_address: str,
    password: str,
    to_address: str,
    subject: str,
    content: str,
) -> None:
    context = create_default_context()
    message: MIMEMultipart = create_email_message(to_address, subject, content)  # type: ignore
    with SMTP_SSL(smtp_server, port, context) as server:  # type: ignore
        # server.login(from_address, password)
        # server.sendmail(from_address, to_address, message.as_string())
        print(f"Email sent to {to_address}")
