# MecSimCalc File Utilities v0.2.1

This library is designed to provide a set of functions for handling and converting various types of data, such as base64 encoded data, Pandas DataFrames, and Pillow images.

- [GitHub Repository](https://github.com/MecSimCalc/MecSimCalc-utils)
- [PyPi Page](https://pypi.org/project/mecsimcalc/)

## General

### input_to_file

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/general_utils.py#L7C1-L66C1)

```python
input_to_file(input_file, metadata = False)
```

#### Description:

Converts a base64 encoded string into a file object and metadata

#### Arguments:

| Argument         | Type                | Description                                                |
| ---------------- | ------------------- | ---------------------------------------------------------- |
| **`input_file`** | **str**             | Base64 encoded string, prefixed with metadata              |
| **`metadata`**   | **bool** (optional) | Flag to return metadata with the file. (Defaults to False) |

#### Raises:

| Exception        | Description                                                                        |
| ---------------- | ---------------------------------------------------------------------------------- |
| **`ValueError`** | If the input string doesn't contain ';base64,' to separate metadata and file data. |

#### Returns:

| Return Type             | Description                                                              | Condition         |
| ----------------------- | ------------------------------------------------------------------------ | ----------------- |
| **`io.BytesIO`**        | The decoded file data (The thing you get when you open a file in Python) | metadata is False |
| **`(io.BytesIO, str)`** | The decoded file data and its metadata                                   | metadata is True  |

#### Example:

```python
import io
import mecsimcalc as msc

def main(inputs):
    input_file = inputs['file']
    file, metadata = msc.input_to_file(input_file, metadata=True)
    return {"file_type": type(file).__name__, "metadata": metadata}

# Expected output:
# {"file_type": "_io.BytesIO", "metadata": "data:image/jpeg;base64,"}
```

### metadata_to_filetype

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/general_utils.py#L68C1-L100C21)

```python
metadata_to_filetype(metadata):
```

#### Description:

Extracts the file type from the metadata

#### Arguments:

| Argument       | Type    | Description                                                                                   |
| -------------- | ------- | --------------------------------------------------------------------------------------------- |
| **`metadata`** | **str** | The metadata string in the form "Data:(MIME type);base64,"(returned from **`input_to_file`**) |

#### Returns:

| Return Type | Description                 |
| ----------- | --------------------------- |
| **`str`**   | The file type (e.g. "jpeg") |

#### Example:

```python
import mecsimcalc as msc

def main(inputs):
    input_file = inputs['file']
    file, metadata = msc.input_to_file(input_file, metadata=True)
    download_file_type = msc.metadata_to_filetype(metadata)
    return {"file_type": download_file_type}

# Expected output:
# {"file_type": "jpeg"}
```

## Text

### string_to_file

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/text_utils.py#L4C1-L63C85)

```python
string_to_file(
    text
    filename= "myfile",
    download_text = "Download File",
)
```

#### Description:

Generates a downloadable text file containing the given text

#### Arguments:

| Argument            | Type               | Description                                                              |
| ------------------- | ------------------ | ------------------------------------------------------------------------ |
| **`text`**          | **str**            | Text to be downloaded                                                    |
| **`filename`**      | **str** (optional) | Name of the download file. (Defaults to "myfile")                        |
| **`download_text`** | **str** (optional) | Text to be displayed as the download link. (Defaults to "Download File") |

#### Raises:

| Exception       | Description                        |
| --------------- | ---------------------------------- |
| **`TypeError`** | If the input text is not a string. |

#### Returns:

| Return Type | Description        |
| ----------- | ------------------ |
| **`str`**   | HTML download link |

#### Example:

#### Python

```python
import mecsimcalc as msc

def main(inputs):
    download_link = msc.string_to_file("Hello World!")
    return {"download": download_link}

# Expected output:
# {"download": "<a href='data:text/plain;base64,SGVsbG8gV29ybGQh' download='myfile.txt'>Download File</a>"}
```

#### Jinja2

```python
# outputs.downloadLink is the html download link generated by the function
{{ outputs.download }}
```

## Spreadsheets

### file_to_dataframe

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/spreadsheet_utils.py#L9C1-L50C14)

```python
file_to_dataframe(file_data):
```

#### Description:

Converts a base64 encoded file data into a pandas DataFrame

#### Arguments:

| Argument        | Type           | Description                                       |
| --------------- | -------------- | ------------------------------------------------- |
| **`file_data`** | **io.BytesIO** | Decoded file data (e.g. from **`input_to_file`**) |

#### Raises:

| Exception                   | Description                                                                                                 |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **`pd.errors.ParserError`** | If the file data cannot be converted to a DataFrame (i.e. file is not an Excel or CSV file or is corrupted) |

#### Returns:

| Return Type        | Description                      |
| ------------------ | -------------------------------- |
| **`pd.DataFrame`** | DataFrame created from file data |

#### Example:

```python
import mecsimcalc as msc

def main(inputs):
    input_file = inputs['file']
    decoded_file = msc.input_to_file(input_file)
    df = msc.file_to_dataframe(decoded_file)
    return {"dataframe": df.to_dict()}

# Expected output:
# {"dataframe": {
# "A": {0: "a", 1: "d"},
# "B": {0: "b", 1: "e"},
# "C": {0: "c", 1: "f"}}}
```

### input_to_dataframe

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/spreadsheet_utils.py#L53C1-L92C44)

```python
input_to_dataframe(file):
```

#### Description:

Converts a base64 encoded file data into a pandas DataFrame

#### Arguments:

| Argument            | Type     | Description                                                          |
| ------------------- | -------- | -------------------------------------------------------------------- |
| **`input_file`**    | **str**  | Base64 encoded file data                                             |
| **`get_file_type`** | **bool** | If True, the function also returns the file type (Defaults to False) |

#### Returns:

| Return Type               | Description                                      | Condition              |
| ------------------------- | ------------------------------------------------ | ---------------------- |
| **`pd.DataFrame`**        | DataFrame created from file data                 | get_file_type is False |
| **`(pd.DataFrame, str)`** | Tuple containing the DataFrame and the file type | get_file_type is True  |

#### Example:

```python
import mecsimcalc as msc

def main(inputs):
    input_file = inputs['file']
    df, file_type = msc.input_to_dataframe(input_file, get_file_type=True)
    return {"dataframe": df.to_dict(), "file_type": file_type}

# Expected output:
# {"dataframe": {
# "A": {0: "a", 1: "d"},
# "B": {0: "b", 1: "e"},
# "C": {0: "c", 1: "f"}}, "file_type": "csv"}
```

### print_dataframe

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/spreadsheet_utils.py#L95C1-L186C39)

```python
print_dataframe(
    df,
    download = False,
    download_text = "Download Table",
    download_file_name = "mytable",
    download_file_type = "csv",
):
```

#### Description:

Creates an HTML table and a download link for a given DataFrame

#### Arguments:

| Argument                 | Type                | Description                                                              |
| ------------------------ | ------------------- | ------------------------------------------------------------------------ |
| **`df`**                 | **pd.DataFrame**    | DataFrame to be converted                                                |
| **`download`**           | **bool** (optional) | If True, function returns a download link (Defaults to False)            |
| **`download_text`**      | **str** (optional)  | Text to be displayed as the download link (Defaults to "Download Table") |
| **`download_file_name`** | **str** (optional)  | Name of file when downloaded (Defaults to "mytable")                     |
| **`download_file_type`** | **str** (optional)  | File type of downloaded file (Defaults to "csv")                         |

#### Returns:

| Return Type           | Description                      | Condition         |
| --------------------- | -------------------------------- | ----------------- |
| **`str`**             | HTML table                       | download is False |
| **`Tuple[str, str]`** | (HTML table, HTML download link) | download is True  |

#### Example:

#### Python Code:

```python
import mecsimcalc as msc

def main(inputs):
    input_file = inputs['file']
    df = msc.input_to_dataframe(input_file)
    table, download = msc.print_dataframe(df, download=True, download_file_name="Table", download_text="Download My Table HERE!", download_file_type="xlsx")
    return {"table": table, "download": download}

# Expected output:
# {"table": "<table>...</table>",
# "download": "<a href='data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,...' download='Table.xlsx'>Download My Table HERE!</a>"}
```

#### Output using Jinja2 Template:

```python
# outputs.table is the HTML table
Displaying Table
{{ outputs.table }}

# outputs.download is the download link
Downloading Table
{{ outputs.download }}
```

## Tables

### table_to_dataframe

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/table_utils.py#L5C1-L45C1)

```python
table_to_dataframe(column_headers, rows):
```

#### Description:

Create a DataFrame from given rows and column headers

#### Arguments:

| Argument             | Type                | Description                                                                     |
| -------------------- | ------------------- | ------------------------------------------------------------------------------- |
| **`column_headers`** | **List[str]**       | List of column headers                                                          |
| **`rows`**           | **List[List[str]]** | List of rows to be converted into a DataFrame. Each column is a list of strings |

#### Returns:

| Return Type        | Description                             |
| ------------------ | --------------------------------------- |
| **`pd.DataFrame`** | DataFrame created from headers and rows |

#### Example:

```python
import mecsimcalc as msc

def main(inputs):
    column_headers = ["A", "B", "C"]
    rows = [["a", "b", "c"], ["d", "e", "f"]]
    df = msc.table_to_dataframe(column_headers, rows)
    return {"dataframe": df.to_dict()}

# Expected output:
# {"dataframe": {
# "A": {0: "a", 1: "d"},
# "B": {0: "b", 1: "e"},
# "C": {0: "c", 1: "f"}}}
```

### print_table

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/table_utils.py#L47C1-L80C58)

```python
print_table(column_headers, rows):
```

#### Description:

Creates an HTML table from given rows and column headers

#### Arguments:

| Argument             | Type                | Description                                                                  |
| -------------------- | ------------------- | ---------------------------------------------------------------------------- |
| **`column_headers`** | **List[str]**       | List of column headers                                                       |
| **`rows`**           | **List[List[str]]** | List of rows to be converted into a table. Each column is a list of strings  |
| **`index`**          | **bool** (optional) | Whether to use the first column as the DataFrame's index. (Defaults to True) |

#### Returns:

| Return Type | Description                              |
| ----------- | ---------------------------------------- |
| **`str`**   | HTML table created from rows and headers |

#### Example:

#### Python Code:

```python
column_headers = ["A", "B", "C"]
rows = [["a", "b", "c"], ["d", "e", "f"]]
table = print_table(column_headers, rows)
return {
        "table":table,
    }
```

#### Output using Jinja2 Template:

```python
# outputs.table is the HTML table
Displaying Table
{{ outputs.table }}
```

## Images

### file_to_PIL

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/image_utils.py#L23C1-L55C88)

```python
file_to_PIL(file):
```

#### Description:

Transforms a file into a Pillow Image object

#### Arguments:

| Argument   | Type    | Description                                     |
| ---------- | ------- | ----------------------------------------------- |
| **`file`** | **str** | Decoded file data (returned from input_to_file) |

#### Raises:

| Exception Type   | Description                             |
| ---------------- | --------------------------------------- |
| **`ValueError`** | If the file does not contain image data |

#### Returns:

| Return Type | Description         |
| ----------- | ------------------- |
| **`Image`** | Pillow Image object |

#### Example:

#### Python Code:

```python
import mecsimcalc as msc

def main(inputs):
    input_file = inputs['file']
    decoded_file = msc.input_to_file(input_file)
    image = msc.file_to_PIL(decoded_file)
    return {"image": image}

# Expected output:
# {"image": <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=...>}
```

#### Output using Jinja2 Template:

```python
# outputs.image is the Pillow Image object
Displaying Image
{{ outputs.image }}
```

### input_to_PIL

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/image_utils.py#L58C1-L109C1)

```python
input_to_PIL(input_file, get_file_type=False):
```

#### Description:

Converts a base64 encoded file data into a pillow image

#### Arguments:

| Argument            | Type     | Description                                                          |
| ------------------- | -------- | -------------------------------------------------------------------- |
| **`input_file`**    | **str**  | Base64 encoded file data                                             |
| **`get_file_type`** | **bool** | If True, the function also returns the file type (Defaults to False) |

#### Returns:

| Return Type                       | Description              | Condition              |
| --------------------------------- | ------------------------ | ---------------------- |
| **`PIL.Image.Image`**             | Pillow Image object      | get_file_type is False |
| **`Tuple[PIL.Image.Image, str]`** | (pillow image, metadata) | get_file_type is True  |

#### Example:

```python
import mecsimcalc as msc

def main(inputs):
    input_file = inputs['file']
    image, file_type = msc.input_to_PIL(input_file, get_file_type=True)
    return {"image": image, "file_type": file_type}

# Expected output:
# {"image": <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=...>, "file_type": "jpeg"}
```

### print_image

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/image_utils.py#L110C1-L209C36)

```python
print_image(
    image,
    width = 200,
    height = 200,
    original_size = False,
    download = False,
    download_text = "Download Image",
    download_file_name= "myimg",
    download_file_type = "png",
):
```

#### Description:

Transforms a Pillow image into an HTML image, with an optional download link

#### Arguments:

| Argument                 | Type                | Description                                                                        |
| ------------------------ | ------------------- | ---------------------------------------------------------------------------------- |
| **`image`**              | **PIL.Image.Image** | Pillow image                                                                       |
| **`width`**              | **int** (optional)  | Output width of the image in pixels (Defaults to 200)                              |
| **`height`**             | **int** (optional)  | Output height of the image in pixels (Defaults to 200)                             |
| **`original_size`**      | **bool** (optional) | If True, the HTML image will be displayed in its original size (Defaults to False) |
| **`download`**           | **bool** (optional) | If True, function returns a download link (Defaults to False)                      |
| **`download_text`**      | **str** (optional)  | The text to be displayed on the download link (Defaults to "Download Image")       |
| **`download_file_name`** | **str** (optional)  | The name of the image file when downloaded (Defaults to "myimg")                   |
| **`download_file_type`** | **str** (optional)  | The file type of the image when downloaded (Defaults to "png")                     |

#### Returns:

| Return Type           | Description                 | Condition         |
| --------------------- | --------------------------- | ----------------- |
| **`str`**             | HTML image                  | download is False |
| **`Tuple[str, str]`** | (HTML image, download link) | download is True  |

#### Example:

#### Python Code:

```python
import mecsimcalc as msc

def main(inputs):
    input_file = inputs['file']
    image, metadata = msc.input_to_PIL(input_file)
    html_image, download = msc.print_image(image, original_size=True, download=True, download_text="Download Image Here", download_file_name="myimage", download_file_type="jpeg")
    return {"image": html_image, "download": download}

# Expected output:
# {"image": "<img src='data:image/jpeg;base64,...' width='...' height='...'>",
# "download": "<a href='data:image/jpeg;base64,...' download='myimage.jpeg'>Download Image Here</a>"}
```

#### Output using Jinja2 Template:

```python
# outputs.image is the HTML image
Displaying Image
{{ outputs.image }}

# outputs.download is the download link
Downloading Image
{{ outputs.download }}
```

## Plots

### print_plot

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/plotting_utils.py#L15C1-L102C1)

```python
print_plot(
    plot_obj,
    width = 500,
    dpi= 100,
    download= False,
    download_text = "Download Plot",
    download_file_name = "myplot",
)
```

#### Description:

Converts a matplotlib.pyplot.axis or matplotlib.figure into an HTML image tag and optionally provides a download link for the image

#### Arguments:

| Argument                 | Type                | Description                                                                 |
| ------------------------ | ------------------- | --------------------------------------------------------------------------- |
| **`plot_obj`**           | **axes or figure**  | Matplotlib figure                                                           |
| **`width`**              | **int** (optional)  | Output width of the image in pixels (Defaults to 500)                       |
| **`dpi`**                | **int** (optional)  | Output dpi of the image in pixels (Defaults to 100)                         |
| **`download`**           | **bool** (optional) | If True, function returns a download link (Defaults to False)               |
| **`download_text`**      | **str** (optional)  | The text to be displayed on the download link (Defaults to "Download Plot") |
| **`download_file_name`** | **str** (optional)  | The name of the image file when downloaded (Defaults to "myplot")           |

#### Returns:

| Return Type           | Description                      | Condition         |
| --------------------- | -------------------------------- | ----------------- |
| **`str`**             | HTML image                       | download is False |
| **`Tuple[str, str]`** | (HTML image, HTML download link) | download is True  |

#### Example:

#### Python Code:

```python
import matplotlib.pyplot as plt
import numpy as np
import mecsimcalc as msc

def main(inputs):
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('A single plot')
    image, download = msc.print_plot(fig, width=500, dpi=100, download=True, download_text="Download Sin Function Plot", download_file_name="sin(x)")
    return {"image": image, "download": download}

# Expected output:
# {"image": "<img src='data:image/jpeg;base64,...' width='500' height='...'>",
#  "download": "<a href='data:image/jpeg;base64,...' download='sin(x).jpeg'>Download Sin Function Plot</a>"}
```

#### Output using Jinja2 Template:

```python
# outputs.image is the HTML image
Displaying Image
{{ outputs.image }}

# outputs.download is the download link
Downloading Image
{{ outputs.download }}
```

### print_animation

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/plotting_utils.py#L104C1-L156C63)

```python
print_animation(
    ani,
    fps = 30,
    save_dir = "/tmp/temp_animation.gif"):
```

#### Description:

Converts a matplotlib animation into an animated GIF. Returns an HTML image tag to display it in your app.

#### Arguments:

| Argument       | Type               | Description                                                                                                                             |
| -------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| **`ani`**      | **FuncAnimation**  | The matplotlib animation to be converted.                                                                                               |
| **`fps`**      | **int** (optional) | Frames per second for the animation. (Defaults to 30)                                                                                   |
| **`save_dir`** | **str** (optional) | The directory to temporarily save files. You can only write to the tmp directory in mecsimcalc. Defaults to `"/tmp/temp_animation.gif"` |

#### Returns:

| Return Type | Description                     |
| ----------- | ------------------------------- |
| **`str`**   | The HTML image tag as a string. |

#### Example:

```python
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import mecsimcalc as msc

def main(inputs):
    fig, ax = plt.subplots()
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    line, = ax.plot(x, y)
    def update(frame):
        line.set_ydata(np.sin(x + frame / 10))
        return line,
    ani = FuncAnimation(fig, update, frames=100)
    animation = msc.print_animation(ani)
    return {"animation": animation}

# Expected output:
# {"animation": "<img src='data:image/gif;base64,...'>"}
```

### animate_plot

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/plotting_utils.py#L159C1-L278C1)

```python
animate_plot(
    x,
    y,
    duration = 3,
    fps = 15,
    x_label = "x",
    y_label = "y",
    title = "y = f(x)",
    show_axes = True,
    follow_tip = False,
    save_dir = "/tmp/temp_animation.gif",
    follow_tip = False,
    hold_last_frame = 1.0,
)
```

#### Description:

Creates an animated plot from given x and y data and returns it as an HTML image tag.

#### Arguments:

| Argument              | Type                 | Description                                                                                                                             |
| --------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **`x`**               | **np.ndarray**       | The x-coordinates of the data points.                                                                                                   |
| **`y`**               | **np.ndarray**       | The y-coordinates of the data points.                                                                                                   |
| **`duration`**        | **float** (optional) | The duration of the animation in seconds. Defaults to `3`.                                                                              |
| **`fps`**             | **float** (optional) | Frames per second for the animation. Defaults to `15`.                                                                                  |
| **`x_label`**         | **str** (optional)   | The label for the x-axis. Defaults to `"x"`.                                                                                            |
| **`y_label`**         | **str** (optional)   | The label for the y-axis. Defaults to `"y"`.                                                                                            |
| **`title`**           | **str** (optional)   | Title of the plot. Defaults to `"y = f(x)"`.                                                                                            |
| **`show_axes`**       | **bool** (optional)  | Whether to show the x and y axes. Defaults to `True`.                                                                                   |
| **`follow_tip`**      | **bool** (optional)  | Whether to follow the tip of the line as it moves along the x-axis. Defaults to `False`.                                                |
| **`hold_last_frame`** | **float** (optional) | The duration to hold the last frame in seconds. Defaults to `1.0`.                                                                      |
| **`save_dir`**        | **str** (optional)   | The directory to temporarily save files. You can only write to the tmp directory in mecsimcalc. Defaults to `"/tmp/temp_animation.gif"` |

#### Returns:

| Return Type | Description                                      |
| ----------- | ------------------------------------------------ |
| **`str`**   | The HTML image tag containing the animated plot. |

#### Example:

```python
import numpy as np
import mecsimcalc as msc

def main(inputs):
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    animation_html = msc.animate_plot(x, y, duration=4, title="Sine Wave", show_axes=True)
    return {"animation": animation_html}

# Expected output:
# {"animation": "<img src='data:image/gif;base64,...'>"}
```

### plot_slider

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/plotting_utils.py#L280C1-L423C45)

```python
plot_slider(
    f_x,
    x_range,
    y_range = None,
    title = "",
    x_label = "x",
    y_label = "y",
    num_points = 250,
    initial_value = 1,
    step_size = 0.1,
    slider_range = (-10, 10),
):
```

#### Description:

Creates an interactive plot with a slider using Plotly, allowing the user to dynamically update the plot based on a parameter.

#### Arguments:

| Argument            | Type                                          | Description                                                                               |
| ------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **`f_x`**           | **Callable[[float, np.ndarray], np.ndarray]** | A function that takes a float and an array of x-values, and returns an array of y-values. |
| **`x_range`**       | **Tuple[float, float]**                       | A tuple defining the range of x-values (start, end) for the plot.                         |
| **`y_range`**       | **Tuple[float, float]** (optional)            | A tuple defining the range of y-values (start, end) for the plot. Defaults to `None`.     |
| **`title`**         | **str** (optional)                            | Title of the plot. Defaults to `""`.                                                      |
| **`x_label`**       | **str** (optional)                            | Label for the x-axis. Defaults to `"x"`.                                                  |
| **`y_label`**       | **str** (optional)                            | Label for the y-axis. Defaults to `"y"`.                                                  |
| **`num_points`**    | **int** (optional)                            | Number of points to plot (line resolution). Defaults to `250`.                            |
| **`initial_value`** | **float** (optional)                          | Initial value of the slider. Defaults to `1`.                                             |
| **`step_size`**     | **float** (optional)                          | Step size for the slider. Defaults to `0.1`.                                              |
| **`slider_range`**  | **Tuple[float, float]** (optional)            | Range for the slider values (start, end). Defaults to `(-10, 10)`.                        |

#### Returns:

| Return Type | Description                                             |
| ----------- | ------------------------------------------------------- |
| **`str`**   | The HTML string containing the Plotly interactive plot. |

#### Example:

```python
import mecsimcalc as msc

def parabola(a, x):
    return a * x ** 2

def main(inputs):
    plot_html = msc.plot_slider(parabola, x_range=(-10, 10), y_range=(-100, 100))
    return {"plot": plot_html}

# Expected output:
# The `plot_html` can be used in a web page to display the interactive plot.
```

## Quiz Toolkit

### append_to_google_sheet

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/quiz_utils.py#L11C1-L134C1)

```python
append_to_google_sheet(
    service_account_info = {...},
    spreadsheet_id = "123abc...",
    values = [["name", 12837, ...]],
    range_name = "Sheet1!A1",
    include_timestamp = True
)
```

#### Description:

This function appends given values to a specified Google Sheet and optionally includes a current timestamp with each entry. It transforms data into a Google Sheets document, facilitating dynamic data entry directly from your application.

#### Arguments:

| Argument                   | Type                | Description                                                                      |
| -------------------------- | ------------------- | -------------------------------------------------------------------------------- |
| **`service_account_info`** | **dict**            | The service account credentials used for Google Sheets API authentication.       |
| **`spreadsheet_id`**       | **str**             | The unique identifier of the target Google Spreadsheet.                          |
| **`values`**               | **list of lists**   | The data to append. Each list element represents a row of data.                  |
| **`range_name`**           | **str** (optional)  | The A1 notation of the range to start appending data. Defaults to `"Sheet1!A1"`. |
| **`include_timestamp`**    | **bool** (optional) | If True, appends the current timestamp to each row of data. Defaults to `True`.  |

#### Returns:

| Return Type | Description                                                                          |
| ----------- | ------------------------------------------------------------------------------------ |
| **`dict`**  | The response from the Google Sheets API, containing details of the append operation. |

#### Example:

#### Code step:

```python
import mecsimcalc as msc

def main(inputs):
    service_account_info = {
        # Your service account info here
    }
    spreadsheet_id = 'your_spreadsheet_id_here'
    values = [
        [inputs['input_1'], inputs['input_2'], inputs['input_3']],
    ]
    result = msc.append_to_google_sheet(service_account_info, spreadsheet_id, values)
    return {"result": result}

# Expected output:
# {"result": {"spreadsheetId": "your_spreadsheet_id_here",
#  "updatedRange": "Sheet1!A1:C1",
#  "updatedRows": 1, "updatedColumns": 3, "updatedCells": 3}}
```

### send_gmail

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.1/mecsimcalc/file_utils/quiz_utils.py#L136C1-L207C21)

```python
send_gmail(
    sender_email='sender@example.com',
    receiver_email='receiver@example.com',
    subject="Quiz",
    app_password = "xxxx xxxx xxxx xxxx",
    values = [
    ["name", "grade"]
    ]
)
```

#### Description:

This function sends an email with specified values formatted in the message body, utilizing a service account for authentication.

#### Arguments:

| Argument             | Type     | Description                                                                |
| -------------------- | -------- | -------------------------------------------------------------------------- |
| **`sender_email`**   | **str**  | The email address of the sender.                                           |
| **`receiver_email`** | **str**  | The email address of the receiver.                                         |
| **`subject`**        | **str**  | The subject line of the email.                                             |
| **`app_password`**   | **str**  | The app-specific password for the sender's email account.                  |
| **`values`**         | **list** | A list of lists. Each list contains data to be included in the email body. |

#### Returns:

| Return Type | Description                                                       |
| ----------- | ----------------------------------------------------------------- |
| **`bool`**  | Returns True if the email was sent successfully, otherwise False. |

#### Example Usage:

```python
import mecsimcalc as msc

def main(inputs):
    sender_email = 'sender@example.com'
    receiver_email = 'receiver@example.com'
    subject = 'Test Email'
    app_password = 'your_app_password_here'

    name = inputs['name']
    grade = inputs['grade']

    values = [
        [name, grade]
    ]

    result = msc.send_gmail(sender_email, receiver_email, subject, app_password, values)
    return {"result": result}

# Expected output:
# {"result": True}
```
