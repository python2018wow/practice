import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 輸入gmail信箱的資訊
gmail_user = 'gmail address'        # your gmail address
gmail_password = 'xxxxxxxxxxxx'     # your gmail password
body  = "This is send email testing"

def send_email(to_email_address, body):
    msg = MIMEMultipart()
    msg['Subject'] = 'Email Test with Python'
    msg['From'] = gmail_user
    msg['To'] = to_email_address        #receiver's email  ex: "abc@gmail.com"

    msg.attach(MIMEText(body, 'plain'))

    # 建立SMTP連線
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    # 登錄Gmail
    server.login(gmail_user, gmail_password)
    # 寄信
    server.send_message(msg)
    # 關閉連線
    server.quit()