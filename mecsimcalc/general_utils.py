import io
import base64
import re
from typing import Union, Tuple


def input_to_file(
    input_file: str, metadata: bool = False
) -> Union[io.BytesIO, Tuple[io.BytesIO, str]]:
    """
    >>> input_to_file(
        input_file: str,
        metadata: bool = False
    ) -> Union[io.BytesIO, Tuple[io.BytesIO, str]]

    Transforms a Base64 encoded string into a file object. Optionally, the file metadata can also be returned.

    # Parameters
    input_file : str
        A Base64 encoded string prefixed with metadata.
    metadata : bool, optional
        If set to True, the function also returns the metadata. Default is False.

    # Raises
    * `ValueError`:
        If the input string does not contain ';base64,' which is required to separate metadata and file data.

    # Returns
    * `Union[io.BytesIO, Tuple[io.BytesIO, str]]` :
        * `metadata | False` : io.BytesIO - Returns a file object containing the file data.
        * `metadata | True` : Tuple[io.BytesIO, str] - Returns a tuple containing the file object and the metadata.

    **Note:** The file object is open and can be used with Python file functions (e.g., file.read()).


    # Examples
    **Without metadata**
    >>> input_file = inputs["input_file"]
    >>> file = msc.input_to_file(input_file)

    (file is now ready to be used with Python file functions) (e.g., file.read())

    **With metadata**
    >>> input_file = inputs["input_file"]
    >>> file, metadata = msc.input_to_file(input_file, metadata=True)

    (metadata holds information about the file, such as the file type)
    """

    # Check if the input string contains ';base64,' which is required to separate metadata and file data
    if ";base64," not in input_file:
        raise ValueError("Invalid input: must contain ';base64,'")

    meta, data = input_file.split(";base64,")
    file_data = io.BytesIO(base64.b64decode(data))
    meta_data = f"{meta};base64,"

    return (file_data, meta_data) if metadata else file_data


def metadata_to_filetype(metadata: str) -> str:
    """
    >>> metadata_to_filetype(metadata: str) -> str

    Extracts the file type from the metadata string.

    # Parameters
    metadata : str
        A metadata string typically in the form "Data:<MIME type>;base64,"

    # Returns
    * `str` :
        The extracted file type (e.g., 'csv'). For a Microsoft Excel file, it returns 'xlsx'.

    # Example
    >>> input_file = inputs["input_file"]
    >>> file, metadata = msc.input_to_file(input_file, metadata=True)
    >>> file_type = msc.metadata_to_filetype(metadata)
    >>> print(file_type)
    jpeg
    """
    # Extract mime type from metadata
    match = re.search(r"/(.+);base64,", metadata)
    file_type = match[1] if match else ""

    # Convert the file type to a more common format
    if file_type == "vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        file_type = "xlsx"

    return file_type
