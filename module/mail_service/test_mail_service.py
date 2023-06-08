import unittest
from unittest.mock import patch
from mail_service import mail_service
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Testet den Mail Service mit unittest
class MailServiceTests(unittest.TestCase):

    def test_send_email(self):
        with patch('smtplib.SMTP') as mock_smtp:
            mail_service.smtp_server = "test_server"
            mail_service.smtp_port = 1234
            mail_service.from_address = "test@example.com"
            mail_service.send_email(MIMEMultipart())

            mock_smtp.assert_called_once_with("test_server", 1234)

    @patch('builtins.print')
    @patch('mail_service.mail_service.send_email')
    def test_mail_service(self, mock_send_email, mock_print):
        mail_service.from_address = "from@example.com"
        mail_service.to_address = "to@example.com"
        subject = "Test Subject"
        body = "Test Body"

        mail_service.mail_service(subject, body)

        mock_send_email.assert_called_once()
        mock_print.assert_called_once_with('Email sent successfully!')

if __name__ == '__main__':
    unittest.main()
