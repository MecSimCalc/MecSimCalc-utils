import sys
import os

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc")

from text_utils import string_to_file


def test_string_to_file():
    # download text from url
    text = getText()
    text = string_to_file(text)
    assert text.startswith("<a href=")


def getText():
    return "This is some text."
