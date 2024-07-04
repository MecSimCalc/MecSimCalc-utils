import requests
import jwt
import time
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging


def append_to_google_sheet(
    service_account_info: dict,
    spreadsheet_id: str,
    values: list,
    range_name: str = "Sheet1!A1",
    include_timestamp: bool = True,
) -> dict:
    """
    >>> append_to_google_sheet(
        service_account_info: dict,
        spreadsheet_id: str,
        values: list,
        range_name: str = 'Sheet1!A1',
        include_timestamp: bool = True
    ) -> dict

    Appends values to Google Sheet, with the option to include a timestamp in each row appended.

    Parameters
    ----------
    service_account_info : dict
        The credentials of the service account, including at least 'client_email', 'private_key',
        and 'private_key_id' fields. This is used to authenticate and interact with the Google Sheets API.
    spreadsheet_id : str
        The unique identifier for the Google Sheets document to which data will be appended.
    values : list of list
        The data to be appended, organized as a list of rows, with each row being a list of values.
    range_name : str, optional
        The A1 notation of the starting cell where appending will begin. Defaults to `"Sheet1!A1"`.
    include_timestamp : bool, optional
        A flag indicating whether to append a timestamp to each row of data. Defaults to `True`.
        The timestamp format is `YYYY-MM-DD HH:MM:SS`.

    Returns
    -------
    * `dict` :

        A dictionary representing the response from the Google Sheets API. This typically includes
        information about the update, such as the range updated and the number of cells affected.

    Raises
    ------
    * `Exception` :
        If an error occurs while obtaining the access token or appending the data to the sheet.

    Examples
    --------
    >>> service_account_info = {
        "client_email": "your_service_account_email",
        "private_key": "your_private_key",
        "private_key_id": "your_private_key_id",
    }
    >>> spreadsheet_id = 'your_spreadsheet_id'
    >>> values = [["Example Name", 42, "Example Data"]]
    >>> msc.append_to_google_sheet(service_account_info, spreadsheet_id, values)
    >>> # Output
    >>> {
        "updates": {
            "spreadsheetId": "your_spreadsheet_id",
            "updatedRange": "Sheet1!A1:C2",
            "updatedRows": 1,
            "updatedColumns": 3,
            "updatedCells": 3,
        }
    }
    """

    # Helper function to get an access token
    def _get_access_token(service_account_info: dict):
        try:
            iat = time.time()
            exp = iat + 3600  # Token valid for 1 hour
            # JWT payload
            payload = {
                "iss": service_account_info["client_email"],
                "scope": "https://www.googleapis.com/auth/spreadsheets",
                "aud": "https://oauth2.googleapis.com/token",
                "iat": iat,
                "exp": exp,
            }
            # Generate JWT
            additional_headers = {"kid": service_account_info["private_key_id"]}
            signed_jwt = jwt.encode(
                payload,
                service_account_info["private_key"],
                algorithm="RS256",
                headers=additional_headers,
            )
            # Exchange JWT for access token
            params = {
                "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
                "assertion": signed_jwt,
            }
            response = requests.post("https://oauth2.googleapis.com/token", data=params)
            response.raise_for_status()  # Raises HTTPError, if one occurred
            response_data = response.json()
            return response_data["access_token"]
        except Exception as e:
            print(f"Error getting access token: {e}")
            return None

    # Get an access token
    access_token = _get_access_token(service_account_info)
    if not access_token:
        return {"error": "Failed to get access token"}

    if include_timestamp:
        current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        values = [row + [current_timestamp] for row in values]

    try:
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_name}:append?valueInputOption=RAW&insertDataOption=INSERT_ROWS"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        body = {"values": values}
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()  # Raises HTTPError, if one occurred
        return response.json()
    except Exception as e:
        print(f"Error appending to Google Sheet: {e}")
        return {"error": "Failed to append to Google Sheet"}


def send_gmail(
    sender_email: str,
    receiver_email: str,
    subject: str,
    app_password: str,
    values: list,
) -> bool:
    """
    >>> send_gmail(
        sender_email: str,
        receiver_email: str,
        subject: str,
        app_password: str,
        values: list
    ) -> bool

    Sends an email from a Gmail account to a specified recipient with a list of values formatted in the message body.

    Parameters
    ----------
    sender_email : str
        The email address of the sender. This should be a valid Gmail address.
    receiver_email : str
        The email address of the recipient. Can be any valid email address.
    subject : str
        The subject line of the email.
    app_password : str
        The app-specific password generated for the sender's Gmail account. This is required for authentication when
        using Gmail's SMTP server for sending emails programmatically.
    values : list of list
        A list of lists, where each inner list contains data (strings or numbers) that will be formatted and included in
        the email body. Each inner list is converted to a comma-separated string and added to the email body on a new line.

    Returns
    -------
    * `bool` :
        Returns True if the email was sent successfully, otherwise False.

    Examples
    --------
    >>> values = [["John Doe", "123456", 10, 2, 5.00, "This is a test message."]]
    >>> msc.send_gmail(
        "sender@example.com",
        "receiver@example.com",
        "Test Email",
        "your_app_password",
        values,
    )
    >>> # Output
    >>> True
    """

    # Initialize email message
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Construct the email body
    body = "\n".join(", ".join(str(v) for v in value) for value in values)
    message.attach(MIMEText(body, "plain"))

    try:
        # Send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        logging.info("Email sent successfully!")
        return True
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        return False
