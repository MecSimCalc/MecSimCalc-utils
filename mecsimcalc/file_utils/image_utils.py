import base64
import io
from typing import Union, Tuple
from mimetypes import guess_type

from PIL import Image

from mecsimcalc import input_to_file


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
    input_file: str, get_file_extension: bool = False
) -> Union[Image.Image, Tuple[Image.Image, str]]:
    """
    >>> input_to_PIL(
        input_file: str,
        get_file_extension: bool = False
    ) -> Union[Image.Image, Tuple[Image.Image, str]]

    Decodes a Base64 encoded string into a PIL Image object. Optionally, the file extension can also be returned.

    Parameters
    ----------
    input_file : str
        A Base64 encoded string containing image data.
    get_file_extension : bool, optional
        If set to True, the function also returns the file extension of the image. Defaults to `False`.

    Returns
    -------
    * `Union[PIL.Image.Image, Tuple[PIL.Image.Image, str]]` :
        * If `get_file_extension` is False, returns a PIL.Image.Image object created from the decoded file data.
        * If `get_file_extension` is True, returns a tuple containing the PIL.Image.Image object and a string representing the file extension.

    Examples
    --------
    **Without file extension**:

    >>> input_file = inputs["input_file"]
    >>> image = msc.input_to_PIL(input_file)
    (Image is now ready to be used with Pillow functions)

    **With file extension**:

    >>> input_file = inputs["input_file"]
    >>> image, file_extension = msc.input_to_PIL(input_file, get_file_extension=True)
    >>> print(file_extension)
    '.png'

    (image is now ready to be used with Pillow functions)
    """
    # Get file extension from metadata
    file_data = input_to_file(input_file)
    image = file_to_PIL(file_data)
    
    if get_file_extension:
        file_data, file_extension = input_to_file(input_file, get_file_extension=True)
        return image, file_extension
    
    return image


def print_image(
    image: Image.Image,
    width: int = 200,
    height: int = 200,
    original_size: bool = False,
    download: bool = False,
    download_text: str = "Download Image",
    download_file_name: str = "myimg",
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

    **With download link**:

    >>> input_file = inputs["input_file"]
    >>> image = msc.input_to_PIL(input_file)
    >>> html_image, download_link = msc.print_image(image, download=True)
    >>> return {
        "html_image": html_image,
        "download_link": download_link
    }

    """
    # get metadata (file type) from image
    dummy_filename = f"dummy.{image.format.lower()}"
    mime_type, _ = guess_type(dummy_filename)
    metadata = f"data:{mime_type};base64,"
    
    if download:
        # Preserve original image if downloading
        download_image = image.copy()

        # Get download image data (Full Resolution Image)
        download_buffer = io.BytesIO()
        download_image.save(download_buffer, format=image.format)
        encoded_data = f"{metadata}{base64.b64encode(download_buffer.getvalue()).decode()}"

    if not original_size:
        image.thumbnail((width, height))

    # Convert image to image tag (HTML)
    buffer = io.BytesIO()
    image.save(buffer, format=image.format)
    encoded_display_data = (metadata + base64.b64encode(buffer.getvalue()).decode())
    image_tag = f"<img src='{encoded_display_data}'>"


    if not download:
        return image_tag
    download_link = f"<a href='{encoded_data}' download='{download_file_name}.{(image.format or 'png').lower()}'>{download_text}</a>"
    return image_tag, download_link
