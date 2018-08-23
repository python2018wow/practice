import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 輸入gmail信箱的資訊
gmail_user = 'python2018wow@gmail.com'
gmail_password = '!Q2w3e4r5t' # your gmail password
body  = "This is an order email"

def send_email(to_email_address, body):
    msg = MIMEMultipart()
    msg['Subject'] = 'Email Test with Python'
    msg['From'] = gmail_user
    msg['To'] = to_email_address

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

if __name__ == '__main__':
    send_email("python2018wow@gmail.com", "This is test email")
    

