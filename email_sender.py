import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, app_password):
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, app_password)
            server.send_message(msg)
        print("✅ 이메일 전송 성공!")
    except Exception as e:
        print("❌ 이메일 전송 실패:", e)
