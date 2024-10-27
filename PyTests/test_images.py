import sys
import os
import base64
import mimetypes
from PIL import Image
import io

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc/file_utils")

from general_utils import input_to_file
from image_utils import input_to_PIL, file_to_PIL, print_image

# tests decode_file_data


def test_decode_file_data():
    # decode file data
    input_data = get_input()

    # try decoding data with file extension
    file, file_extension = input_to_file(input_data, get_file_extension=True)

    # for coconut.jpg, file_extension should be ".jpg"
    assert file_extension == ".jpg"
    assert isinstance(file, io.BytesIO)

    # try decoding data without file extension
    file = input_to_file(input_data)
    assert isinstance(file, io.BytesIO)


def test_input_to_PIL():
    # convert file data to pillow image
    input_data = get_input()

    # try converting data and getting image type
    pillow = input_to_PIL(input_data)

    assert isinstance(pillow, Image.Image)

    # try converting data
    pillow2 = input_to_PIL(input_data)
    assert isinstance(pillow2, Image.Image)


def test_file_to_PIL():
    # convert file data to pillow image
    input_data = get_input()
    file = input_to_file(input_data)
    pillow = file_to_PIL(file)
    assert isinstance(pillow, Image.Image)


def test_print_image():
    # convert file data to pillow image
    input_data = get_input()
    pillow = input_to_PIL(input_data)

    # making sure print_image returns a string that starts with "<img src="
    displayHTML = print_image(pillow)
    assert displayHTML.startswith("<img src=")
    assert displayHTML.endswith(">")

    # making sure print_image returns a string that starts with "<img src=" and "<a href="
    displayHTML, downloadHTML = print_image(
        pillow, download=True)

    assert displayHTML.startswith("<img src=")
    assert displayHTML.endswith(">")

    assert downloadHTML.startswith("<a href=")
    assert downloadHTML.endswith(">")


# returns a base64 encoded image
def get_input():
    return getInputImg(os.path.join(THIS_DIR, "./test_files/coconut.jpg"))


# returns a base64 encoded image
def getInputImg(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    mime_type = get_mime_type(path)
    metadata_string = f"data:{mime_type};base64,"

    return metadata_string + encoded_string


# returns part of the image metadata
def get_mime_type(file_path):
    return mimetypes.guess_type(file_path)[0]
