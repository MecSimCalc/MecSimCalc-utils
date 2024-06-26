import base64
import io
from typing import Union, Tuple

from PIL import Image

from mecsimcalc import input_to_file, metadata_to_filetype

# Define a dictionary for file type conversions
file_type_mappings = {
    "jpg": "jpeg",
    "jpeg": "jpeg",
    "tif": "tiff",
    "tiff": "tiff",
    "ico": "x-icon",
    "x-icon": "x-icon",
    "svg": "svg+xml",
    "svg+xml": "svg+xml",
    "png": "png",
}


def file_to_PIL(file: io.BytesIO) -> Image.Image:
    """
    >>> file_to_PIL(file: io.BytesIO) -> Image.Image

    Converts a binary file object into a PIL Image object.

    Parameters
    ----------
    file : io.BytesIO
        A binary file object containing image data.

    Returns
    ----------
    * `PIL.Image.Image` :
        An image object created from the file data.

    Raises
    --------
    * `ValueError` :
        If the file object does not contain valid image data.

    Examples
    ----------
    >>> input_file = inputs["input_file"]
    >>> file = msc.input_to_file(input_file)
    >>> image = msc.file_to_PIL(file)

    (image is now ready to be used with Pillow functions)
    """
    try:
        return Image.open(file)
    except IOError as e:
        raise ValueError("Invalid file object. It does not contain image data.") from e


def input_to_PIL(
    input_file: str, get_file_type: bool = False
) -> Union[Image.Image, Tuple[Image.Image, str]]:
    """
    >>> input_to_PIL(
        input_file: str,
        get_file_type: bool = False
    ) -> Union[Image.Image, Tuple[Image.Image, str]]

    Decodes a Base64 encoded string into a PIL Image object. Optionally, the file type can also be returned.

    Parameters
    ----------
    input_file : str
        A Base64 encoded string containing image data.
    get_file_type : bool, optional
        If set to True, the function also returns the file type of the image. Defaults to `False`.

    Returns
    -------
    * `Union[PIL.Image.Image, Tuple[PIL.Image.Image, str]]` :
        * If `get_file_type` is False, returns a PIL.Image.Image object created from the decoded file data.
        * If `get_file_type` is True, returns a tuple containing the PIL.Image.Image object and a string representing the file type.

    Examples
    --------
    **Without file type**:

    >>> input_file = inputs["input_file"]
    >>> image = msc.input_to_PIL(input_file)
    (Image is now ready to be used with Pillow functions)

    **With file type**:

    >>> input_file = inputs["input_file"]
    >>> image, file_type = msc.input_to_PIL(input_file, get_file_type=True)
    >>> print(file_type)
    'png'

    (image is now ready to be used with Pillow functions)
    """
    file_data, metadata = input_to_file(input_file, metadata=True)

    image = file_to_PIL(file_data)

    if get_file_type:
        file_type = metadata_to_filetype(metadata)
        return image, file_type

    return image


def print_image(
    image: Image.Image,
    width: int = 200,
    height: int = 200,
    original_size: bool = False,
    download: bool = False,
    download_text: str = "Download Image",
    download_file_name: str = "myimg",
    download_file_type: str = "png",
) -> Union[str, Tuple[str, str]]:
    """
    >>> print_image(
        image: Image.Image,
        width: int = 200,
        height: int = 200,
        original_size: bool = False,
        download: bool = False,
        download_text: str = "Download Image",
        download_file_name: str = "myimg",
        download_file_type: str = "png"
    ) -> Union[str, Tuple[str, str]]

    Transforms a Pillow image into an HTML image, with an optional download link.

    Parameters
    ----------
    image : PIL.Image.Image
        A Pillow image object.
    width : int, optional
        The width for the displayed image, in pixels. Defaults to `200`.
    height : int, optional
        The height for the displayed image, in pixels. Defaults to `200`.
    original_size : bool, optional
        If True, the image will retain its original size. Defaults to `False`.
    download : bool, optional
        If True, a download link will be provided below the image. Defaults to `False`.
    download_text : str, optional
        The text for the download link. Defaults to `"Download Image"`.
    download_file_name : str, optional
        The name for the downloaded file, without file extension. Defaults to `"myimg"`.
    download_file_type : str, optional
        The file type for the downloaded file. Defaults to `"png"`.

    Returns
    -------
    * `Union[str, Tuple[str, str]]` :
        * If `download` is False, returns an HTML string containing the image.
        * If `download` is True, returns a tuple containing the HTML string of the image and the HTML string of the download link.

    Examples
    --------
    **Without download link, with original size**:

    >>> input_file = inputs["input_file"]
    >>> image = msc.input_to_PIL(input_file)
    >>> html_image = msc.print_image(image, original_size=True)
    >>> return {
        "html_image": html_image
    }

    **With download link and specified file type**:

    >>> input_file = inputs["input_file"]
    >>> image, file_type = msc.input_to_PIL(input_file, get_file_type=True)
    >>> html_image, download_link = msc.print_image(image, download=True, download_file_type = file_type)
    >>> return {
        "html_image": html_image,
        "download_link": download_link
    }

    """
    # preserve original image for download
    display_image = image.copy()

    mime_type = file_type_mappings.get(
        download_file_type.lower().replace(".", ""), "png"
    )
    metadata = f"data:image/{mime_type};base64,"

    if not original_size:
        display_image.thumbnail((width, height))

    # Get download image data (Full Resolution Image)
    buffer = io.BytesIO()
    image.save(buffer, format=image.format)
    encoded_data = metadata + base64.b64encode(buffer.getvalue()).decode()

    # Get display image data (Custom Resolution)
    display_buffer = io.BytesIO()
    display_image.save(display_buffer, format=image.format)
    encoded_display_data = (
        metadata + base64.b64encode(display_buffer.getvalue()).decode()
    )

    image_tag = f"<img src='{encoded_display_data}'>"
    if not download:
        return image_tag

    download_link = f"<a href='{encoded_data}' download='{download_file_name}.{image.format}'>{download_text}</a>"
    return image_tag, download_link
