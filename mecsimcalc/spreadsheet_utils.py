import io
import base64
import pandas as pd
from typing import Union, Tuple

from mecsimcalc import input_to_file, metadata_to_filetype


def file_to_dataframe(file: io.BytesIO) -> pd.DataFrame:
    """
    >>> file_to_dataframe(file: io.BytesIO) -> pd.DataFrame

    Converts base64 encoded file data into a pandas DataFrame.

    Parameters
    ----------
    file : io.BytesIO
        Decoded file data as an io.BytesIO object.

    Returns
    -------
    pd.DataFrame
        A DataFrame created from the decoded file data.

    Raises
    ------
    pd.errors.ParserError
        If the file type is not supported or cannot be converted into a DataFrame.

    Examples
    --------
    >>> input_file = "data:text/csv;base64,dGVzdCx0ZXN0Mix0ZXN0Mw=="
    >>> file = input_to_file(input_file)
    >>> df = file_to_dataframe(file)
    >>> print(df)
       A  B  C
    0  1  2  3
    1  4  5  6
    """

    # get dataframe from file data (try csv first, then excel)
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
    >>> input_to_dataframe(
        input_file: str,
        get_file_type: bool = False
    ) -> Union[pd.DataFrame, Tuple[pd.DataFrame, str]]

    Converts base64 encoded file data into a pandas DataFrame.

    Parameters
    ----------
    input_file : str
        The base64 encoded file data.
    get_file_type : bool, optional
        If True, the function also returns the file type. Defaults to False.

    Returns
    -------
    Union[pd.DataFrame, Tuple[pd.DataFrame, str]]
        If `get_file_type` is False, returns a `pd.DataFrame` created from the file data.
        If `get_file_type` is True, returns a tuple containing the `pd.DataFrame` and the file type.

    Examples
    --------
    >>> input_file = "data:text/csv;base64,dGVzdCx0ZXN0Mix0ZXN0Mw=="
    >>> df = input_to_dataframe(input_file)
    >>> print(df)
       A  B  C
    0  1  2  3
    1  4  5  6
    """
    # converts input file into a dataframe
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

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to be converted into an HTML table.
    download : bool, optional
        If True, the function also provides a download link for the table. Defaults to False.
    download_text : str, optional
        The text to be displayed on the download link. Defaults to "Download Table".
    download_file_name : str, optional
        The name of the file to be downloaded. Defaults to "myfile".
    download_file_type : str, optional
        The file type of the download file. Can be "xlsx" or "csv". Defaults to "csv".

    Returns
    -------
    Union[str, Tuple[str, str]]
        If `download` is False, returns the HTML table as a string.
        If `download` is True, returns a tuple containing the HTML table as a string and the HTML download link as a string.

    Examples
    --------
    Without Download Link:
    >>> df = pd.DataFrame({'A': [1, 4], 'B': [2, 5], 'C': [3, 6]})
    >>> table = print_dataframe(df)
    >>> print(table)
    # Outputs the HTML table as a string.

    With Download Link for an Excel file:
    >>> df = pd.DataFrame({'A': [1, 4], 'B': [2, 5], 'C': [3, 6]})
    >>> table, download_link = print_dataframe(df, download=True, download_file_type="xlsx")
    >>> print(table)
    >>> print(download_link)
    # Outputs the HTML table as a string and the HTML download link for the Excel file.
    """
    if not download:
        return df.to_html()

    # -------- Creating Downloadable File --------#

    buf = io.BytesIO()
    download_file_type = download_file_type.lower()

    # excel
    if download_file_type in {
        "excel",
        "xlsx",
        "xls",
        "xlsm",
        "xlsb",
        "odf",
        "ods",
        "odt",
        "vnd.openxmlformats-officedocument.spreadsheetml.sheet",  # MIME type
    }:
        df.to_excel(buf, index=False, engine="openpyxl")
        encoded_file = (
            "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,"
            + base64.b64encode(buf.getvalue()).decode()
        )
    # csv
    else:
        csv_str = df.to_csv(index=False)
        buf.write(csv_str.encode())

        encoded_file = (
            "data:text/csv;base64," + base64.b64encode(buf.getvalue()).decode()
        )

    download_link = f"<a href='{encoded_file}' download='{download_file_name}.{download_file_type}'>{download_text}</a>"
    return df.to_html(), download_link
