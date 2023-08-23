import io
import base64
import pandas as pd
from typing import Union, Tuple

from mecsimcalc import input_to_file, metadata_to_filetype


def file_to_dataframe(file: io.BytesIO) -> pd.DataFrame:
    """
    >>> file_to_dataframe(file: io.BytesIO) -> pd.DataFrame

    Converts a base64 encoded file data into a pandas DataFrame.

    # Parameters

    file : io.BytesIO
        Decoded file data.

    # Raises

    * `pd.errors.ParserError` :
        If the file type is not supported.

    # Returns
    * `pd.DataFrame` :
        Returns a DataFrame created from the file data.

    # Example
    >>> input_file = inputs["input_file"]
    >>> file = msc.input_to_file(input_file)
    >>> df = msc.file_to_dataframe(file)
    >>> print(df)
        A  B  C
     0  1  2  3
     1  4  5  6
    """

    # try to read the file as a CSV, if that fails try to read it as an Excel file
    try:
        df = pd.read_csv(file)
    except Exception:
        try:
            df = pd.read_excel(file, engine="openpyxl")
        except Exception as e:
            raise pd.errors.ParserError("File Type Not Supported") from e

    return df


def input_to_dataframe(
    input_file: str, get_file_type: bool = False
) -> Union[pd.DataFrame, Tuple[pd.DataFrame, str]]:
    """
    >>> input_to_dataframe(input_file: str, get_file_type: bool = False) -> Union[pd.DataFrame, Tuple[pd.DataFrame, str]]

    Converts a base64 encoded file data into a pandas DataFrame.

    # Parameters

    input_file : str
        The base64 encoded file data.
    get_file_type : bool, optional
        If True, the function also returns the file type (Defaults to False).

    # Returns

    * `Union[pd.DataFrame, Tuple[pd.DataFrame, str]]` :
        * `get_file_type | False` : pd.DataFrame - Returns a DataFrame created from the file data.
        * `get_file_type | True` : Tuple[pd.DataFrame, str] - Returns a tuple containing the DataFrame and the file type.

    # Example
    >>> input_file = inputs["input_file"]
    >>> df = msc.input_to_dataframe(input_file)
    >>> print(df)
       A  B  C
    0  1  2  3
    1  4  5  6

    """

    file_data, metadata = input_to_file(input_file, metadata=True)

    if get_file_type:
        return file_to_dataframe(file_data), metadata_to_filetype(metadata)
    else:
        return file_to_dataframe(file_data)


def print_dataframe(
    df: pd.DataFrame,
    download: bool = False,
    download_text: str = "Download Table",
    download_file_name: str = "mytable",
    download_file_type: str = "csv",
) -> Union[str, Tuple[str, str]]:
    """
    >>> print_dataframe(
        df: pd.DataFrame,
        download: bool = False,
        download_text: str = "Download Table",
        download_file_name: str = "mytable",
        download_file_type: str = "csv"
    ) -> Union[str, Tuple[str, str]]

    Creates an HTML table from a pandas DataFrame and optionally provides a download link for the table.

    # Parameters

    df : pd.DataFrame
        The DataFrame to be converted.
    download : bool, optional
        If True, the function also provides a download link. (Defaults to False)
    download_text : str, optional
        The text to be displayed on the download link. (Defaults to "Download Table")
    download_file_name : str, optional
        The name of the downloaded file. (Defaults to "myfile")
    download_file_type : str, optional
        The file type of the download file. xlsx or csv (Defaults to "csv")

    # Returns

    * `Union[str, Tuple[str, str]]` :
        * `download | False` : str - Returns the HTML table as a string.
        * `download | True` : Tuple[str, str] - Returns a tuple containing the HTML table and the HTML download link as strings.

    # Examples
    ** Without Download Link **
    >>> input_file = inputs["input_file"]
    >>> df = msc.input_to_dataframe(input_file)
    >>> table = msc.print_dataframe(df)
    >>> return {
        "table": table
    }

    ** With Download Link for excel file **
    >>> input_file = inputs["input_file"]
    >>> df = msc.input_to_dataframe(input_file)
    >>> table, download_link = msc.print_dataframe(df, download=True, download_file_type="xlsx")
    >>> return {
        "table": table,
        "download_link": download_link
    }
    """
    # if download is False, return the table as a string
    if not download:
        return df.to_html()

    # convert the download file type to lowercase
    download_file_type = download_file_type.lower()

    # create a buffer to store the file data
    buf = io.BytesIO()

    # if the file type is an alias of excel, convert the DataFrame to an excel file
    if download_file_type in {
        "excel",
        "xlsx",
        "xls",
        "xlsm",
        "xlsb",
        "odf",
        "ods",
        "odt",
    }:
        # convert the DataFrame to an excel file
        df.to_excel(buf, index=False, engine="openpyxl")
        buf.seek(0)

        encoded_data = (
            "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,"
            + base64.b64encode(buf.read()).decode()
        )

    # if the file type does not match an alias of excel, convert the DataFrame to a csv file
    else:
        csv_str = df.to_csv(index=False)
        buf.write(csv_str.encode())
        buf.seek(0)

        encoded_data = "data:text/csv;base64," + base64.b64encode(buf.read()).decode()

    # create the download link
    download_link = f"<a href='{encoded_data}' download='{download_file_name}.{download_file_type}'>{download_text}</a>"

    return df.to_html(), download_link
