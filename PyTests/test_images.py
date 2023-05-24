import sys
import os
import pytest
import base64
import mimetypes
from PIL import Image
import io

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc")

from general_utils import decode_file_data, metadata_to_filetype
from image_utils import input_to_PIL, file_to_PIL, print_img

# tests decode_file_data


def test_decode_file_data():
    # decode file data
    inputData = get_input()

    # try decoding data with metadata
    file, metadata = decode_file_data(inputData, metadata=True)

    # for coconut.jpg, metadata should be "data:image/jpeg;base64,"
    assert metadata == "data:image/jpeg;base64,"
    assert isinstance(file, io.BytesIO)

    # try converting metadata to file type
    fileType = metadata_to_filetype(metadata)
    assert fileType == "jpeg"

    # try decoding data without metadata
    file = decode_file_data(inputData)
    assert isinstance(file, io.BytesIO)


def test_input_to_PIL():
    # convert file data to pillow image
    inputData = get_input()

    # try converting data and getting image type
    pillow, fileType = input_to_PIL(inputData, getFileType=True)

    assert isinstance(pillow, Image.Image)
    assert fileType == "jpeg"

    # try converting data without getting image type
    pillow2 = input_to_PIL(inputData)
    assert isinstance(pillow2, Image.Image)


def test_file_to_PIL():
    # convert file data to pillow image
    inputData = get_input()
    file = decode_file_data(inputData)
    pillow = file_to_PIL(file)
    assert isinstance(pillow, Image.Image)


def test_print_img():
    # convert file data to pillow image
    inputData = get_input()
    pillow, fileType = input_to_PIL(inputData, getFileType=True)

    # making sure print_img returns a string that starts with "<img src="
    displayHTML = print_img(pillow)
    assert displayHTML.startswith("<img src=")

    # making sure print_img returns a string that starts with "<img src=" and "<a href="
    displayHTML, downloadHTML = print_img(pillow, fileType=fileType, download=True)
    assert displayHTML.startswith("<img src=")
    assert downloadHTML.startswith("<a href=")


# returns a base64 encoded image
def get_input():
    return getInputImg("./coconut.jpg")


# returns a base64 encoded image
def getInputImg(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

    mime_type = get_mime_type(path)
    metadata_string = f"data:{mime_type};base64,"

    return metadata_string + encoded_string


# returns part of the image metadata
def get_mime_type(file_path):
    mime_type, encoding = mimetypes.guess_type(file_path)
    return mime_type
