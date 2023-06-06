import unittest
from unittest.mock import patch, MagicMock
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

from mail_service import mail_service

class MailServiceTests(unittest.TestCase):

    @patch('smtplib.SMTP')
    def test_mail_service(self, mock_smtp):
        subject = "This is the subject."
        body = "This is the email message."

        mock_smtp_instance = MagicMock(spec=mail_service)
        mock_smtp_instance.starttls = MagicMock(spec=mail_service)
        mock_smtp_instance.login = MagicMock(spec=mail_service)
        mock_smtp_instance.send_message = MagicMock()

        # Assert that SMTP was instantiated with the correct parameters
        mock_smtp.assert_called_once_with("smtp.gmail.com", 587)

        # Assert that starttls() was called
        mock_smtp_instance.starttls.assert_called_once()

        # Assert that login() was called with the correct parameters
        mock_smtp_instance.login.assert_called_once_with("luca.kmrth@gmail.com", 'krmrkyvnkqtfrpbg')

        # Assert that send_message() was called with the correct parameters
        expected_message = MIMEMultipart()
        expected_message['From'] = "luca.kmrth@gmail.com"
        expected_message['To'] = "lucakamrath.arbeit@gmail.com"
        expected_message['Subject'] = subject
        expected_message.attach(MIMEText(body, 'plain'))
        mock_smtp_instance.send_message.assert_called_once_with(expected_message)

    @patch('smtplib.SMTP')
    def test_mail_service_exception(self, mock_smtp):
        subject = "This is the subject."
        body = "This is the email message."

        # Simulate an exception during the email sending process
        mock_smtp_instance = mock_smtp.return_value
        mock_smtp_instance.__enter__.side_effect = Exception("An error occurred")

        # Assert that an exception is raised
        with self.assertRaises(Exception):
            mail_service(subject, body)

if __name__ == '__main__':
    unittest.main()
