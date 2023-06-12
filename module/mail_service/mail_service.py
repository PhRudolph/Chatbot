import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Creating and sending an E-mail to a service E-Mail for updating the chatbot
class mail_service:

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    from_address = "luca.kmrth@gmail.com"
    to_address = "lucakamrath.arbeit@gmail.com"

#Writing Mail and call send-email methode
    def mail_service(subject, body):

        message = MIMEMultipart()
        message['From'] = mail_service.from_address
        message['To'] = mail_service.to_address
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        mail_service.send_email(message)

        print('Email sent successfully!')

#Login into mail programm and sending mail
    def send_email(message):
            with smtplib.SMTP(mail_service.smtp_server, mail_service.smtp_port) as server:
                server.starttls()
                server.login(mail_service.from_address, 'krmrkyvnkqtfrpbg')
                server.send_message(message)