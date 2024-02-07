import requests
import jwt
import time
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging


# Function to append values to a Google Sheet
def append_to_google_sheet(service_account_info, spreadsheet_id, values, range_name='Sheet1!A1', include_timestamp=True):
    """
    Appends values to a Google Sheet, optionally including a timestamp.

    Parameters:
        service_account_info (dict): The service account credentials.
        spreadsheet_id (str): The ID of the spreadsheet.
        values (list of lists): The data to append.
        range_name (str): The starting cell where appending begins.
        include_timestamp (bool): Whether to include a timestamp in each row.

    Returns:
        dict: The API response.
        The values will be appended to Google Sheet.

    Examples:
    >>> service_account_info = {...}
    >>> spreadsheet_id = '...'
    >>> values = [["name", 1811123, "correct"]]
    >>> append_to_google_sheet(service_account_info, spreadsheet_id, values)
    """
    # Helper function to get an access token
    def _get_access_token(service_account_info):
        iat = time.time()
        exp = iat + 3600  # Token valid for 1 hour
        # JWT payload
        payload = {
            'iss': service_account_info['client_email'],
            'scope': 'https://www.googleapis.com/auth/spreadsheets',
            'aud': 'https://oauth2.googleapis.com/token',
            'iat': iat,
            'exp': exp
        }
        # Generate JWT
        additional_headers = {'kid': service_account_info['private_key_id']}
        signed_jwt = jwt.encode(
            payload,
            service_account_info['private_key'],
            algorithm='RS256',
            headers=additional_headers
        )
        # Exchange JWT for access token
        params = {
            'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
            'assertion': signed_jwt
        }
        response = requests.post('https://oauth2.googleapis.com/token', data=params)
        response_data = response.json()
        return response_data['access_token']

    # Get an access token
    access_token = _get_access_token(service_account_info)

    if include_timestamp:
        current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        values = [row + [current_timestamp] for row in values]

    url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_name}:append?valueInputOption=RAW&insertDataOption=INSERT_ROWS'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    body = {'values': values}
    response = requests.post(url, headers=headers, json=body)
    return response.json()


def send_gmail(sender_email, receiver_email, subject, app_password, values):
    """
    Sends an email with provided values formatted in the message body.

    Parameters:
    - sender_email: Email address of the sender.
    - receiver_email: Email address of the receiver.
    - subject: Subject line of the email.
    - password: App-specific password for the sender's email account.
    - values: A list of tuples containing data to be included in the email body.

    Examples:
    >>> values = [
        ["John Doe", "123456", 10, 2, 5.00, "This is a test message."]
    ]
    >>> send_email("xxx@gmail.com", "xxx@ualberta.ca", "test", "xxxx xxxx xxxx xxxx", values)
    """
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    body = ""
    for value in values:
        body += ", ".join(str(v) for v in value) + "\n"

    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        logging.info("Email sent successfully!")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
