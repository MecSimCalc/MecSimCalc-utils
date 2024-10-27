import io
import base64
import re
from typing import Union, Tuple
from mimetypes import guess_type, guess_extension

def input_to_file(
    input_file: str, file_extension: bool = False
) -> Union[io.BytesIO, Tuple[io.BytesIO, str]]:
    """
    >>> input_to_file(
        input_file: str,
        file_extension: bool = False
    ) -> Union[io.BytesIO, Tuple[io.BytesIO, str]]

    Transforms a Base64 encoded string into a file object. Optionally, returns the file extension.

    Parameters
    ----------
    input_file : str
        A Base64 encoded string prefixed with file_extension.
    file_extension : bool, optional
        If set to True, the function also returns the file_extension. Defaults to `False`.

    Returns
    -------
    * `Union[io.BytesIO, Tuple[io.BytesIO, str]]` :
        * If `file_extension` is False, returns an `io.BytesIO` object containing the decoded file data.
        * If `file_extension` is True, returns a tuple containing the `io.BytesIO` object and a `string` representing the file_extension.

    Raises
    ------
    * `ValueError` :
        If the input string does not contain ";base64,", which is required to separate file_extension from the file data.

    Notes
    -----
    The file object is an open file and can be used with Python file functions like open_file.read()

    Examples
    --------
    **Without file extension**:
    >>> input_file = inputs["input_file"]
    >>> open_file = msc.input_to_file(input_file)

    (file is now ready to be used with Python file functions) (e.g., file.read())

    **With file extension**:
    >>> input_file = inputs["input_file"]
    >>> open_file, file_extension = msc.input_to_file(input_file, file_extension=True)
    """
    # Check if the input string contains ';base64,' which is required to separate metadata and file data
    if ";base64," not in input_file:
        raise ValueError("Invalid input: must contain ';base64,'")
    
    # Split metadata and data
    meta, data = input_file.split(";base64,")
    file_data = io.BytesIO(base64.b64decode(data))
    meta_data = f"{meta};base64,"
    
    extension = guess_extension(guess_type(meta_data)[0])
    extension = '.jpg' if extension=='.jpe' else extension

    return (file_data, extension) if file_extension else file_data

@DeprecationWarning
def metadata_to_filetype(metadata: str) -> str:
    """
    >>> metadata_to_filetype(metadata: str) -> str

    Extracts the file type from the metadata string.

    Parameters
    ----------
    metadata : str
        A metadata string typically in the form `Data:<MIME type>;base64,`

    Returns
    -------
    * `str` :
        The extracted file type (e.g., 'csv'). For a Microsoft Excel file, it returns 'xlsx'.

    Examples
    --------
    >>> input_file = inputs["input_file"]
    >>> open_file, metadata = msc.input_to_file(input_file, metadata=True)
    >>> file_type = msc.metadata_to_filetype(metadata)
    >>> print(file_type)
    'jpeg'
    """
    # Extract mime type from metadata
    match = re.search(r"/(.+);base64,", metadata)
    file_type = match[1] if match else ""

    # Convert the file type to a more common format
    if file_type == "vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        file_type = "xlsx"

    return file_type
