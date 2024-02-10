import base64


def string_to_file(
    text: str,
    filename: str = "myfile",
    download_text: str = "Download File",
) -> str:
    """
    >>> string_to_file(
        text: str,
        filename: str = "myfile",
        download_text: str = "Download File"
    ) -> str

    Generates a downloadable text file containing the given text and provides an HTML download link.

    Parameters
    ----------
    text : str
        The text to be included in the download file.
    filename : str, optional
        The name of the file to be downloaded. Defaults to "myfile".
    download_text : str, optional
        The text to be displayed as the download link. Defaults to "Download File".

    Returns
    -------
    str
        An HTML string representing the download link for the generated text file.

    Raises
    ------
    TypeError
        If the input text is not a string.

    Examples
    --------
    Default usage:
    >>> download_link = string_to_file("Hello World")
    >>> print(download_link)
    # This will print the HTML download link with default filename and download text.

    Custom Filename and Download Text:
    >>> download_link = string_to_file("Hello World", filename="mytextfile", download_text="Download File Here")
    >>> print(download_link)
    # This will print the HTML download link with a custom filename and download text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if filename.endswith(".txt"):
        filename = filename[:-4]

    # Encode to a text file
    encoded_text = base64.b64encode(text.encode()).decode()
    mime_type = "data:text/plain;base64,"
    encoded_file = mime_type + encoded_text

    return f"<a href='{encoded_file}' download='{filename}.txt'>{download_text}</a>"
