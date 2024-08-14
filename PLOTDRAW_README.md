# Plot Draw v0.2.0

This library is designed to provide a set of functions for drawing various types of plots, arrows, segments, and shapes using Matplotlib. These functions allow for customized plotting and annotation of graphical elements.

## General

### blank_canvas

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L7C1-L49C14)

```python
blank_canvas(
    width = 800,
    height = 600,
    color = "white"
)
```

#### Description:

Creates a blank image with specified width and height, displaying a grid.

#### Arguments:

| Argument     | Type               | Description                                             |
| ------------ | ------------------ | ------------------------------------------------------- |
| **`width`**  | **int** (optional) | The width of the image in pixels. (Default is 800)      |
| **`height`** | **int** (optional) | The height of the image in pixels. (Default is 600)     |
| **`color`**  | **str**(optional)  | The background color of the image. (Default is 'white') |

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
    ax = plot_draw.blank_canvas()
    plot = msc.print_plot(plt)
    return {'plot': plot}
```

<div style={{textAlign: 'center'}}>
![white canvas](./images/blank_canvas.png)
</div>

## lines and arrows

### draw_line

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L52C1-L110C1)

```python
draw_line(
    start,
    end,
    color = "black",
    line_width = None,
    ax = None
)
```

#### Description:

Draws a segment between two points with a specified line width and color.

#### Arguments:

| Argument         | Type                    | Description                                               |
| ---------------- | ----------------------- | --------------------------------------------------------- |
| **`start`**      | **tuple**               | The coordinates of the starting point (x, y).             |
| **`end`**        | **tuple**               | The coordinates of the final point (x, y).                |
| **`color`**      | **str** (optional)      | The color of the segment. (Default is 'black')            |
| **`line_width`** | **float** (optional)    | The width of the segment. (Default is None)               |
| **`ax`**         | **plt.Axes** (optional) | The Axes object to draw the segment on. (Default is None) |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_line((0, 0), (1, 1), color='blue', line_width=0.005)
    plot = msc.print_plot(plt)
    return {'plot': plot}
```

<div style={{textAlign: 'center'}}>
![segment](./images/draw_line.png)
</div>

### draw_arrow

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L112C1-L190C1)

```python
draw_arrow(
    start,
    end,
    thickness = 5,
    color = "black",
    text = "",
    text_offset = 0.1,
    head_width = 0.08,
    head_length = 0.08,
    fontsize = 12,
    ax = None
)
```

#### Description:

Draws an arrow between two points on a plot.

#### Arguments:

| Argument          | Type                    | Description                                                                       |
| ----------------- | ----------------------- | --------------------------------------------------------------------------------- |
| **`start`**       | **Tuple[float, float]** | The starting point of the arrow (x, y).                                           |
| **`end`**         | **Tuple[float, float]** | The ending point of the arrow (x, y).                                             |
| **`thickness`**   | **float** (optional)    | The thickness of the arrow line. (Default is 5)                                   |
| **`color`**       | **str** (optional)      | The color of the arrow. (Default is 'black')                                      |
| **`text`**        | **str** (optional)      | Text to display near the arrow. (Default is None)                                 |
| **`text_offset`** | **float** (optional)    | Distance from the arrow end point where the text will be placed. (Default is 0.5) |
| **`head_width`**  | **float** (optional)    | Width of the arrow head. (Default is 0.08)                                        |
| **`head_length`** | **float** (optional)    | Length of the arrow head. (Default is 0.08)                                       |
| **`fontsize`**    | **float** (optional)    | Font size of the text. (Default is 12)                                            |
| **`ax`**          | **plt.Axes** (optional) | The Axes object to draw the arrow on. (Default is None)                           |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_arrow((0, 0), (1, 1), color='red', text='Arrow')
    plt.xlim(-1, 2)
    plt.ylim(-1, 2)
    plot = msc.print_plot(plt)
    return {'plot': plot}
```

#### Output:

<div style={{textAlign: 'center'}}>
![Arrow](./images/draw_arrow.png)
</div>

### draw_double_arrowhead

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L192C1-L269C6)

```python
draw_double_arrowhead(
    start,
    end,
    color = "black",
    line_thickness = 1,
    ax = None
)
```

#### Description:

Draws a double arrowhead between two points.

#### Arguments:

| Argument             | Type                    | Description                                       |
| -------------------- | ----------------------- | ------------------------------------------------- |
| **`start`**          | **tuple**               | Coordinates of the start point (x, y).            |
| **`end`**            | **tuple**               | Coordinates of the end point (x, y).              |
| **`color`**          | **str** (optional)      | Color of the arrow and line. (Default is 'black') |
| **`line_thickness`** | **float** (optional)    | Thickness of the line. (Default is 1)             |
| **`ax`**             | **plt.Axes** (optional) | The Axes object to draw the arrow on.             |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_double_arrowhead(start=(0, 0), end=(1, 1))
    plot = msc.print_plot(plt)
    return {'plot': plot}
```

<div style={{textAlign: 'center'}}>
![double arrowhead](./images/draw_double_arrowhead.png)
</div>

### vertical_arrow_rain

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L272C1-L348C10)

```python
vertical_arrow_rain(
    quantity,
    start,
    end,
    y_origin = 0,
    arrow_color = "blue",
    head_width = 0.05,
    head_length = 0.1,
    ax = None
)
```

#### Description:

Draws a specific quantity of arrows from equidistant points on a segment that extends from start to end, with all arrows pointing to y_origin.

#### Arguments:

| Argument          | Type         | Description                                                   |
| ----------------- | ------------ | ------------------------------------------------------------- |
| **`quantity`**    | **int**      | Number of arrows to draw.                                     |
| **`start`**       | **tuple**    | Tuple (x, y) representing the starting point of the segment.  |
| **`end`**         | **tuple**    | Tuple (x, y) representing the final point of the segment.     |
| **`y_origin`**    | **float**    | y-coordinate to which all arrows should point. (Default is 0) |
| **`arrow_color`** | **str**      | Color of the arrows. (Default is 'blue')                      |
| **`head_width`**  | **float**    | Width of the arrow head. (Default is 0.05)                    |
| **`head_length`** | **float**    | Length of the arrow head. (Default is 0.1)                    |
| **`ax`**          | **plt.Axes** | The Axes object to draw the arrows on.                        |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.vertical_arrow_rain(quantity=5, start=(0, 1), end=(1, 1), y_origin=0)
    plot = msc.print_plot(plt)
    return {'plot': plot}
```

<div style={{textAlign: 'center'}}>
![vertical arrow rain](./images/vertical_arrow_rain.png)
</div>

### horizontal_arrow_rain

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L351C1-L427C1)

```python
horizontal_arrow_rain(
    quantity,
    start,
    end,
    x_origin = 0,
    arrow_color = "blue",
    head_width = 0.05,
    head_length = 0.1,
    ax = None
)
```

#### Description:

Draws a specific quantity of arrows from a vertical line at x_origin to equidistant points on a segment that extends from start to end.

#### Arguments:

| Argument          | Type         | Description                                                  |
| ----------------- | ------------ | ------------------------------------------------------------ |
| **`quantity`**    | **int**      | Number of arrows to draw.                                    |
| **`start`**       | **tuple**    | Tuple (x, y) representing the starting point of the segment. |
| **`end`**         | **tuple**    | Tuple (x, y) representing the final point of the segment.    |
| **`x_origin`**    | **float**    | x-coordinate from which all arrows originate. (Default is 0) |
| **`arrow_color`** | **str**      | Color of the arrows. (Default is 'blue')                     |
| **`head_width`**  | **float**    | Width of the arrow head. (Default is 0.05)                   |
| **`head_length`** | **float**    | Length of the arrow head. (Default is 0.1)                   |
| **`ax`**          | **plt.Axes** | The Axes object to draw the arrows on. (Default is None)     |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.horizontal_arrow_rain(quantity=5, start=(1, 1), end=(1, 0), x_origin=0)
    plot = msc.print_plot(plt)
    return {'plot': plot}
```

<div style={{textAlign: 'center'}}>
![horizontal arrow rain](./images/horizontal_arrow_rain.png)
</div>

## Shapes

### draw_circle

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L429C1-L468C58)

```python
draw_circle(
    center = (0, 0),
    radius = 10,
    color = "black",
    ax = None
)
```

#### Description:

Draws a custom circle on a given axis.

#### Arguments:

| Argument     | Type                    | Description                                                |
| ------------ | ----------------------- | ---------------------------------------------------------- |
| **`center`** | **tuple** (optional)    | The center point of the circle (x, y). (Default is (0, 0)) |
| **`radius`** | **float** (optional)    | The size of the circle. (Default is 100)                   |
| **`color`**  | **str** (optional)      | The color of the circle. (Default is 'black')              |
| **`ax`**     | **plt.Axes** (optional) | The Axes object to draw the circle on. (Default is None)   |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_circle((100, 100), radius=20, color='red')
    plot = msc.print_plot(plt)
    return {'plot': plot}

# Expected output: A plot displaying a red circle with a center at (100, 100) and size 200.
```

<div style={{textAlign: 'center'}}>
![arrow](./images/draw_circle.png)
</div>

### draw_semicircle

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L471C1-L557C10)

```python
draw_semicircle(
    radius,
    start_angle,
    end_angle,
    center = (0, 0),
    degrees = False,
    color = "red",
    text = "",
    text_offset = 0.1,
    fontsize = 12,
    ax = None,
)
```

#### Description:

Draws an arc of a circumference with a given radius between two angles.

#### Arguments:

| Argument          | Type                    | Description                                                                     |
| ----------------- | ----------------------- | ------------------------------------------------------------------------------- |
| **`radius`**      | **float**               | The radius of the circumference.                                                |
| **`start_angle`** | **float**               | The starting angle of the arc in radians.                                       |
| **`end_angle`**   | **float**               | The ending angle of the arc in radians.                                         |
| **`center`**      | **tuple** (optional)    | The center of the circumference. (Default is (0, 0))                            |
| **`degrees`**     | **bool** (optional)     | Whether the angles are. (Default is False)                                      |
| **`color`**       | **str** (optional)      | The color of the arc. (Default is 'red')                                        |
| **`text`**        | **str** (optional)      | Text to display near the arc. (Default is None)                                 |
| **`text_offset`** | **float** (optional)    | Distance from the arc end point where the text will be placed. (Default is 0.1) |
| **`fontsize`**    | **float** (optional)    | Font size of the text. (Default is 12)                                          |
| **`ax`**          | **plt.Axes** (optional) | The Axes object to draw the arc on. (Default is None)                           |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_semicircle(5, 0, 90, degrees=True)
    plot = msc.print_plot(plt)
    return {'plot': plot}.
```

<div style={{textAlign: 'center'}}>
![quarter circle arc](./images/draw_semicircle.png)
</div>

### draw_rounded_rectangle

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L560C1-L643C25)

```python
draw_rounded_rectangle(
    width,
    height,
    center = (0, 0),
    corner_radius = 0.5,
    color = "black",
    ax = None
)
```

#### Description:

Draws a rounded rectangle with specified properties.

#### Arguments:

| Argument            | Type                    | Description                                                                           |
| ------------------- | ----------------------- | ------------------------------------------------------------------------------------- |
| **`width`**         | **float**               | The width of the rounded rectangle.                                                   |
| **`height`**        | **float**               | The height of the rounded rectangle.                                                  |
| **`center`**        | **tuple** (optional)    | The middle point of the top side of the rounded rectangle (x, y). (Default is (0, 0)) |
| **`corner_radius`** | **float** (optional)    | The radius of the corners. (Default is 0.5)                                           |
| **`color`**         | **str** (optional)      | The color of the rectangle. (Default is 'black')                                      |
| **`ax`**            | **plt.Axes** (optional) | The Axes object to draw the rectangle on. (Default is None)                           |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_rounded_rectangle(4, 2, center = (0,0), corner_radius = 0.5,  color='blue')
    plot = msc.print_plot(plt)
    return {'plot': plot}
```

<div style={{textAlign: 'center'}}>
![rounded rectangle](./images/draw_rounded_rectangle.png)
</div>

## Axes

### draw_two_axes

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L646C1-L755C14)

```python
draw_two_axes(
    arrow_length,
    line_thickness = 1.5,
    text_offset = 0.1,
    negative_y = False,
    negative_x = False,
    ax = None
)
```

#### Description:

Draws two axes representing the x and y directions.

#### Arguments:

| Argument             | Type         | Description                                                     |
| -------------------- | ------------ | --------------------------------------------------------------- |
| **`arrow_length`**   | **float**    | Length of the arrows representing the axes.                     |
| **`line_thickness`** | **float**    | Thickness of the arrows representing the axes. (Default is 1.5) |
| **`text_offset`**    | **float**    | Offset for the axis labels. (Default is 0.1)                    |
| **`negative_y`**     | **bool**     | Draws negative y-axis if True. (Default is False)               |
| **`negative_x`**     | **bool**     | Draws negative x-axis if True. (Default is False)               |
| **`ax`**             | **plt.Axes** | The Axes object to draw the axes on.                            |

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
    ax = plot_draw.draw_two_axes(arrow_length=1.0, negative_y=True, negative_x=True)
    plot = msc.print_plot(plt)
    return {'plot': plot}
```

<div style={{textAlign: 'center'}}>
![two axes](./images/draw_two_axes.png)
</div>

### draw_two_inclined_axes

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L758C1-L873C14)

```python
draw_two_inclined_axes(
    arrow_length,
    arrow_thickness = 2,
    text_offset = 0.1,
    negative_y = False,
    negative_x = False,
    ax = None
)
```

#### Description:

Draws two inclined axes (x and y) with optional negative directions.

#### Arguments:

| Argument              | Type                    | Description                                                                    |
| --------------------- | ----------------------- | ------------------------------------------------------------------------------ |
| **`arrow_length`**    | **float**               | The length of the arrows representing the axes.                                |
| **`arrow_thickness`** | **float** (optional)    | The thickness of the arrows. (Default is 2)                                    |
| **`text_offset`**     | **float** (optional)    | The distance between the end of the arrow and the label text. (Default is 0.1) |
| **`negative_y`**      | **bool** (optional)     | Draws negative y-axis if True. (Default is False)                              |
| **`negative_x`**      | **bool** (optional)     | Draws negative x-axis if True. (Default is False)                              |
| **`ax`**              | **plt.Axes** (optional) | The Axes object to draw the axes on. (Default is None)                         |

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
    ax = plot_draw.draw_two_inclined_axes(arrow_length=1, negative_y=True, negative_x=True)
    plot = msc.print_plot(plt)
    return {'plot': plot}
```

<div style={{textAlign: 'center'}}>
![2 inclined axes](./images/draw_two_inclined_axes.png)
</div>

### draw_three_axes

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L876C1-L1005C1)

```python
draw_three_axes(
    arrow_length,
    arrow_thickness = 2,
    text_offset = 0.1,
    negative_y = False,
    negative_x = False,
    ax = None
)
```

#### Description:

Draws a set of three axes (x, y, z) with optional negative directions for x and y.

#### Arguments:

| Argument              | Type                    | Description                                                                    |
| --------------------- | ----------------------- | ------------------------------------------------------------------------------ |
| **`arrow_length`**    | **float**               | The length of the arrows representing the axes.                                |
| **`arrow_thickness`** | **float** (optional)    | The thickness of the arrows. (Default is 2)                                    |
| **`text_offset`**     | **float** (optional)    | The distance between the end of the arrow and the label text. (Default is 0.1) |
| **`negative_y`**      | **bool** (optional)     | Draws negative y-axis if True. (Default is False)                              |
| **`negative_x`**      | **bool** (optional)     | draws negative x-axis if True. (Default is False)                              |
| **`ax`**              | **plt.Axes** (optional) | The Axes object to draw the axes on. (Default is None)                         |

#### Example:

```python
import matplotlib.pyplot as plt
import mecsimcalc as msc
import mecimcalc.plot_draw as plot_draw

def main(inputs):
    plot_draw.draw_three_axes(arrow_length=1, negative_y=True, negative_x=True)
    plot = msc.print_plot(plt)
    return {'plot': plot}
```

<div style={{textAlign: 'center'}}>
![three axes](./images/draw_three_axes.png)
</div>

### draw_three_axes_rotated

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L1007C1-L1145C14)

```python
draw_three_axes_rotated(
    arrow_length,
    line_thickness = 1.5,
    text_offset = 0.2,
    negative_y = False,
    negative_x = False,
    ax = None
)
```

#### Description:

Draws three rotated axes in a 3D coordinate system.

#### Arguments:

| Argument             | Type      | Description                                            |
| -------------------- | --------- | ------------------------------------------------------ |
| **`arrow_length`**   | **float** | The length of the arrow.                               |
| **`line_thickness`** | **float** | The thickness of the line.                             |
| **`text_offset`**    | **float** | The offset of the text from the arrow.                 |
| **`negative_y`**     | **bool**  | Whether to include negative y-axis (Default is False). |
| **`negative_x`**     | **bool**  | Whether to include negative x-axis (Default is False). |

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
    ax = plot_draw.draw_three_axes_rotated(arrow_length=1.0, negative_y=True, negative_x=True)
    plot = msc.print_plot(plt)
    return {'plot': plot}
```

<div style={{textAlign: 'center'}}>
![three axes rotated](./images/draw_three_axes_rotated.png)
</div>

## Calculations

### calculate_midpoint

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L1148C1-L1180C40)

```python
calculate_midpoint(
    coord1,
    coord2
)
```

#### Description:

Calculates the midpoint between two coordinates.

#### Arguments:

| Argument     | Type                    | Description                   |
| ------------ | ----------------------- | ----------------------------- |
| **`coord1`** | **Tuple[float, float]** | The first coordinate (x, y).  |
| **`coord2`** | **Tuple[float, float]** | The second coordinate (x, y). |

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

### calculate_intersection_point

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L1183C1-L1248C1)

```python
calculate_intersection_point(
    point1,
    angle1,
    point2,
    angle2,
    degrees = False
)
```

#### Description:

Calculates the intersection point of two lines defined by points and angles.

#### Arguments:

| Argument      | Type                | Description                                                                      |
| ------------- | ------------------- | -------------------------------------------------------------------------------- |
| **`point1`**  | **tuple**           | The coordinates of the first point (x, y) through which the first line passes.   |
| **`angle1`**  | **float**           | The angle of the first line.                                                     |
| **`point2`**  | **tuple**           | The coordinates of the second point (x, y) through which the second line passes. |
| **`angle2`**  | **float**           | The angle of the second line.                                                    |
| **`degrees`** | **bool** (optional) | Whether the angles are. (Default is False)                                       |

#### Returns:

| Return Type          | Description                                       |
| -------------------- | ------------------------------------------------- |
| **`(float, float)`** | The coordinates of the intersection point (x, y). |

#### Example:

```python
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    intersection = plot_draw.calculate_intersection_point((0, 0), 45, (1, 1), 135, degrees=True)
    return {"intersection"ersection}

# Expected output: {"intersection": (1.0, 0.9999999999999999)}
```

### calculate_arrow_endpoint

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L1249C1-L1291C1)

```python
calculate_arrow_endpoint(
    start,
    angle,
    length,
    degrees = False
)
```

#### Description:

Calculates the end point of an arrow in pixel coordinates.

#### Arguments:

| Argument      | Type      | Description                                                  |
| ------------- | --------- | ------------------------------------------------------------ |
| **`start`**   | **tuple** | The starting point of the arrow (x, y) in pixel coordinates. |
| **`angle`**   | **float** | The angle of the arrow.                                      |
| **`length`**  | **float** | The length of the arrow.                                     |
| **`degrees`** | **bool**  | Whether the angle is. (Default is False)                     |

#### Returns:

| Return Type          | Description                                             |
| -------------------- | ------------------------------------------------------- |
| **`(float, float)`** | The end point of the arrow (x, y) in pixel coordinates. |

#### Example:

```python
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    endpoint = plot_draw.calculate_arrow_endpoint((100, 200), 45, 50, degrees=True)
    return {"endpoint": endpoint}

# Expected output: {"endpoint": (135.35533905932738, 235.35533905932738)}
```

### calculate_angle

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L1293C1-L1333C1)

```python
calculate_angle(
    start: tuple,
    end: tuple,
    degrees: bool = False
)
```

#### Description:

Calculates the angle (in degrees) between two points.

#### Arguments:

| Argument      | Type      | Description                                                |
| ------------- | --------- | ---------------------------------------------------------- |
| **`start`**   | **tuple** | Tuple (x, y) representing the starting point.              |
| **`end`**     | **tuple** | Tuple (x, y) representing the final point.                 |
| **`degrees`** | **bool**  | Whether to return the angle in degrees. (Default is False) |

#### Returns:

| Return Type | Description                       |
| ----------- | --------------------------------- |
| **`float`** | The angle between the two points. |

#### Example:

```python
import mecsimcalc.plot_draw as plot_draw

def main(inputs):
    angle = plot_draw.calculate_angle(start=(0, 0), end=(1, 1), degrees=True)
    return {"angle": angle}

# Expected output: {"angle": 45.0}
```

### get_arc_points

[**[Source]**](https://github.com/MecSimCalc/MecSimCalc-utils/blob/v0.2.0/mecsimcalc/plot_draw.py#L1335C1-L1387C16)

```python
get_arc_points(
    start_angle,
    end_angle,
    radius,
    center: Union[tuple, list]
)
```

#### Description:

Calculates points along a circular arc defined by a start angle and an end angle.

#### Arguments:

| Argument          | Type                    | Description                                        |
| ----------------- | ----------------------- | -------------------------------------------------- |
| **`start_angle`** | **float**               | The starting angle of the arc.                     |
| **`end_angle`**   | **float**               | The ending angle of the arc.                       |
| **`radius`**      | **float**               | The radius of the arc.                             |
| **`center`**      | **Tuple[float, float]** | The coordinates of the center of the arc [cx, cy]. |

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
    arc_points_x1, arc_points_y1 = plot_draw.get_arc_points(90, 240, 0.25, (0, -0.25), degrees=True)
    plt.plot(arc_points_x1, arc_points_y1, 'k')
    plot = msc.print_plot(plt)
    return {'plot': plot}
```

<div style={{textAlign: 'center'}}>
![arc points](./images/get_arc_points.png)
</div>
