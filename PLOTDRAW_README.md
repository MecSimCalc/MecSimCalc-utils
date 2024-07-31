<div style={{ margin: '1em 0' }}>
  <label htmlFor="version-select" style={{ fontWeight: 'bold', marginRight: '10px' }}>Select Version:</label>
  <select id="version-select" onChange={(e) => window.location.href = e.target.value}>
    <option value="">Latest Release (v0.1.9)</option>
    <!-- Add more options as needed -->
  </select>
</div>

# Plot Draw

This library is designed to provide a set of functions for drawing various types of plots, arrows, segments, and shapes using Matplotlib. These functions allow for customized plotting and annotation of graphical elements.

## General

### draw_arrow

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L7C1-L84C78)

```python
draw_arrow(
    start: Union[tuple, list],
    end: Union[tuple, list],
    thickness: int = 5,
    color: str = "black",
    text: str = None,
    text_distance: float = 0.5,
    head_width: float = 0.08,
    head_length: float = 0.08,
    fontsize: int = 12
) -> None
```

#### Description:

Draws an arrow between two points on a plot.

#### Arguments:

| Argument            | Type                 | Description                                                                              |
| ------------------- | -------------------- | ---------------------------------------------------------------------------------------- |
| **`start`**         | **tuple or list**    | The starting point of the arrow (x, y).                                                  |
| **`end`**           | **tuple or list**    | The ending point of the arrow (x, y).                                                    |
| **`thickness`**     | **int**              | The thickness of the arrow line. (Default is 5)                                          |
| **`color`**         | **str**              | The color of the arrow. (Default is 'black')                                             |
| **`text`**          | **str** (optional)   | Text to display near the arrow. (Default is None)                                        |
| **`text_distance`** | **float** (optional) | Distance factor from the arrow end point where the text will be placed. (Default is 0.5) |
| **`head_width`**    | **float** (optional) | Width of the arrow head. (Default is 0.08)                                               |
| **`head_length`**   | **float** (optional) | Length of the arrow head. (Default is 0.08)                                              |
| **`fontsize`**      | **int** (optional)   | Font size of the text. (Default is 12)                                                   |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_arrow((0, 0), (1, 1), thickness=2, color='red', text='Arrow', text_distance=0.1, head_width=0.1, head_length=0.1, fontsize=10)
    plt.xlim(-1, 2)
    plt.ylim(-1, 2)
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a red arrow from (0, 0) to (1, 1) with the label "Arrow".

```

### calculate_midpoint

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L87C1-L121C1)

```python
calculate_midpoint(
    coord1: tuple,
    coord2: tuple
) -> tuple
```

#### Description:

Calculates the midpoint between two coordinates.

#### Arguments:

| Argument     | Type      | Description                   |
| ------------ | --------- | ----------------------------- |
| **`coord1`** | **tuple** | The first coordinate (x, y).  |
| **`coord2`** | **tuple** | The second coordinate (x, y). |

#### Returns:

| Return Type          | Description                                         |
| -------------------- | --------------------------------------------------- |
| **`(float, float)`** | A tuple containing the coordinates of the midpoint. |

#### Example:

```python
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    midpoint = plot_draw.calculate_midpoint((0, 0), (2, 2))
    return {"midpoint": midpoint}

# Expected output: {"midpoint": (1.0, 1.0)}

```

### draw_arc_circumference

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L123C1-L167C22)

```python
draw_arc_circumference(
    radius: float,
    initial_angle: float,
    final_angle: float,
    center: tuple = (0, 0)
) -> None
```

#### Description:

Draws an arc of a circumference with a given radius between two angles.

#### Arguments:

| Argument            | Type      | Description                                          |
| ------------------- | --------- | ---------------------------------------------------- |
| **`radius`**        | **float** | The radius of the circumference.                     |
| **`initial_angle`** | **float** | The starting angle of the arc in radians.            |
| **`final_angle`**   | **float** | The ending angle of the arc in radians.              |
| **`center`**        | **tuple** | The center of the circumference. (Default is (0, 0)) |

#### Example:

```python
import matplotlib.pyplot as plt
import numpy as np
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_arc_circumference(5, 0, np.pi/2)
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a quarter-circle arc with a radius of 5.


```

### create_blank_image

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L170C1-L213C14)

```python
create_blank_image(
    width: int = 1000,
    height: int = 1000
) -> plt.Axes
```

#### Description:

Creates a blank image with specified width and height, displaying a grid.

#### Arguments:

| Argument     | Type    | Description                                          |
| ------------ | ------- | ---------------------------------------------------- |
| **`width`**  | **int** | The width of the image in pixels. (Default is 1000)  |
| **`height`** | **int** | The height of the image in pixels. (Default is 1000) |

#### Returns:

| Return Type    | Description                                 |
| -------------- | ------------------------------------------- |
| **`plt.Axes`** | The Axes object of the created blank image. |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    ax = plot_draw.create_blank_image(800, 600)
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A blank plot with a grid, 800x600 pixels.
```

### draw_three_axes

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L216C1-L343C14)

```python
draw_three_axes(
    arrow_length: float,
    arrow_thickness: float,
    offset_text: float,
    longx: float,
    axis_y_negative: bool,
    axis_x_negative: bool
) -> plt.Axes
```

#### Description:

Draws a set of three axes (x, y, z) with optional negative directions for x and y.

#### Arguments:

| Argument              | Type      | Description                                                   |
| --------------------- | --------- | ------------------------------------------------------------- |
| **`arrow_length`**    | **float** | The length of the arrows representing the axes.               |
| **`arrow_thickness`** | **float** | The thickness of the arrows.                                  |
| **`offset_text`**     | **float** | The distance between the end of the arrow and the label text. |
| **`longx`**           | **float** | The factor to adjust the length of the diagonal x-axis.       |
| **`axis_y_negative`** | **bool**  | Draws negative y-axis if True                                 |
| **`axis_x_negative`** | **bool**  | draws negative x-axis if True                                 |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc

def main(inputs):
    ax = msc.draw_three_axes(arrow_length=1, arrow_thickness=2, offset_text=0.1, longx=1.5, axis_y_negative=True, axis_x_negative=True)
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying three axes (x, y, z) with optional negative directions.

```

### draw_two_inclined_axes

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L346C1-L460C14)

```python
draw_two_inclined_axes(
    arrow_length: float,
    arrow_thickness: float,
    offset_text: float,
    longx: float,
    axis_y_negative: bool,
    axis_x_negative: bool
) -> plt.Axes
```

#### Description:

Draws two inclined axes (x and y) with optional negative directions.

#### Arguments:

| Argument              | Type      | Description                                                   |
| --------------------- | --------- | ------------------------------------------------------------- |
| **`arrow_length`**    | **float** | The length of the arrows representing the axes.               |
| **`arrow_thickness`** | **float** | The thickness of the arrows.                                  |
| **`offset_text`**     | **float** | The distance between the end of the arrow and the label text. |
| **`longx`**           | **float** | The factor to adjust the length of the diagonal y-axis.       |
| **`axis_y_negative`** | **bool**  | Draws negative y-axis if True                                 |
| **`axis_x_negative`** | **bool**  | Draws negative x-axis if True                                 |

#### Returns:

| Return Type    | Description                          |
| -------------- | ------------------------------------ |
| **`plt.Axes`** | The Axes object with the drawn axes. |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    ax = plot_draw.draw_two_inclined_axes(arrow_length=1, arrow_thickness=2, offset_text=0.1, longx=1.5, axis_y_negative=True, axis_x_negative=True)
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying two inclined axes (x and y) with optional negative directions.
```

## Segments

### plot_segment_pixels

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L463C1-L549C1)

```python
plot_segment_pixels(
    start_point_pixels: tuple,
    end_point_pixels: tuple,
    line_properties: dict = {"color": "k", "linewidth": 1, "linestyle": "dashed"},
    text: str = "",
    min_spacing: float = 150,
    fontsize: int = 15,
    text_loc: dict = {"ha": "center", "va": "top"},
    alpha: float = 0.8
) -> tuple
```

#### Description:

Plots a line segment between two points and adds a label at the end point.

#### Arguments:

| Argument                 | Type                 | Description                                                          |
| ------------------------ | -------------------- | -------------------------------------------------------------------- |
| **`start_point_pixels`** | **tuple**            | The starting point of the line segment (x, y).                       |
| **`end_point_pixels`**   | **tuple**            | The ending point of the line segment (x, y).                         |
| **`line_properties`**    | **dict** (optional)  | Properties for the line, including color, linewidth, and linestyle.  |
| **`text`**               | **str** (optional)   | The text to display near the end point of the line segment.          |
| **`min_spacing`**        | **float** (optional) | Minimum spacing for the text from the end point.                     |
| **`fontsize`**           | **int** (optional)   | Font size of the text.                                               |
| **`text_loc`**           | **dict** (optional)  | Dictionary specifying horizontal and vertical alignment of the text. |
| **`alpha`**              | **float** (optional) | Transparency level of the line segment.                              |

#### Returns:

| Return Type          | Description                               |
| -------------------- | ----------------------------------------- |
| **`(float, float)`** | The end point of the line segment (x, y). |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    start = (100, 200)
    end = (400, 500)
    end_point = plot_draw.plot_segment_pixels(start, end, text="Segment", min_spacing=50)
    plot = msc.print_plot(plt)
    return {'plot': plot, 'end_point': end_point}

# Expected output: A plot displaying a dashed line segment with a label "Segment".
# The end point of the segment is (400, 500).
```

### plot_annotate_arrow

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L551C1-L699C1)

```python
plot_annotate_arrow(
    start_point: tuple,
    trig_angle: float,
    vec_length: float,
    text: str = "",
    min_spacing: float = 150,
    fontsize: int = 11,
    text_loc: dict = {"ha": "center", "va": "top"},
    arrow_properties: dict = {
        "width": 2,
        "head_width": 15,
        "head_length": 15,
        "fc": "black",
        "ec": "black"
    },
    reverse_arrow: str = "no",
    text_in_center: str = "no",
    rev_text: str = "no",
    alpha: float = 0.8
) -> tuple[float, float]
```

#### Description:

Plots an annotated arrow starting from a given point and extending in a given direction.

#### Arguments:

| Argument               | Type                 | Description                                                                                               |
| ---------------------- | -------------------- | --------------------------------------------------------------------------------------------------------- |
| **`start_point`**      | **tuple**            | The starting point of the arrow (x, y).                                                                   |
| **`trig_angle`**       | **float**            | The angle of the arrow in degrees.                                                                        |
| **`vec_length`**       | **float**            | The length of the arrow.                                                                                  |
| **`text`**             | **str** (optional)   | The text to display near the arrow.                                                                       |
| **`min_spacing`**      | **float** (optional) | Minimum spacing for the text from the end of the arrow.                                                   |
| **`fontsize`**         | **int** (optional)   | Font size of the text.                                                                                    |
| **`text_loc`**         | **dict** (optional)  | Dictionary specifying horizontal and vertical alignment of the text.                                      |
| **`arrow_properties`** | **dict** (optional)  | Properties for the arrow, including width, head_width, head_length, fill color (fc), and edge color (ec). |
| **`reverse_arrow`**    | **str** (optional)   | Whether to reverse the direction of the arrow. (Default is 'no')                                          |
| **`text_in_center`**   | **str** (optional)   | Whether to place the text in the center of the arrow. (Default is 'no')                                   |
| **`rev_text`**         | **str** (optional)   | Whether to reverse the text orientation. (Default is 'no')                                                |
| **`alpha`**            | **float** (optional) | Transparency level of the arrow.                                                                          |

#### Returns:

| Return Type          | Description                        |
| -------------------- | ---------------------------------- |
| **`(float, float)`** | The end point of the arrow (x, y). |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    start = (100, 200)
    angle = 45
    length = 100
    end_point = plot_draw.plot_annotate_arrow(start, angle, length, text="Arrow", min_spacing=50)
    plot = msc.print_plot(plt)
    return {'plot': plot, 'end_point': end_point}

# Expected output: A plot displaying an annotated arrow starting from (100, 200) at a 45-degree angle.
# The end point of the arrow is (170.71067811865476, 270.71067811865476)


```

### draw_custom_arrow

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L700C1-L785C1)

```python
draw_custom_arrow(
    ax: plt.Axes,
    start_point: tuple,
    point_2: tuple,
    factor: float,
    max_value: float,
    arrow_vector_length: float,
    arrow_width: float,
    arrow_color: str = "blue",
    line_width: float = 1,
    text: str = None
) -> None
```

#### Description:

Draws a custom arrow from a start point to another point on a given axis, using pixel-based parameters.

#### Arguments:

| Argument                  | Type                     | Description                                                        |
| ------------------------- | ------------------------ | ------------------------------------------------------------------ |
| **`ax`**                  | **matplotlib.axes.Axes** | The Axes object to draw the arrow on.                              |
| **`start_point`**         | **tuple**                | The starting point of the arrow (x, y) in pixels.                  |
| **`point_2`**             | **tuple**                | The end point of the arrow (x, y) in pixels.                       |
| **`factor`**              | **float**                | A factor to adjust the position of the text relative to the arrow. |
| **`max_value`**           | **float**                | The maximum value for scaling the arrow length.                    |
| **`arrow_vector_length`** | **float**                | The length of the arrow vector.                                    |
| **`arrow_width`**         | **float**                | The width of the arrow head in pixels.                             |
| **`arrow_color`**         | **str** (optional)       | The color of the arrow. (Default is 'blue')                        |
| **`line_width`**          | **float** (optional)     | The width of the arrow line. (Default is 1)                        |
| **`text`**                | **str** (optional)       | The text to display near the end of the arrow.                     |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    fig, ax = plt.subplots()
    plot_draw.draw_custom_arrow(ax, (0, 0), (100, 100), factor=0.5, max_value=100, arrow_vector_length=50, arrow_width=5, text="Custom Arrow")
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a custom arrow with the label "Custom Arrow".

```

### calculate_arrow_endpoint_pixels

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L787C1-L823C1)

```python
calculate_arrow_endpoint_pixels(
    start_point: tuple,
    trig_angle: float,
    vec_length: float
) -> tuple[float, float]
```

#### Description:

Calculates the end point of an arrow in pixel coordinates.

#### Arguments:

| Argument          | Type      | Description                                                  |
| ----------------- | --------- | ------------------------------------------------------------ |
| **`start_point`** | **tuple** | The starting point of the arrow (x, y) in pixel coordinates. |
| **`trig_angle`**  | **float** | The angle of the arrow in degrees.                           |
| **`vec_length`**  | **float** | The length of the arrow.                                     |

#### Returns:

| Return Type          | Description                                             |
| -------------------- | ------------------------------------------------------- |
| **`(float, float)`** | The end point of the arrow (x, y) in pixel coordinates. |

#### Example:

```python
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    endpoint = plot_draw.calculate_arrow_endpoint_pixels((100, 200), 45, 50)
    return {"endpoint": endpoint}

# Expected output: {"endpoint": (135.35533905932738, 235.35533905932738)}
```

### plot_segment

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L825C1-L911C21)

```python
plot_segment(
    start_point: tuple,
    trig_angle: float,
    vec_length: float,
    line_properties: dict = {"color": "blue", "linewidth": 1},
    text: str = "",
    min_spacing: float = 150,
    fontsize: int = 15,
    text_loc: dict = {"ha": "center", "va": "top"},
    alpha: float = 0.8
) -> tuple[float, float]
```

#### Description:

Plots a line segment starting from a given point with a specific angle and length.

#### Arguments:

| Argument              | Type                 | Description                                                       |
| --------------------- | -------------------- | ----------------------------------------------------------------- |
| **`start_point`**     | **tuple**            | The starting point of the line segment (x, y).                    |
| **`trig_angle`**      | **float**            | The angle of the line segment in degrees.                         |
| **`vec_length`**      | **float**            | The length of the line segment.                                   |
| **`line_properties`** | **dict** (optional)  | Properties of the line segment such as color and linewidth.       |
| **`text`**            | **str** (optional)   | The text to display near the end of the line segment.             |
| **`min_spacing`**     | **float** (optional) | Minimum spacing between the end of the line segment and the text. |
| **`fontsize`**        | **int** (optional)   | The font size of the text.                                        |
| **`text_loc`**        | **dict** (optional)  | Location parameters for the text.                                 |
| **`alpha`**           | **float** (optional) | The alpha value for transparency.                                 |

#### Returns:

| Return Type          | Description                               |
| -------------------- | ----------------------------------------- |
| **`(float, float)`** | The end point of the line segment (x, y). |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    end_point = plot_draw.plot_segment((100, 200), 45, 50, text='Value')
    plot = msc.print_plot(plt)
    return {'plot': plot, 'end_point': end_point}

# Expected output: A plot displaying a line segment starting from (100, 200) at a 45-degree angle with the label "Value".
# The end point of the segment is (135.35533905932738, 235.35533905932738).
```

### plot_segment_dashed

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L914C1-L1001C21)

```python
plot_segment_dashed(
    start_point: tuple,
    trig_angle: float,
    vec_length: float,
    line_properties: dict = {"color": "blue", "linestyle": "dashed", "linewidth": 1},
    text: str = "",
    min_spacing: float = 150,
    fontsize: int = 15,
    text_loc: dict = {"ha": "center", "va": "top"},
    alpha: float = 0.8
) -> tuple[float, float]
```

#### Description:

Plots a dashed line segment starting from a given point with a specific angle and length.

#### Arguments:

| Argument              | Type                | Description                                                 |
| --------------------- | ------------------- | ----------------------------------------------------------- |
| **`start_point`**     | **tuple**           | The starting point of the line segment (x, y).              |
| **`trig_angle`**      | **float**           | The angle of the line segment in degrees.                   |
| **`vec_length`**      | **float**           | The length of the line segment.                             |
| **`line_properties`** | **dict** (optional) | Properties of the line segment such as color and linewidth. |

|
| **`text`** | **str** (optional) | The text to display near the end of the line segment. |
| **`min_spacing`** | **float** (optional) | Minimum spacing between the end of the line segment and the text. |
| **`fontsize`** | **int** (optional) | The font size of the text. |
| **`text_loc`** | **dict** (optional) | Location parameters for the text. |
| **`alpha`** | **float** (optional) | The alpha value for transparency. |

#### Returns:

| Return Type          | Description                               |
| -------------------- | ----------------------------------------- |
| **`(float, float)`** | The end point of the line segment (x, y). |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    end_point = plot_draw.plot_segment_dashed((100, 200), 45, 50, text='Value')
    plot = msc.print_plot(plt)
    return {'plot': plot, 'end_point': end_point}

# Expected output: A plot displaying a dashed line segment starting from (100, 200) at a 45-degree angle with the label "Value".
# The end point of the segment is (135.35533905932738, 235.35533905932738)
```

## Shapes

### draw_custom_circle

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1004C1-L1041C1)

```python
draw_custom_circle(
    ax: plt.Axes,
    center_point: tuple,
    circle_size: float = 100,
    circle_color: str = "black"
) -> None
```

#### Description:

Draws a custom circle on a given axis.

#### Arguments:

| Argument           | Type                     | Description                                   |
| ------------------ | ------------------------ | --------------------------------------------- |
| **`ax`**           | **matplotlib.axes.Axes** | The Axes object to draw the circle on.        |
| **`center_point`** | **tuple**                | The center point of the circle (x, y).        |
| **`circle_size`**  | **float** (optional)     | The size of the circle. (Default is 100)      |
| **`circle_color`** | **str** (optional)       | The color of the circle. (Default is 'black') |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    fig, ax = plt.subplots()
    plot_draw.draw_custom_circle(ax, (100, 100), circle_size=200, circle_color='red')
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a red circle with a center at (100, 100) and size 200.

```

### draw_rounded_rectangle

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1042C1-L1120C1)

```python
draw_rounded_rectangle(
    middle_point: tuple,
    width: float,
    height: float,
    radius: float,
    color: str = "black"
) -> None
```

#### Description:

Draws a rounded rectangle with specified properties.

#### Arguments:

| Argument           | Type               | Description                                                       |
| ------------------ | ------------------ | ----------------------------------------------------------------- |
| **`middle_point`** | **tuple**          | The middle point of the top side of the rounded rectangle (x, y). |
| **`width`**        | **float**          | The width of the rounded rectangle.                               |
| **`height`**       | **float**          | The height of the rounded rectangle.                              |
| **`radius`**       | **float**          | The radius of the corners.                                        |
| **`color`**        | **str** (optional) | The color of the rectangle. (Default is 'black')                  |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_rounded_rectangle((0, 0), 4, 2, 0.5, color='blue')
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a blue rounded rectangle with specified dimensions and corner radius.

```

### calculate_intersection_point

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1122C1-L1178C44)

```python
calculate_intersection_point(
    point1: tuple,
    angle1: float,
    point2: tuple,
    angle2: float
) -> tuple[float, float]
```

#### Description:

Calculates the intersection point of two lines defined by points and angles.

#### Arguments:

| Argument     | Type      | Description                                                                      |
| ------------ | --------- | -------------------------------------------------------------------------------- |
| **`point1`** | **tuple** | The coordinates of the first point (x, y) through which the first line passes.   |
| **`angle1`** | **float** | The angle of the first line in degrees.                                          |
| **`point2`** | **tuple** | The coordinates of the second point (x, y) through which the second line passes. |
| **`angle2`** | **float** | The angle of the second line in degrees.                                         |

#### Returns:

| Return Type          | Description                                       |
| -------------------- | ------------------------------------------------- |
| **`(float, float)`** | The coordinates of the intersection point (x, y). |

#### Example:

```python
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    intersection = plot_draw.calculate_intersection_point((0, 0), 45, (1, 1), 135)
    return {"intersection": intersection}

# Expected output: {"intersection": (1.0, 0.9999999999999999)}
```

### draw_segment

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1181C1-L1229C1)

```python
draw_segment(
    start_point: tuple,
    final_point: tuple,
    line_width: float = 0.001,
    color: str = "black"
) -> None
```

#### Description:

Draws a segment between two points with a specified line width and color.

#### Arguments:

| Argument          | Type                 | Description                                    |
| ----------------- | -------------------- | ---------------------------------------------- |
| **`start_point`** | **tuple**            | The coordinates of the starting point (x, y).  |
| **`final_point`** | **tuple**            | The coordinates of the final point (x, y).     |
| **`line_width`**  | **float** (optional) | The width of the segment. (Default is 0.001)   |
| **`color`**       | **str** (optional)   | The color of the segment. (Default is 'black') |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_segment((0, 0), (1, 1), line_width=0.005, color='blue')
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a blue segment from (0, 0) to (1, 1).

```

### plot_annotate_arrow_end

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1231C1-L1369C1)

```python
plot_annotate_arrow_end(
    end_point: tuple,
    trig_angle: float,
    vec_length: float,
    text: str = "",
    text_distance: float = 0.5,
    fontsize: int = 12,
    text_loc: dict = {"ha": "center", "va": "top"},
    arrow_properties: dict = {
        "width": 2,
        "head_width": 15,
        "head_length": 15,
        "fc": "black",
        "ec": "black"
    },
    reverse_arrow: str = "no",
    text_in_center: str = "no",
    rev_text: str = "no",
    alpha: float = 0.8
) -> tuple[float, float]
```

#### Description:

Plots an arrow annotation at the end point of a vector.

#### Arguments:

| Argument               | Type                 | Description                                                                                                                 |
| ---------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **`end_point`**        | **tuple**            | The coordinates of the end point (x, y) of the vector.                                                                      |
| **`trig_angle`**       | **float**            | The trigonometric angle of the vector in degrees.                                                                           |
| **`vec_length`**       | **float**            | The length of the vector.                                                                                                   |
| **`text`**             | **str** (optional)   | The text to be displayed near the arrow.                                                                                    |
| **`text_distance`**    | **float** (optional) | The distance between the text and the arrow. (Default is 0.5)                                                               |
| **`fontsize`**         | **int** (optional)   | The font size of the text. (Default is 12)                                                                                  |
| **`text_loc`**         | **dict** (optional)  | The text alignment. (Default is \{'ha': 'center', 'va': 'top'\})                                                            |
| **`arrow_properties`** | **dict** (optional)  | The properties of the arrow. (Default is \{'width': 2, 'head_width': 15, 'head_length': 15, 'fc': 'black', 'ec': 'black'\}) |
| **`reverse_arrow`**    | **str** (optional)   | Whether to reverse the arrow. (Default is 'no')                                                                             |
| **`text_in_center`**   | **str** (optional)   | Whether to place the text in the center. (Default is 'no')                                                                  |
| **`rev_text`**         | **str** (optional)   | Whether to reverse the text. (Default is 'no')                                                                              |
| **`alpha`**            | **float** (optional) | The transparency of the arrow and text. (Default is 0.8)                                                                    |

#### Returns:

| Return Type          | Description                                             |
| -------------------- | ------------------------------------------------------- |
| **`(float, float)`** | The coordinates of the start point (x, y) of the arrow. |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    start_point = plot_draw.plot_annotate_arrow_end((1, 1), 45, 1, text="End", text_distance=0.5, fontsize=12, text_loc={'ha': 'center', 'va': 'top'})
    plot = msc.print_plot(plt)
    return {'plot': plot, 'start_point': start_point}

# Expected output: A plot displaying an arrow annotation at the end point (1, 1) with the label "End".
# The coordinates of the start point of the arrow is (10.899494936611665, 10.899494936611665)
```

### draw_arc_with_text

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1371C1-L1430C1)

```python
draw_arc_with_text(
    start_point: tuple,
    radius: float,
    start_angle: float,
    final_angle: float,
    text: str
) -> None
```

#### Description:

Draws an arc with text annotation.

#### Arguments:

| Argument          | Type      | Description                                                                           |
| ----------------- | --------- | ------------------------------------------------------------------------------------- |
| **`start_point`** | **tuple** | The coordinates (x, y) of the center point of the circle from which the arc is drawn. |
| **`radius`**      | **float** | The radius of the arc.                                                                |
| **`start_angle`** | **float** | The start angle of the arc in degrees.                                                |
| **`final_angle`** | **float** | The final angle of the arc in degrees.                                                |
| **`text`**        | **str**   | The text to be displayed along the arc.                                               |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_arc_with_text((0, 0), 5, 30, 120, "Sample Text")
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying an arc with the text "Sample Text" along it.

```

### draw_three_axes_rotated

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1431C1-L1566C1)

```python
draw_three_axes_rotated(
    arrow_length: float,
    line_thickness: float,
    offset_text: float,
    longx: float,
    negativeaxis_y: int,
    negativeaxis_x: int
) -> plt.Axes
```

#### Description:

Draws three rotated axes in a 3D coordinate system.

#### Arguments:

| Argument             | Type      | Description                                               |
| -------------------- | --------- | --------------------------------------------------------- |
| **`arrow_length`**   | **float** | The length of the arrow.                                  |
| **`line_thickness`** | **float** | The thickness of the line.                                |
| **`offset_text`**    | **float** | The offset of the text from the arrow.                    |
| **`longx`**          | **float** | The length of the x-axis.                                 |
| **`negativeaxis_y`** | **int**   | Whether to include negative y-axis (1 for yes, 0 for no). |
| **`negativeaxis_x`** | **int**   | Whether to include negative x-axis (1 for yes, 0 for no). |

#### Returns:

| Return Type    | Description                                     |
| -------------- | ----------------------------------------------- |
| **`plt.Axes`** | The matplotlib Axes object containing the plot. |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    ax = plot_draw.draw_three_axes_rotated(arrow_length=1.0, line_thickness=1.5, offset_text=0.1, longx=1.5, negativeaxis_y=1, negativeaxis_x=1)
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying three rotated axes in a 3D coordinate system.
```

### draw_double_arrowhead

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1568C1-L1639C6)

```python
draw_double_arrowhead(
    start_point: tuple,
    end_point: tuple,
    color: str = "black",
    line_thickness: float = 1
) -> None
```

#### Description:

Draws a double arrowhead between two points.

#### Arguments:

| Argument             | Type                 | Description                                       |
| -------------------- | -------------------- | ------------------------------------------------- |
| **`start_point`**    | **tuple**            | Coordinates of the start point (x, y).            |
| **`end_point`**      | **tuple**            | Coordinates of the end point (x, y).              |
| **`color`**          | **str** (optional)   | Color of the arrow and line. (Default is 'black') |
| **`line_thickness`** | **float** (optional) | Thickness of the line. (Default is 1)             |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_double_arrowhead(start_point=(0, 0), end_point=(1, 1), color='black', line_thickness=1)
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a double arrowhead between (0, 0) and (1, 1).

```

### draw_custom_arrow_end

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1642C1-L1705C1)

```python
draw_custom_arrow_end(
    start_point: tuple,
    end_point: tuple,
    color: str = "black",
    line_thickness: float = 1
) -> None
```

#### Description:

Draws a custom arrow at the end of a line segment.

#### Arguments:

| Argument             | Type                 | Description                                       |
| -------------------- | -------------------- | ------------------------------------------------- |
| **`start_point`**    | **tuple**            | Coordinates of the start point (x, y).            |
| **`end_point`**      | **tuple**            | Coordinates of the end point (x, y).              |
| **`color`**          | **str** (optional)   | Color of the arrow and line. (Default is 'black') |
| **`line_thickness`** | **float** (optional) | Thickness of the line. (Default is 1)             |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_custom_arrow_end(start_point=(0, 0), end_point=(1, 1), color='black', line_thickness=1)
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a custom arrow at the end of a line segment from (0, 0) to (1, 1).
```

### draw_two_axes

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1706C1-L1815C14)

```python
draw_two_axes(
    arrow_length: float,
    line_thickness: float,
    offset_text: float,
    longx: float,
    negativeaxis_y: int,
    negativeaxis_x: int
) -> plt.Axes
```

#### Description:

Draws two axes representing the x and y directions.

#### Arguments:

| Argument             | Type      | Description                                    |
| -------------------- | --------- | ---------------------------------------------- |
| **`arrow_length`**   | **float** | Length of the arrows representing the axes.    |
| **`line_thickness`** | **float** | Thickness of the arrows representing the axes. |
| **`offset_text`**    | **float** | Offset for the axis labels.                    |
| **`longx`**          | **float** | Length factor for the x-axis.                  |
| **`negativeaxis_y`** | **int**   | Draws negative y-axis if True.                 |
| **`negativeaxis_x`** | **int**   | Draws negative x-axis if True                  |

#### Returns:

| Return Type    | Description  |
| -------------- | ------------ |
| **`plt.Axes`** | Axes object. |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    ax = plot_draw.draw_two_axes(arrow_length=1.0, line_thickness=1.5, offset_text=0.1, longx=1.5, negativeaxis_y=1, negativeaxis_x=1)
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying two axes representing the x and y directions.
```

### vertical_arrow_rain

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1818C1-L1864C1)

```python
vertical_arrow_rain(
    quantity_arrows: int,
    start_point: tuple,
    final_point: tuple,
    y_origin: float
) -> None
```

#### Description:

Draws a specific quantity of arrows from equidistant points on a segment that extends from start_point to final_point, with all arrows pointing to y_origin.

#### Arguments:

| Argument              | Type      | Description                                                  |
| --------------------- | --------- | ------------------------------------------------------------ |
| **`quantity_arrows`** | **int**   | Number of arrows to draw.                                    |
| **`start_point`**     | **tuple** | Tuple (x, y) representing the starting point of the segment. |
| **`final_point`**     | **tuple** | Tuple (x, y) representing the final point of the segment.    |
| **`y_origin`**        | **float** | y-coordinate to which all arrows should point.               |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.vertical_arrow_rain(quantity_arrows=5, start_point=(0, 1), final_point=(1, 1), y_origin=0)
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a vertical arrow rain from the segment (0, 1) to (1, 1) pointing to y=0.
```

### draw_rain_arrows_horizontal

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1865C1-L1918C1)

```python
draw_rain_arrows_horizontal(
    quantity_arrows: int,
    x_origin: float,
    start_point: tuple,
    final_point: tuple
) -> None
```

#### Description:

Draws a specific quantity of arrows from a vertical line at x_origin to equidistant points on a segment that extends from start_point to final_point.

#### Arguments:

| Argument              | Type      | Description                                                  |
| --------------------- | --------- | ------------------------------------------------------------ |
| **`quantity_arrows`** | **int**   | Number of arrows to draw.                                    |
| **`x_origin`**        | **float** | x-coordinate from which all arrows originate.                |
| **`start_point`**     | **tuple** | Tuple (x, y) representing the starting point of the segment. |
| **`final_point`**     | **tuple** | Tuple (x, y) representing the final point of the segment.    |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_rain_arrows_horizontal(quantity_arrows=5, x_origin=0, start_point=(0, 1), final_point=(1, 1))
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a horizontal arrow rain from x=0 to the segment (0, 1) to (1, 1).

```

## Angles

### calculate_angle

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1919C1-L1954C1)

```python
calculate_angle(
    start_point: tuple,
    final_point: tuple
) -> float
```

#### Description:

Calculates the angle (in degrees) between two points.

#### Arguments:

| Argument          | Type      | Description                                   |
| ----------------- | --------- | --------------------------------------------- |
| **`start_point`** | **tuple** | Tuple (x, y) representing the starting point. |
| **`final_point`** | **tuple** | Tuple (x, y) representing the final point.    |

#### Returns:

| Return Type | Description                                  |
| ----------- | -------------------------------------------- |
| **`float`** | The angle in degrees between the two points. |

#### Example:

```python
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    angle = plot_draw.calculate_angle(start_point=(0, 0), final_point=(1, 1))
    return {"angle": angle}

# Expected output: {"angle": 45.0}
```

### draw_segment_1

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1955C1-L1979C1)

```python
draw_segment_1(
    start: Union[tuple, list],
    end: Union[tuple, list]
) -> None
```

#### Description:

Draws a line segment in black ('k').

#### Arguments:

| Argument    | Type              | Description                                     |
| ----------- | ----------------- | ----------------------------------------------- |
| **`start`** | **tuple or list** | The coordinates of the starting point [x1, y1]. |
| **`end`**   | **tuple or list** | The coordinates of the ending point [x2, y2].   |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_segment_1((0, 0), (10, 0))
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a black line segment from (0, 0) to (10, 0).

```

### draw_segment_2

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L1981C1-L2004C64)

```python
draw_segment_2(
    start: Union[tuple, list],
    end: Union[tuple, list]
) -> None
```

#### Description:

Draws a line segment in red ('r').

#### Arguments:

| Argument    | Type              | Description            |
| ----------- | ----------------- | ---------------------- |
| **`start`** | **tuple or list** | The coordinates of the |

starting point [x1, y1]. |
| **`end`** | **tuple or list** | The coordinates of the ending point [x2, y2]. |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_segment_2((0, 2.6), (10, 1))
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a red line segment from (0, 2.6) to (10, 1).

```

### draw_segment_3

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L2007C1-L2031C1)

```python
draw_segment_3(
    start: Union[tuple, list],
    end: Union[tuple, list]
) -> None
```

#### Description:

Draws a line segment in blue ('b').

#### Arguments:

| Argument    | Type              | Description                                     |
| ----------- | ----------------- | ----------------------------------------------- |
| **`start`** | **tuple or list** | The coordinates of the starting point [x1, y1]. |
| **`end`**   | **tuple or list** | The coordinates of the ending point [x2, y2].   |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_segment_3((0, 2.6), (10, 1))
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a blue line segment from (0, 2.6) to (10, 1).

```

### get_arc_points

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.1.9/mecsimcalc/eng130/plot_draw.py#L2033C1-L2074C16)

```python
get_arc_points(
    start_angle: float,
    end_angle: float,
    radius: float,
    center: Union[tuple, list]
) -> tuple[np.ndarray, np.ndarray]
```

#### Description:

Calculates points along a circular arc defined by a start angle and an end angle.

#### Arguments:

| Argument          | Type              | Description                                        |
| ----------------- | ----------------- | -------------------------------------------------- |
| **`start_angle`** | **float**         | The starting angle of the arc in degrees.          |
| **`end_angle`**   | **float**         | The ending angle of the arc in degrees.            |
| **`radius`**      | **float**         | The radius of the arc.                             |
| **`center`**      | **tuple or list** | The coordinates of the center of the arc [cx, cy]. |

#### Returns:

| Return Type                         | Description                                |
| ----------------------------------- | ------------------------------------------ |
| **`Tuple[np.ndarray, np.ndarray]`** | The x and y coordinates of the arc points. |

#### Example:

```python
import matplotlib.pyplot as plt
import numpy as np
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    arc_points_x1, arc_points_y1 = plot_draw.get_arc_points(90, 240, 0.25, (0, -0.25))
    plt.plot(arc_points_x1, arc_points_y1, 'k')
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying an arc from 90 to 240 degrees with a radius of 0.25 centered at (0, -0.25).

```
