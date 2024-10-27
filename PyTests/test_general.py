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

def test_input_to_file():
  img = readImg()
  xml = readXML()
  csv = readCSV()
  html = readHTML()
  mp4 = readMP4()
  
  # convert encoded file to usable file
  fileImg, file_extensionImg = input_to_file(img, get_file_extension = True)
  fileXML, file_extensionXML = input_to_file(xml, get_file_extension = True)
  fileCSV, file_extensionCSV = input_to_file(csv, get_file_extension = True)
  fileHTML, file_extensionHTML = input_to_file(html, get_file_extension = True)
  fileMP4, file_extensionMP4 = input_to_file(mp4, get_file_extension = True)
  
  assert file_extensionImg == ".jpg"
  assert isinstance(fileImg, io.BytesIO)
  assert file_extensionXML == ".xlsx"
  assert isinstance(fileXML, io.BytesIO)
  assert file_extensionCSV == ".csv"
  assert isinstance(fileCSV, io.BytesIO)
  assert file_extensionHTML == ".html"
  assert isinstance(fileHTML, io.BytesIO)
  assert file_extensionMP4 == ".mp4"
  assert isinstance(fileMP4, io.BytesIO)


# returns part of the image metadata
def get_mime_type(file_path):
  return mimetypes.guess_type(file_path)[0]
def readImg():
    return getInput(os.path.join(THIS_DIR, "./test_files/coconut.jpg"))
def readXML():
    return getInput(os.path.join(THIS_DIR, "./test_files/xlsxFile.xlsx"), xlsx=True)
def readCSV():
    return getInput(os.path.join(THIS_DIR, "./test_files/csvFile.csv"))
def readHTML():
    return getInput(os.path.join(THIS_DIR, "./test_files/htmlFile.html"))
def readMP4():
    return getInput(os.path.join(THIS_DIR, "./test_files/mp4File.mp4"))

def getInput(path, xlsx=False):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    mime_type = get_mime_type(path)
    metadata_string = f"data:{mime_type};base64,"

    if xlsx:
        metadata_string = "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,"

    return metadata_string + encoded_string
    
  