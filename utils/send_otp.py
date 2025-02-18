from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from core.config import settings



def send_otp_from_email(recipient, subject, body):
    print("email send function")
    # senderEmail = os.getenv("SENDER_EMAIL")
    senderEmail = settings.EMAIL_HOST_USER 


    password = settings.EMAIL_HOST_PASSWORD
    receiverEmail = recipient
    # Body = body
    message = body
    msg = MIMEMultipart()
    msg['From'] = senderEmail
    msg['To'] = receiverEmail
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(senderEmail, password)
        text = msg.as_string()
        server.sendmail(senderEmail, receiverEmail, text)
        print("email send to ", receiverEmail)
        return True
    except Exception as e:
        return False