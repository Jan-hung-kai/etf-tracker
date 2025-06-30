import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def send_email():
    sender = "hiltonsaul0502@gmail.com"
    recipient = "hiltonsaul0502@gmail.com"
    password = os.environ.get("GMAIL_APP_PASSWORD")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"ETF 每日追蹤報告 - {datetime.date.today()}"
    msg["From"] = sender
    msg["To"] = recipient

    html = """    <html>
      <body>
        <h2>ETF 追蹤報告</h2>
        <p>這是每日自動寄送的報告。</p>
        <p><a href="https://vnvgt3m3wpgxxao8.streamlit.app">點此查看完整儀表板</a></p>
      </body>
    </html>
    """
    part = MIMEText(html, "html")
    msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

if __name__ == "__main__":
    send_email()
