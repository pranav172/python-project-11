import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = "pbjg bmgr uitp jnhr"
username = "rloveumom@gmail.com"

def sendMail():
    email_content = "Don't forget to take a break!"
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg["To"] = "rpranav1820@gmail.com"
    msg["From"] = username
    msg["Subject"] = "Take a Break!"
    msg.attach(MIMEText(email_content, "plain"))

    s.send_message(msg)
    del msg
    s.quit()

def printMe():
    print("💙 Sending Reminder")
    sendMail()
schedule.every(1).hours.do(printMe)

while True:
    schedule.run_pending()
    time.sleep(1)