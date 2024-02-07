import sys
import os

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc")

from quiz_utils import append_to_google_sheet, send_gmail

def test_append_to_google_sheet():
    # get input data
    service_account_info = {
        ...
    }

    spreadsheet_id = '...'

    values = [
        ["test util", 1811123, 341, 113, round(26.1, 2), "correct"]
    ]

    res = append_to_google_sheet(service_account_info, spreadsheet_id, values)
    print(res)


def test_send_gmail():
    values = [
    ["test", "123456", 10, 2, 5.00, "This is a test message."]
]
    send_gmail("..", "..", "test", "...", values)


