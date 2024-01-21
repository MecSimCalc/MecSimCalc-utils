import io
import base64
from typing import Union, Tuple

import matplotlib.pyplot as plt
import matplotlib.figure as figure


def print_plot(
    plot_obj: Union[plt.Axes, figure.Figure],
    width: int = 500,
    dpi: int = 100,
    download: bool = False,
    download_text: str = "Download Plot",
    download_file_name: str = "myplot",
) -> Union[str, Tuple[str, str]]:
    """
    >>> print_plot(
        plot_obj: Union[plt.Axes, figure.Figure],
        width: int = 500,
        dpi: int = 100,
        download: bool = False,
        download_text: str = "Download Plot",
        download_file_name: str = "myplot"
    ) -> Union[str, Tuple[str, str]]

    Converts a matplotlib plot into an HTML image tag and optionally provides a download link for the image.

    # Parameters

    plot_obj : Union[plt.Axes, figure.Figure]
        The matplotlib plot to be converted.
    width : int, optional
        The width of the image in pixels. (Defaults to 500)
    dpi : int, optional
        The DPI of the image. (Defaults to 100)
    download : bool, optional
        If set to True, a download link will be provided. (Defaults to False)
    download_text : str, optional
        The text to be displayed for the download link. (Defaults to "Download Plot")
    download_file_name : str, optional
        The name of the downloaded file. (Defaults to 'myplot')

    # Returns

    Union[str, Tuple[str, str]] :
        * `download | False` : str - Returns the HTML image as a string.
        * `download | True` : Tuple[str, str] - Returns the HTML image and the download link

    # Examples
    **Without Download Link**
    >>> fig, ax = plt.subplots()
    >>> ax.plot([1, 2, 3], [1, 2, 3])
    >>> plot = msc.print_plot(ax)
    >>> return {
        "plot": plot
    }

    **With Download Link and Custom Download Text**
    >>> fig, ax = plt.subplots()
    >>> ax.plot([1, 2, 3], [1, 2, 3])
    >>> plot, download_link = msc.print_plot(ax, download=True, download_text="Download My Plot")
    >>> return {
        "plot": plot,
        "download_link": download_link
    }
    """
    if isinstance(plot_obj, plt.Axes):
        plot_obj = plot_obj.get_figure()

    buffer = io.BytesIO()
    plot_obj.savefig(buffer, format="png", dpi=dpi)

    if hasattr(plot_obj, "close"):
        plot_obj.close()

    encoded_image = (
        f"data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode()}"
    )
    html_img = f"<img src='{encoded_image}' width='{width}'>"

    if not download:
        return html_img

    download_link = (
        f"<a href='{encoded_image}' "
        f"download='{download_file_name}.png'>{download_text}</a>"
    )
    return html_img, download_link
