import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class mail_service:

    def mail_service(subject, body):
    
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        from_address = "luca.kmrth@gmail.com"
        to_address = "lucakamrath.arbeit@gmail.com"

        message = MIMEMultipart()
        message['From'] = from_address
        message['To'] = to_address
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        def send_email(message):
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(from_address, 'krmrkyvnkqtfrpbg')
                server.send_message(message)

        print('Email sent successfully!')
