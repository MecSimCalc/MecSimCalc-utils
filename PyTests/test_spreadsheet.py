import sys
import os
import base64
import mimetypes
import io
import pandas as pd

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

# add parent directory to path so we can import mecsimcalc
sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc")

from general_utils import input_to_file, metadata_to_filetype
from spreadsheet_utils import input_to_dataframe, file_to_dataframe, print_dataframe


def test_input_to_file():
    # Simulates Mecsimcalc's input files (base64 encoded strings)
    inputCSV = get_csv()
    inputXLSX = get_xlsx()

    # convert encoded file to usable file
    fileCSV, metadataCSV = input_to_file(inputCSV, metadata=True)
    fileXLSX, metadataXLSX = input_to_file(inputXLSX, metadata=True)

    assert metadataCSV == "data:text/csv;base64,"
    assert (
        metadataXLSX
        == "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,"
    )
    assert isinstance(fileCSV, io.BytesIO)
    assert isinstance(fileXLSX, io.BytesIO)

    # try converting metadata to file type
    fileType = metadata_to_filetype(metadataCSV)
    assert fileType == "csv"

    fileType = metadata_to_filetype(metadataXLSX)
    assert fileType == "xlsx"

    # try decoding data without metadata
    file = input_to_file(inputCSV)
    assert isinstance(file, io.BytesIO)

    file = input_to_file(inputXLSX)
    assert isinstance(file, io.BytesIO)


# def test_file_to_dataframe():
def test_file_to_dataframe():
    # get input data
    inputCSV = get_csv()
    inputXLSX = get_xlsx()

    # decode file data
    fileCSV = input_to_file(inputCSV)
    fileXLSX = input_to_file(inputXLSX)

    # convert file data to dataframe
    dfCSV = file_to_dataframe(fileCSV)
    dfXLSX = file_to_dataframe(fileXLSX)

    # make sure dataframe is a pandas dataframe
    assert isinstance(dfCSV, pd.DataFrame)
    assert isinstance(dfXLSX, pd.DataFrame)


def test_input_to_dataframe():
    # get input data
    inputCSV = get_csv()
    inputXLSX = get_xlsx()

    # convert input data to dataframe
    dfCSV = input_to_dataframe(inputCSV)
    dfXLSX = input_to_dataframe(inputXLSX)

    # make sure dataframe is a pandas dataframe
    assert isinstance(dfCSV, pd.DataFrame)
    assert isinstance(dfXLSX, pd.DataFrame)


def test_print_dataframe():
    # get input data
    inputCSV = get_csv()
    inputXLSX = get_xlsx()

    # convert input data to dataframe
    dfCSV = input_to_dataframe(inputCSV)
    dfXLSX = input_to_dataframe(inputXLSX)

    # make sure dataframe is a pandas dataframe
    assert isinstance(dfCSV, pd.DataFrame)
    assert isinstance(dfXLSX, pd.DataFrame)

    # print dataframe
    dfHTMLcsv = print_dataframe(dfCSV)
    dfHTMLxlsx = print_dataframe(dfXLSX)

    # make sure html is a string
    assert dfHTMLcsv.startswith("<table")
    assert dfHTMLxlsx.startswith("<table")

    # convert input data to dataframe with metadata
    dfCSV, fileTypeCSV = input_to_dataframe(inputCSV, get_file_type=True)
    dfXLSX, fileTypeXLSX = input_to_dataframe(inputXLSX, get_file_type=True)

    # make sure dataframe is a pandas dataframe and file type is correct
    assert fileTypeCSV == "csv"
    assert fileTypeXLSX == "xlsx"
    assert isinstance(dfCSV, pd.DataFrame)
    assert isinstance(dfXLSX, pd.DataFrame)

    # make sure dataframe is a pandas dataframe
    assert isinstance(dfCSV, pd.DataFrame)
    assert isinstance(dfXLSX, pd.DataFrame)

    # print dataframe
    dfHTMLcsv, downloadHTMLcsv = print_dataframe(
        dfCSV, download=True, download_file_type=fileTypeCSV
    )
    dfHTMLxlsx, downloadHTMLxlsx = print_dataframe(
        dfXLSX, download=True, download_file_type=fileTypeXLSX
    )

    # make sure dfHTML is actually html
    assert dfHTMLcsv.startswith("<table")
    assert dfHTMLxlsx.startswith("<table")

    # make sure downloadHTML is actually html
    assert downloadHTMLcsv.startswith("<a href=")
    assert downloadHTMLxlsx.startswith("<a href=")


# returns a base64 encoded image
def get_csv():
    return getSpreadsheetInput(os.path.join(THIS_DIR, "./test_files/csvFile.csv"))


def get_xlsx():
    return getSpreadsheetInput(os.path.join(THIS_DIR, "./test_files/xlsxFile.xlsx"), xlsx=True)


# returns a base64 encoded image
def getSpreadsheetInput(path, xlsx=False):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    mime_type = get_mime_type(path)
    metadata_string = f"data:{mime_type};base64,"

    if xlsx:
        metadata_string = "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,"

    return metadata_string + encoded_string


# returns part of the spreadsheet's metadata
def get_mime_type(file_path):
    mime_type, encoding = mimetypes.guess_type(file_path)
    return mime_type
