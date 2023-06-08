import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Erstellt E-Mail und sendet sie and die E-Mail
class mail_service:

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    from_address = "luca.kmrth@gmail.com"
    to_address = "lucakamrath.arbeit@gmail.com"

    def mail_service(subject, body):

        message = MIMEMultipart()
        message['From'] = mail_service.from_address
        message['To'] = mail_service.to_address
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        mail_service.send_email(message)

        print('Email sent successfully!')

    def send_email(message):
            with smtplib.SMTP(mail_service.smtp_server, mail_service.smtp_port) as server:
                server.starttls()
                server.login(mail_service.from_address, 'krmrkyvnkqtfrpbg')
                server.send_message(message)