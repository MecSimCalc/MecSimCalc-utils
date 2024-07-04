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

    Generates a downloadable text file containing the given text.

    Parameters
    ----------
    text : str
        Text to be downloaded
    filename : str, optional
        Name of the download file. Defaults to `"myfile"`.
    download_text : str, optional
        Text to be displayed as the download link. Defaults to `"Download File"`.

    Returns
    -------
    * `str` :
        HTML download link

    Raises
    ------
    * `TypeError` :
        If the input text is not a string.

    Examples
    --------
    **Default usage**:
    >>> download_link = msc.string_to_file("Hello World")
    >>> return {"download_link": download_link}

    **Custom Filename and Download Text**:
    >>> download_link = msc.string_to_file(
        "Hello World",
        filename="mytextfile",
        download_text="Download File Here"
    )
    >>> return {"download_link": download_link}
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
