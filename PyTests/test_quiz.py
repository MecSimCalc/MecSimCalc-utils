import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc")

from quiz_utils import append_to_google_sheet, send_gmail


class TestAppendToGoogleSheet(unittest.TestCase):
    @patch("mecsimcalc.quiz_utils.requests")
    def test_append_to_google_sheet(self, mock_post):
        # mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": True}

        mock_post.return_value = mock_response

        # create test data
        service_account_info = {
            "type": "service_account",
            "project_id": "123-quiz",
            "private_key_id": "123",
            "private_key": "-----BEGIN PRIVATE KEY-----\n123\n-----END PRIVATE KEY-----\n",
            "client_email": "123@.com",
            "client_id": "123",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/xxx.com",
            "universe_domain": "googleapis.com",
        }
        spreadsheet_id = "dummy_spreadsheet_id"
        values = [["dummy_data"]]
        range_name = "Sheet1!A1"

        # execute the function
        response = append_to_google_sheet(
            service_account_info, spreadsheet_id, values, range_name, False
        )
        assert isinstance(response, dict)


class TestSendEmail(unittest.TestCase):
    @patch("mecsimcalc.quiz_utils.smtplib.SMTP_SSL")
    def test_send_email_success(self, mock_smtp_ssl):
        # Setup test data
        sender_email = "sender@example.com"
        receiver_email = "receiver@example.com"
        subject = "Test Subject"
        app_password = "app-specific-password"
        values = [("Data1", "Data2"), ("Data3", "Data4")]

        # Configure the mock SMTP server
        mock_server = MagicMock()
        mock_smtp_ssl.return_value.__enter__.return_value = mock_server

        # Execute the function
        res = send_gmail(sender_email, receiver_email, subject, app_password, values)

        # Assertions
        assert res == True
        mock_smtp_ssl.assert_called_once_with("smtp.gmail.com", 465)
        mock_server.login.assert_called_once_with(sender_email, app_password)
        mock_server.sendmail.assert_called_once()
        args, _ = mock_server.sendmail.call_args
        self.assertEqual(args[0], sender_email)
        self.assertEqual(args[1], receiver_email)

        # Check that the email body contains the expected values
        email_body = args[2]
        for value in values:
            self.assertIn(", ".join(value), email_body)

    @patch("mecsimcalc.quiz_utils.smtplib.SMTP_SSL")
    def test_send_email_failure(self, mock_smtp_ssl):
        # Setup test data with same parameters as success test
        sender_email = "sender@example.com"
        receiver_email = "receiver@example.com"
        subject = "Test Subject"
        app_password = "app-specific-password"
        values = [("Data1", "Data2"), ("Data3", "Data4")]

        # Configure the mock SMTP server to raise an exception
        mock_smtp_ssl.return_value.__enter__.side_effect = Exception("SMTP Error")

        # Execute the function
        res = send_gmail(sender_email, receiver_email, subject, app_password, values)

        # Assertions
        assert res == False
        mock_smtp_ssl.assert_called_once_with("smtp.gmail.com", 465)
