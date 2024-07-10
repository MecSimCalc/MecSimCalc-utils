from typing import Union, Tuple
import matplotlib.pyplot as plt
import numpy as np
import math


def draw_arrow(
    start: Union[tuple, list],
    end: Union[tuple, list],
    thickness: int = 5,
    color: str = "black",
    text: str = None,
    text_distance: float = 0.5,
    head_width: float = 0.08,
    head_length: float = 0.08,
    fontsize: int = 12,
) -> None:
    """
    >>> draw_arrow(
        start: Union[tuple, list],
        end: Union[tuple, list],
        thickness: int = 5,
        color: str = 'black',
        text: str = None,
        text_distance: float = 0.5,
        head_width: float = 0.08,
        head_length: float = 0.08,
        fontsize: int = 12
    ) -> None

    Draws an arrow between two points on a plot.

    Parameters
    ----------
    start : tuple or list
        The starting point of the arrow (x, y).
    end : tuple or list
        The ending point of the arrow (x, y).
    thickness : int, optional
        The thickness of the arrow line. (Default is 5)
    color : str, optional
        The color of the arrow. (Default is 'black')
    text : str, optional
        Text to display near the arrow. (Default is None)
    text_distance : float, optional
        Distance factor from the arrow end point where the text will be placed. (Default is 0.5)
    head_width : float, optional
        Width of the arrow head. (Default is 0.08)
    head_length : float, optional
        Length of the arrow head. (Default is 0.08)
    fontsize : int, optional
        Font size of the text. (Default is 12)

    Returns
    -------
    None

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_arrow((0, 0), (1, 1), thickness=2, color='red', text='Arrow', text_distance=0.1, head_width=0.1, head_length=0.1, fontsize=10)
    >>> plt.xlim(-1, 2)
    >>> plt.ylim(-1, 2)
    >>> plt.show()
    """
    start = np.array(start)
    end = np.array(end)
    plt.arrow(
        start[0],
        start[1],
        end[0] - start[0],
        end[1] - start[1],
        head_width=head_width,
        head_length=head_length,
        linewidth=thickness,
        color=color,
    )
    if text:
        arrow_vector = end - start
        text_position = end + text_distance * arrow_vector / np.linalg.norm(
            arrow_vector
        )
        plt.text(text_position[0], text_position[1], text, fontsize=fontsize)


def calculate_midpoint(coord1: tuple, coord2: tuple) -> tuple:
    """
    >>> calculate_midpoint(
        coord1: tuple,
        coord2: tuple
    ) -> tuple

    Calculates the midpoint between two coordinates.

    Parameters
    ----------
    coord1 : tuple
        The first coordinate (x, y).
    coord2 : tuple
        The second coordinate (x, y).

    Returns
    -------
    * `tuple` :
        The midpoint (x, y).

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> midpoint = pltdraw.calculate_midpoint((0, 0), (2, 2))
    >>> print(midpoint)
    (1.0, 1.0)
    """
    x1, y1 = coord1
    x2, y2 = coord2

    x_middle = (x1 + x2) / 2
    y_middle = (y1 + y2) / 2
    return (x_middle, y_middle)


def draw_arc_circumference(
    radius: float, initial_angle: float, final_angle: float, center: tuple = (0, 0)
) -> None:
    """
    >>> draw_arc_circumference(
        radius: float,
        initial_angle: float,
        final_angle: float,
        center: tuple = (0, 0)
    ) -> None

    Draws an arc of a circumference with a given radius between two angles.

    Parameters
    ----------
    radius : float
        The radius of the circumference.
    initial_angle : float
        The starting angle of the arc in radians.
    final_angle : float
        The ending angle of the arc in radians.
    center : tuple
        The center of the circumference.

    Returns
    -------
    None

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_arc_circumference(5, 0, np.pi/2)
    >>> plt.show()
    """
    # prevent circle from overlapping
    if abs(final_angle - initial_angle) > 2 * np.pi:
        final_angle = 2 * np.pi
        initial_angle = 0

    angles = np.linspace(initial_angle, final_angle, 200)
    x = radius * np.cos(angles) + center[0]
    y = radius * np.sin(angles) + center[1]
    plt.plot(x, y, color="red")
    plt.axis("equal")


def create_blank_image(width: int = 1000, height: int = 1000) -> plt.Axes:
    """
    >>> create_blank_image(
        width: int = 1000,
        height: int = 1000
    ) -> plt.Axes

    Creates a blank image with specified width and height, displaying a grid.

    Parameters
    ----------
    width : int, optional
        The width of the image in pixels. (Default is 1000)
    height : int, optional
        The height of the image in pixels. (Default is 1000)

    Returns
    -------
    * `plt.Axes` :
        The Axes object of the created blank image.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> ax = pltdraw.create_blank_image(800, 600)
    >>> plt.show()
    """
    fig, ax = plt.subplots(figsize=(int(width / 1000 * 6), int(height / 1000 * 6)))
    plt.imshow(np.ones((height, width, 3)))
    plt.tick_params(
        axis="both",
        which="both",
        bottom=False,
        top=False,
        left=False,
        right=False,
        labelbottom=False,
        labelleft=False,
    )
    plt.grid(True, alpha=0.5)
    ax.minorticks_on()
    ax.grid(which="minor", linestyle=":", linewidth="0.5", color="gray")
    return ax


def draw_three_axes(
    arrow_length: float,
    arrow_thickness: float,
    offset_text: float,
    longx: float,
    axis_y_negative: bool,
    axis_x_negative: bool,
) -> plt.Axes:
    """
    >>> draw_three_axes(
        arrow_length: float,
        arrow_thickness: float,
        offset_text: float,
        longx: float,
        axis_y_negative: bool,
        axis_x_negative: bool
    ) -> plt.Axes

    Draws a set of three axes (x, y, z) with optional negative directions for x and y.

    Parameters
    ----------
    arrow_length : float
        The length of the arrows representing the axes.
    arrow_thickness : float
        The thickness of the arrows.
    offset_text : float
        The distance between the end of the arrow and the label text.
    longx : float
        The factor to adjust the length of the diagonal x-axis.
    axis_y_negative : bool
        Whether to draw the negative y-axis.
    axis_x_negative : bool
        Whether to draw the negative x-axis.

    Returns
    -------
    * `plt.Axes` :
        The Axes object with the drawn axes.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> ax = pltdraw.draw_three_axes(arrow_length=1, arrow_thickness=2, offset_text=0.1, longx=1.5, axis_y_negative=True, axis_x_negative=True)
    >>> plt.show()
    """
    fig, ax = plt.subplots()
    ax.arrow(
        0,
        0,
        0,
        arrow_length,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=arrow_thickness,
    )
    ax.text(0, arrow_length + offset_text, "z", fontsize=12, ha="center", va="bottom")

    ax.arrow(
        0,
        0,
        arrow_length,
        0,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=arrow_thickness,
    )
    ax.text(arrow_length + offset_text, 0, "y", fontsize=12, ha="left", va="center")

    if axis_y_negative:
        ax.arrow(
            0,
            0,
            -arrow_length,
            0,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=arrow_thickness,
        )

    ax.arrow(
        0,
        0,
        -arrow_length / longx,
        -arrow_length / longx,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=arrow_thickness,
    )
    ax.text(
        -arrow_length / longx - offset_text / 1.5,
        -arrow_length / longx - offset_text / 1.5,
        "x",
        fontsize=12,
        ha="right",
        va="top",
    )

    if axis_x_negative:
        ax.arrow(
            0,
            0,
            arrow_length / longx,
            arrow_length / longx,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=arrow_thickness,
        )

    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    plt.axis("equal")
    return ax


def draw_two_inclined_axes(
    arrow_length: float,
    arrow_thickness: float,
    offset_text: float,
    longx: float,
    axis_y_negative: bool,
    axis_x_negative: bool,
) -> plt.Axes:
    """
    >>> draw_two_inclined_axes(
        arrow_length: float,
        arrow_thickness: float,
        offset_text: float,
        longx: float,
        axis_y_negative: bool,
        axis_x_negative: bool
    ) -> plt.Axes

    Draws two inclined axes (x and y) with optional negative directions.

    Parameters
    ----------
    arrow_length : float
        The length of the arrows representing the axes.
    arrow_thickness : float
        The thickness of the arrows.
    offset_text : float
        The distance between the end of the arrow and the label text.
    longx : float
        The factor to adjust the length of the diagonal y-axis.
    axis_y_negative : bool
        Whether to draw the negative y-axis.
    axis_x_negative : bool
        Whether to draw the negative x-axis.

    Returns
    -------
    * `plt.Axes` :
        The Axes object with the drawn axes.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> ax = pltdraw.draw_two_inclined_axes(arrow_length=1, arrow_thickness=2, offset_text=0.1, longx=1.5, axis_y_negative=True, axis_x_negative=True)
    >>> plt.show()
    """
    fig, ax = plt.subplots()
    ax.arrow(
        0,
        0,
        arrow_length,
        0,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=arrow_thickness,
    )
    ax.text(arrow_length + offset_text, 0, "x", fontsize=12, ha="left", va="center")

    if axis_x_negative:
        ax.arrow(
            0,
            0,
            -arrow_length,
            0,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=arrow_thickness,
        )

    ax.arrow(
        0,
        0,
        arrow_length / longx,
        arrow_length / longx,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=arrow_thickness,
    )
    ax.text(
        arrow_length / longx + offset_text / 1.5,
        arrow_length / longx + offset_text / 1.5,
        "y",
        fontsize=12,
        ha="left",
        va="bottom",
    )

    if axis_y_negative:
        ax.arrow(
            0,
            0,
            -arrow_length / longx,
            -arrow_length / longx,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=arrow_thickness,
        )

    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    plt.axis("equal")
    return ax


def plot_segment_pixels(
    start_point_pixels: tuple,
    end_point_pixels: tuple,
    line_properties: dict = {"color": "k", "linewidth": 1, "linestyle": "dashed"},
    text: str = "",
    min_spacing: float = 150,
    fontsize: int = 15,
    text_loc: dict = {"ha": "center", "va": "top"},
    alpha: float = 0.8,
) -> tuple:
    """
    >>> plot_segment_pixels(
        start_point_pixels: tuple,
        end_point_pixels: tuple,
        line_properties: dict = {'color': 'k', 'linewidth': 1, 'linestyle': 'dashed'},
        text: str = "",
        min_spacing: float = 150,
        fontsize: int = 15,
        text_loc: dict = {'ha': 'center', 'va': 'top'},
        alpha: float = 0.8
    ) -> tuple

    Plots a line segment between two points and adds a label at the end point.

    Parameters
    ----------
    start_point_pixels : tuple
        The starting point of the line segment (x, y).
    end_point_pixels : tuple
        The ending point of the line segment (x, y).
    line_properties : dict, optional
        Properties for the line, including color, linewidth, and linestyle.
    text : str, optional
        The text to display near the end point of the line segment.
    min_spacing : float, optional
        Minimum spacing for the text from the end point.
    fontsize : int, optional
        Font size of the text.
    text_loc : dict, optional
        Dictionary specifying horizontal and vertical alignment of the text.
    alpha : float, optional
        Transparency level of the line segment.

    Returns
    -------
    * `tuple` :
        The end point of the line segment (x, y).

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> start = (100, 200)
    >>> end = (400, 500)
    >>> pltdraw.plot_segment_pixels(start, end, text="Segment", min_spacing=50)
    (400, 500)
    >>> plt.show()
    """
    plt.plot(
        [start_point_pixels[0], end_point_pixels[0]],
        [start_point_pixels[1], end_point_pixels[1]],
        **line_properties,
        alpha=alpha,
    )
    mid_point = (
        (start_point_pixels[0] + end_point_pixels[0]) / 2,
        (start_point_pixels[1] + end_point_pixels[1]) / 2,
    )
    space = max(
        0.1
        * (
            (end_point_pixels[0] - start_point_pixels[0]) ** 2
            + (end_point_pixels[1] - start_point_pixels[1]) ** 2
        )
        ** 0.5,
        min_spacing,
    )
    plt.text(
        end_point_pixels[0] + space,
        end_point_pixels[1] + space,
        text,
        fontsize=fontsize,
        color="k",
        **text_loc,
    )
    return end_point_pixels


def plot_annotate_arrow(
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
        "ec": "black",
    },
    reverse_arrow: str = "no",
    text_in_center: str = "no",
    rev_text: str = "no",
    alpha: float = 0.8,
) -> tuple:
    """
    >>> plot_annotate_arrow(
        start_point: tuple,
        trig_angle: float,
        vec_length: float,
        text: str = "",
        min_spacing: float = 150,
        fontsize: int = 11,
        text_loc: dict = {'ha': 'center', 'va': 'top'},
        arrow_properties: dict = {'width': 2, 'head_width': 15, 'head_length': 15, 'fc': 'black', 'ec': 'black'},
        reverse_arrow: str = 'no',
        text_in_center: str = 'no',
        rev_text: str = 'no',
        alpha: float = 0.8
    ) -> tuple

    Plots an annotated arrow starting from a given point and extending in a given direction.

    Parameters
    ----------
    start_point : tuple
        The starting point of the arrow (x, y).
    trig_angle : float
        The angle of the arrow in degrees.
    vec_length : float
        The length of the arrow.
    text : str, optional
        The text to display near the arrow.
    min_spacing : float, optional
        Minimum spacing for the text from the end of the arrow.
    fontsize : int, optional
        Font size of the text.
    text_loc : dict, optional
        Dictionary specifying horizontal and vertical alignment of the text.
    arrow_properties : dict, optional
        Properties for the arrow, including width, head_width, head_length, fill color (fc), and edge color (ec).
    reverse_arrow : str, optional
        Whether to reverse the direction of the arrow. (Default is 'no')
    text_in_center : str, optional
        Whether to place the text in the center of the arrow. (Default is 'no')
    rev_text : str, optional
        Whether to reverse the text orientation. (Default is 'no')
    alpha : float, optional
        Transparency level of the arrow.

    Returns
    -------
    * `tuple` :
        The end point of the arrow (x, y).

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> start = (100, 200)
    >>> angle = 45
    >>> length = 100
    >>> pltdraw.plot_annotate_arrow(start, angle, length, text="Arrow", min_spacing=50)
    (170.71067811865476, 270.71067811865476)
    >>> plt.show()
    """
    trig_angle = trig_angle if trig_angle > 0 else 360 + trig_angle

    end_point = (
        start_point[0]
        + (vec_length - arrow_properties["head_length"])
        * np.cos(np.radians(trig_angle)),
        start_point[1]
        + (vec_length - arrow_properties["head_length"])
        * np.sin(np.radians(trig_angle)),
    )
    if reverse_arrow == "no":
        plt.arrow(
            *start_point,
            *(end_point[0] - start_point[0], end_point[1] - start_point[1]),
            **arrow_properties,
            alpha=alpha,
        )
    else:
        end_point = (
            start_point[0] + vec_length * np.cos(np.radians(trig_angle)),
            start_point[1] + vec_length * np.sin(np.radians(trig_angle)),
        )
        start_point = (
            start_point[0] + 0 * np.cos(np.radians(trig_angle)),
            start_point[1] + 0 * np.sin(np.radians(trig_angle)),
        )
        plt.arrow(
            *end_point,
            *(start_point[0] - end_point[0], start_point[1] - end_point[1]),
            **arrow_properties,
            alpha=alpha,
        )

    mid_point = (
        start_point[0] + 0.5 * vec_length * np.cos(np.radians(trig_angle)),
        start_point[1] + 0.5 * vec_length * np.sin(np.radians(trig_angle)),
    )
    if text_in_center == "no":
        space = max(0.1 * vec_length, min_spacing)
        plt.text(
            end_point[0] + space * np.cos(np.radians(trig_angle)),
            end_point[1] + space * np.sin(np.radians(trig_angle)),
            text,
            fontsize=fontsize,
            color="k",
            **text_loc,
        )
    else:
        rot_angle = -trig_angle if trig_angle < 90 else (180 - trig_angle)
        rot_angle = rot_angle if rev_text == "no" else rot_angle + 180
        plt.text(
            mid_point[0] + min_spacing * np.cos(np.radians(90 + trig_angle)),
            mid_point[1] + min_spacing * np.sin(np.radians(90 + trig_angle)),
            text,
            fontsize=fontsize,
            color="k",
            **text_loc,
            rotation=rot_angle,
        )

    end_point = (
        start_point[0] + vec_length * np.cos(np.radians(trig_angle)),
        start_point[1] + vec_length * np.sin(np.radians(trig_angle)),
    )
    
    return end_point


def draw_custom_arrow(
    ax: plt.Axes,
    start_point: tuple,
    point_2: tuple,
    factor: float,
    max_value: float,
    arrow_vector_length: float,
    arrow_width: float,
    arrow_color: str = "blue",
    line_width: float = 1,
    text: str = None,
) -> None:
    """
    >>> draw_custom_arrow(
        ax: plt.Axes,
        start_point: tuple,
        point_2: tuple,
        factor: float,
        max_value: float,
        arrow_vector_length: float,
        arrow_width: float,
        arrow_color: str = 'blue',
        line_width: float = 1,
        text: str = None
    ) -> None

    Draws a custom arrow from a start point to another point on a given axis, using pixel-based parameters.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes object to draw the arrow on.
    start_point : tuple
        The starting point of the arrow (x, y) in pixels.
    point_2 : tuple
        The end point of the arrow (x, y) in pixels.
    factor : float
        A factor to adjust the position of the text relative to the arrow.
    max_value : float
        The maximum value for scaling the arrow length.
    arrow_vector_length : float
        The length of the arrow vector.
    arrow_width : float
        The width of the arrow head in pixels.
    arrow_color : str, optional
        The color of the arrow. (Default is 'blue')
    line_width : float, optional
        The width of the arrow line. (Default is 1)
    text : str, optional
        The text to display near the end of the arrow.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> fig, ax = plt.subplots()
    >>> pltdraw.draw_custom_arrow(ax, (0, 0), (100, 100), factor=0.5, max_value=100, arrow_vector_length=50, arrow_width=5, text="Custom Arrow")
    >>> plt.show()
    """
    start_point = np.array(start_point)
    point_2 = np.array(point_2)
    arrow_vector = point_2 - start_point
    arrow_direction = arrow_vector * arrow_vector_length / (max_value * 2)
    arrow_end = start_point + arrow_direction
    text_offset = arrow_direction * factor
    ax.arrow(
        start_point[0],
        start_point[1],
        arrow_direction[0],
        arrow_direction[1],
        head_width=arrow_width,
        head_length=arrow_width * 2,
        fc=arrow_color,
        ec=arrow_color,
        lw=line_width,
    )
    if text:
        ax.text(
            arrow_end[0] + text_offset[0],
            arrow_end[1] + text_offset[1],
            f"${text}$",
            fontsize=12,
            ha="center",
            va="top",
        )


def calculate_arrow_endpoint_pixels(
    start_point: tuple, trig_angle: float, vec_length: float
) -> tuple:
    """
    >>> calculate_arrow_endpoint_pixels(
        start_point: tuple,
        trig_angle: float,
        vec_length: float
    ) -> tuple

    Calculates the end point of an arrow in pixel coordinates.

    Parameters
    ----------
    start_point : tuple
        The starting point of the arrow (x, y) in pixel coordinates.
    trig_angle : float
        The angle of the arrow in degrees.
    vec_length : float
        The length of the arrow.

    Returns
    -------
    * `tuple` :
        The end point of the arrow (x, y) in pixel coordinates.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.calculate_arrow_endpoint_pixels((100, 200), 45, 50)
    (135.35533905932738, 235.35533905932738)
    """
    trig_angle = trig_angle if trig_angle > 0 else 360 + trig_angle
    return start_point[0] + vec_length * np.cos(np.radians(trig_angle)), start_point[
        1
    ] + vec_length * np.sin(np.radians(trig_angle))


def plot_segment(
    start_point: tuple,
    trig_angle: float,
    vec_length: float,
    line_properties: dict = {"color": "blue", "linewidth": 1},
    text: str = "",
    min_spacing: float = 150,
    fontsize: int = 15,
    text_loc: dict = {"ha": "center", "va": "top"},
    alpha: float = 0.8,
) -> tuple:
    """
    >>> plot_segment(
        start_point: tuple,
        trig_angle: float,
        vec_length: float,
        line_properties: dict = {'color': 'blue', 'linewidth': 1},
        text: str = "",
        min_spacing: float = 150,
        fontsize: int = 15,
        text_loc: dict = {'ha': 'center', 'va': 'top'},
        alpha: float = 0.8
    ) -> tuple

    Plots a line segment starting from a given point with a specific angle and length.

    Parameters
    ----------
    start_point : tuple
        The starting point of the line segment (x, y).
    trig_angle : float
        The angle of the line segment in degrees.
    vec_length : float
        The length of the line segment.
    line_properties : dict, optional
        Properties of the line segment such as color and linewidth.
    text : str, optional
        The text to display near the end of the line segment.
    min_spacing : float, optional
        Minimum spacing between the end of the line segment and the text.
    fontsize : int, optional
        The font size of the text.
    text_loc : dict, optional
        Location parameters for the text.
    alpha : float, optional
        The alpha value for transparency.

    Returns
    -------
    * `tuple` :
        The end point of the line segment (x, y).

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.plot_segment((100, 200), 45, 50, text='Value')
    (135.35533905932738, 235.35533905932738)
    >>> plt.show()
    """
    trig_angle = trig_angle if trig_angle > 0 else 360 + trig_angle
    end_point = (
        start_point[0] + vec_length * np.cos(np.radians(trig_angle)),
        start_point[1] + vec_length * np.sin(np.radians(trig_angle)),
    )
    plt.plot(
        [start_point[0], end_point[0]],
        [start_point[1], end_point[1]],
        **line_properties,
        alpha=alpha,
    )

    mid_point = (
        start_point[0] + 0.5 * vec_length * np.cos(np.radians(trig_angle)),
        start_point[1] + 0.5 * vec_length * np.sin(np.radians(trig_angle)),
    )
    space = max(0.1 * vec_length, min_spacing)
    plt.text(
        end_point[0] + space * np.cos(np.radians(trig_angle)),
        end_point[1] + space * np.sin(np.radians(trig_angle)),
        text,
        fontsize=fontsize,
        color="k",
        **text_loc,
    )

    return end_point


def plot_segment_dashed(
    start_point: tuple,
    trig_angle: float,
    vec_length: float,
    line_properties: dict = {"color": "blue", "linestyle": "dashed", "linewidth": 1},
    text: str = "",
    min_spacing: float = 150,
    fontsize: int = 15,
    text_loc: dict = {"ha": "center", "va": "top"},
    alpha: float = 0.8,
) -> tuple:
    """
    >>> plot_segment_dashed(
        start_point: tuple,
        trig_angle: float,
        vec_length: float,
        line_properties: dict = {'color': 'blue', 'linestyle': 'dashed', 'linewidth': 1},
        text: str = "",
        min_spacing: float = 150,
        fontsize: int = 15,
        text_loc: dict = {'ha': 'center', 'va': 'top'},
        alpha: float = 0.8
    ) -> tuple

    Plots a dashed line segment starting from a given point with a specific angle and length.

    Parameters
    ----------
    start_point : tuple
        The starting point of the line segment (x, y).
    trig_angle : float
        The angle of the line segment in degrees.
    vec_length : float
        The length of the line segment.
    line_properties : dict, optional
        Properties of the line segment such as color and linewidth.
    text : str, optional
        The text to display near the end of the line segment.
    min_spacing : float, optional
        Minimum spacing between the end of the line segment and the text.
    fontsize : int, optional
        The font size of the text.
    text_loc : dict, optional
        Location parameters for the text.
    alpha : float, optional
        The alpha value for transparency.

    Returns
    -------
    * `tuple` :
        The end point of the line segment (x, y).

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.plot_segment_dashed((100, 200), 45, 50, text='Value')
    (135.35533905932738, 235.35533905932738)
    >>> plt.show()
    """
    trig_angle = trig_angle if trig_angle > 0 else 360 + trig_angle
    end_point = (
        start_point[0] + vec_length * np.cos(np.radians(trig_angle)),
        start_point[1] + vec_length * np.sin(np.radians(trig_angle)),
    )
    plt.plot(
        [start_point[0], end_point[0]],
        [start_point[1], end_point[1]],
        **line_properties,
        alpha=alpha,
    )

    mid_point = (
        start_point[0] + 0.5 * vec_length * np.cos(np.radians(trig_angle)),
        start_point[1] + 0.5 * vec_length * np.sin(np.radians(trig_angle)),
    )
    if text:
        space = max(0.1 * vec_length, min_spacing)
        plt.text(
            end_point[0] + space * np.cos(np.radians(trig_angle)),
            end_point[1] + space * np.sin(np.radians(trig_angle)),
            text,
            fontsize=fontsize,
            color="k",
            **text_loc,
        )

    return end_point


def draw_custom_circle(
    ax: plt.Axes,
    center_point: tuple,
    circle_size: float = 100,
    circle_color: str = "black",
) -> None:
    """
    >>> draw_custom_circle(
        ax: plt.Axes,
        center_point: tuple,
        circle_size: float = 100,
        circle_color: str = 'black'
    ) -> None

    Draws a custom circle on a given axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The Axes object to draw the circle on.
    center_point : tuple
        The center point of the circle (x, y).
    circle_size : float, optional
        The size of the circle. (Default is 100)
    circle_color : str, optional
        The color of the circle. (Default is 'black')

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> fig, ax = plt.subplots()
    >>> pltdraw.draw_custom_circle(ax, (100, 100), circle_size=200, circle_color='red')
    >>> plt.show()
    """
    ax.scatter(center_point[0], center_point[1], s=circle_size, color=circle_color)


def draw_rounded_rectangle(
    middle_point: tuple,
    width: float,
    height: float,
    radius: float,
    color: str = "black",
) -> None:
    """
    >>> draw_rounded_rectangle(
        middle_point: tuple,
        width: float,
        height: float,
        radius: float,
        color: str = 'black'
    ) -> None

    Draws a rounded rectangle with specified properties.

    Parameters
    ----------
    middle_point : tuple
        The middle point of the top side of the rounded rectangle (x, y).
    width : float
        The width of the rounded rectangle.
    height : float
        The height of the rounded rectangle.
    radius : float
        The radius of the corners.
    color : str, optional
        The color of the rectangle. (Default is 'black')

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_rounded_rectangle((0, 0), 4, 2, 0.5, color='blue')
    >>> plt.show()
    """
    x_sup, y_sup = middle_point
    x1 = x_sup - width / 2
    y1 = y_sup
    x2 = x_sup + width / 2
    y2 = y_sup
    x3 = x_sup + width / 2
    y3 = y_sup + height
    x4 = x_sup - width / 2
    y4 = y_sup + height

    plt.plot([x1 + radius, x2 - radius], [y1, y2], color=color)
    plt.plot([x2, x3], [y2 + radius, y3 - radius], color=color)
    plt.plot([x3 - radius, x4 + radius], [y3, y4], color=color)
    plt.plot([x4, x1], [y4 - radius, y1 + radius], color=color)

    angle1 = np.linspace(np.pi, 1.5 * np.pi, 50)
    angle2 = np.linspace(1.5 * np.pi, 2 * np.pi, 50)
    plt.plot(
        x1 + radius + radius * np.cos(angle1),
        y1 + radius + radius * np.sin(angle1),
        color=color,
    )  # top left  (sup izq)

    plt.plot(
        x2 - radius + radius * np.cos(angle2),
        y2 + radius + radius * np.sin(angle2),
        color=color,
    )  # top right (sup der)

    plt.plot(
        x3 - radius - radius * np.cos(angle1),
        y3 - radius - radius * np.sin(angle1),
        color=color,
    )  # bottom right (inf der)

    plt.plot(
        x4 + radius - radius * np.cos(angle2),
        y4 - radius - radius * np.sin(angle2),
        color=color,
    )  # bottom left  (inf izq)


def calculate_intersection_point(
    point1: tuple, angle1: float, point2: tuple, angle2: float
) -> Tuple[float, float]:
    """
    >>> calculate_intersection_point(
        point1: tuple,
        angle1: float,
        point2: tuple,
        angle2: float,
    ) -> tuple

    Calculates the intersection point of two lines defined by points and angles.

    Parameters
    ----------
    point1 : tuple
        The coordinates of the first point (x, y) through which the first line passes.
    angle1 : float
        The angle of the first line in degrees.
    point2 : tuple
        The coordinates of the second point (x, y) through which the second line passes.
    angle2 : float
        The angle of the second line in degrees.

    Returns
    -------
    * `tuple` :
        The coordinates of the intersection point (x, y). (None, None) if the lines are parallel.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.calculate_intersection_point((0, 0), 45, (1, 1), 135)
    (1.0, 0.9999999999999999)
    """
    # Convert angles to radians
    angle1_rad = np.radians(angle1)
    angle2_rad = np.radians(angle2)
    
    x1, y1 = point1
    x2, y2 = point2
    
    # Calculate the slopes of the lines
    m1 = np.tan(angle1_rad)
    m2 = np.tan(angle2_rad)
    
    # lines are parallel so they don't intersect
    if m1 == m2:
        return None, None
    
    b1 = y1 - m1 * x1
    b2 = y2 - m2 * x2
    
    intersection_x = (b2 - b1) / (m1 - m2)
    intersection_y = m1 * intersection_x + b1
    
    return (intersection_x, intersection_y)


def draw_segment(
    start_point: tuple,
    final_point: tuple,
    line_width: float = 0.001,
    color: str = "black",
) -> None:
    """
    >>> draw_segment(
        start_point: tuple,
        final_point: tuple,
        line_width: float = 0.001,
        color: str = 'black'
    ) -> None

    Draws a segment between two points with a specified line width and color.

    Parameters
    ----------
    start_point : tuple
        The coordinates of the starting point (x, y).
    final_point : tuple
        The coordinates of the final point (x, y).
    line_width : float, optional
        The width of the segment. (Default is 0.001)
    color : str, optional
        The color of the segment. (Default is 'black')

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_segment((0, 0), (1, 1), line_width=0.005, color='blue')
    >>> plt.show()
    """
    x_start, y_start = start_point
    x_end, y_end = final_point
    angle = np.arctan2(y_end - y_start, y_end - x_start)
    offset_x = np.sin(angle) * line_width / 2
    offset_y = np.cos(angle) * line_width / 2
    x1 = x_start + offset_x
    y1 = y_start - offset_y
    x2 = x_start - offset_x
    y2 = y_start + offset_y
    x3 = x_end - offset_x
    y3 = y_end + offset_y
    x4 = x_end + offset_x
    y4 = y_end - offset_y
    plt.fill([x1, x2, x3, x4, x1], [y1, y2, y3, y4, y1], color=color)


def plot_annotate_arrow_end(
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
        "ec": "black",
    },
    reverse_arrow: str = "no",
    text_in_center: str = "no",
    rev_text: str = "no",
    alpha: float = 0.8
) -> tuple:
    """
    >>> plot_annotate_arrow_end(
        end_point: tuple,
        trig_angle: float,
        vec_length: float,
        text: str = "",
        text_distance: float = 0.5,
        fontsize: int = 12,
        text_loc: dict = {'ha': 'center', 'va': 'top'},
        arrow_properties: dict = {'width': 2, 'head_width': 15, 'head_length': 15, 'fc': 'black', 'ec': 'black'},
        reverse_arrow: str = 'no',
        text_in_center: str = 'no',
        rev_text: str = 'no',
        alpha: float = 0.8
    ) -> tuple

    Plots an arrow annotation at the end point of a vector.

    Parameters
    ----------
    end_point : tuple
        The coordinates of the end point (x, y) of the vector.
    trig_angle : float
        The trigonometric angle of the vector in degrees.
    vec_length : float
        The length of the vector.
    text : str, optional
        The text to be displayed near the arrow. (Default is "")
    text_distance : float, optional
        The distance between the text and the arrow. (Default is 0.5)
    fontsize : int, optional
        The font size of the text. (Default is 12)
    text_loc : dict, optional
        The text alignment. (Default is {'ha': 'center', 'va': 'top'})
    arrow_properties : dict, optional
        The properties of the arrow. (Default is {'width': 2, 'head_width': 15, 'head_length': 15, 'fc': 'black', 'ec': 'black'})
    reverse_arrow : str, optional
        Whether to reverse the arrow. (Default is 'no')
    text_in_center : str, optional
        Whether to place the text in the center. (Default is 'no')
    rev_text : str, optional
        Whether to reverse the text. (Default is 'no')
    alpha : float, optional
        The transparency of the arrow and text. (Default is 0.8)\

    Returns
    -------
    * `tuple` :
        The coordinates of the start point (x, y) of the arrow.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.plot_annotate_arrow_end((1, 1), 45, 1, text="End", text_distance=0.5, fontsize=12, text_loc={'ha': 'center', 'va': 'top'})
    (10.899494936611665, 10.899494936611665)
    >>> plt.show()
    """
    trig_angle = trig_angle if trig_angle > 0 else 360 + trig_angle

    start_point = (
        end_point[0]
        - (vec_length - arrow_properties["head_length"])
        * np.cos(np.radians(trig_angle)),
        end_point[1]
        - (vec_length - arrow_properties["head_length"])
        * np.sin(np.radians(trig_angle)),
    )
    if reverse_arrow == "no":
        plt.arrow(
            *start_point,
            *(end_point[0] - start_point[0], end_point[1] - start_point[1]),
            **arrow_properties,
            alpha=alpha,
        )
    else:
        start_point = (
            end_point[0] - vec_length * np.cos(np.radians(trig_angle)),
            end_point[1] - vec_length * np.sin(np.radians(trig_angle)),
        )
        end_point = (
            end_point[0] - 0 * np.cos(np.radians(trig_angle)),
            end_point[1] - 0 * np.sin(np.radians(trig_angle)),
        )
        plt.arrow(
            *end_point,
            *(start_point[0] - end_point[0], start_point[1] - end_point[1]),
            **arrow_properties,
            alpha=alpha,
        )

    mid_point = (
        start_point[0] + 0.5 * vec_length * np.cos(np.radians(trig_angle)),
        start_point[1] + 0.5 * vec_length * np.sin(np.radians(trig_angle)),
    )
    if text_in_center == "no":
        plt.text(
            start_point[0] - text_distance * np.cos(np.radians(trig_angle)),
            start_point[1] - text_distance * np.sin(np.radians(trig_angle)),
            text,
            fontsize=fontsize,
            color="k",
            **text_loc,
        )
    else:
        rot_angle = -trig_angle if trig_angle < 90 else (180 - trig_angle)
        rot_angle = rot_angle if rev_text == "no" else rot_angle + 180
        plt.text(
            mid_point[0] + text_distance * np.cos(np.radians(90 + trig_angle)),
            mid_point[1] + text_distance * np.sin(np.radians(90 + trig_angle)),
            text,
            fontsize=fontsize,
            color="k",
            **text_loc,
            rotation=rot_angle,
        )
    
    return start_point


def draw_arc_with_text(
    start_point: tuple, radius: float, start_angle: float, final_angle: float, text: str
) -> None:
    """
    >>> draw_arc_with_text(
        start_point: tuple,
        radius: float,
        start_angle: float,
        final_angle: float,
        text: str
    ) -> None

    Draws an arc with text annotation.

    Parameters
    ----------
    start_point : tuple
        The coordinates (x, y) of the center point of the circle from which the arc is drawn.
    radius : float
        The radius of the arc.
    start_angle : float
        The start angle of the arc in degrees.
    final_angle : float
        The final angle of the arc in degrees.
    text : str
        The text to be displayed along the arc.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_arc_with_text((0, 0), 5, 30, 120, "Sample Text")
    >>> plt.show()
    """
    angles = np.linspace(np.radians(start_angle), np.radians(final_angle), 1000)
    x = start_point[0] + radius * np.cos(angles)
    y = start_point[1] + radius * np.sin(angles)
    plt.plot(x, y, color="black", linewidth=1)
    middle_point_x = start_point[0] + radius * np.cos(
        (np.radians(start_angle) + np.radians(final_angle)) / 2
    )
    middle_point_y = start_point[1] + radius * np.sin(
        (np.radians(start_angle) + np.radians(final_angle)) / 2
    )
    displacement_x = (
        np.cos((np.radians(start_angle) + np.radians(final_angle)) / 2) * radius * 0.7
    )
    displacement_y = (
        np.sin((np.radians(start_angle) + np.radians(final_angle)) / 2) * radius * 0.6
    )
    plt.text(
        middle_point_x + displacement_x,
        middle_point_y + displacement_y,
        text,
        fontsize=8,
        ha="center",
        va="center",
    )
    plt.axis("equal")


def draw_three_axes_rotated(
    arrow_length: float,
    line_thickness: float,
    offset_text: float,
    longx: float,
    negativeaxis_y: int,
    negativeaxis_x: int,
) -> plt.Axes:
    """
    >>> draw_three_axes_rotated(
        arrow_length: float,
        line_thickness: float,
        offset_text: float,
        longx: float,
        negativeaxis_y: int,
        negativeaxis_x: int
    ) -> plt.Axes

    Draws three rotated axes in a 3D coordinate system.

    Parameters
    ----------
    arrow_length : float
        The length of the arrow.
    line_thickness : float
        The thickness of the line.
    offset_text : float
        The offset of the text from the arrow.
    longx : float
        The length of the x-axis.
    negativeaxis_y : int
        Whether to include negative y-axis (1 for yes, 0 for no).
    negativeaxis_x : int
        Whether to include negative x-axis (1 for yes, 0 for no).

    Returns
    -------
    * `plt.Axes` :
        The matplotlib Axes object containing the plot.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> ax = pltdraw.draw_three_axes_rotated(arrow_length=1.0, line_thickness=1.5, offset_text=0.1, longx=1.5, negativeaxis_y=1, negativeaxis_x=1)
    >>> plt.show()
    """
    fig, ax = plt.subplots()
    ax.arrow(
        0,
        0,
        0,
        arrow_length,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=line_thickness,
    )
    ax.text(0, arrow_length + offset_text, "z", fontsize=12, ha="center", va="bottom")

    ax.arrow(
        0,
        0,
        -arrow_length * np.cos(np.radians(30)) / longx,
        -arrow_length * np.sin(np.radians(30)) / longx,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=line_thickness,
    )
    ax.text(
        -arrow_length * np.cos(np.radians(30)) / longx - offset_text,
        -arrow_length * np.sin(np.radians(30)) / longx - offset_text,
        "x",
        fontsize=12,
        ha="left",
        va="center",
    )

    if negativeaxis_x == 1:
        ax.arrow(
            0,
            0,
            arrow_length * np.cos(np.radians(30)) / longx,
            arrow_length * np.sin(np.radians(30)) / longx,
            head_width=0,
            head_length=0,
            fc="gray",
            ec="gray",
            lw=line_thickness,
        )
        ax.arrow(
            0,
            0,
            arrow_length * np.cos(np.radians(30)) / longx,
            -arrow_length * np.sin(np.radians(30)) / longx,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=line_thickness,
        )
        ax.text(
            arrow_length * np.cos(np.radians(30)) / longx + 2 * offset_text / 1.5,
            -arrow_length * np.sin(np.radians(30)) / longx - offset_text / 1.5,
            "y",
            fontsize=12,
            ha="right",
            va="top",
        )

    if negativeaxis_y == 1:
        ax.arrow(
            0,
            0,
            -arrow_length * np.cos(np.radians(30)) / longx,
            arrow_length * np.sin(np.radians(30)) / longx,
            head_width=0,
            head_length=0,
            fc="gray",
            ec="gray",
            lw=line_thickness,
        )

    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    plt.axis("equal")
    return ax


def draw_double_arrowhead(
    start_point: tuple,
    end_point: tuple,
    color: str = "black",
    line_thickness: float = 1,
) -> None:
    """
    >>> draw_double_arrowhead(
        start_point: tuple,
        end_point: tuple,
        color: str = 'black',
        line_thickness: float = 1
    ) -> None

    Draws a double arrowhead between two points.

    Parameters
    ----------
    start_point : tuple
        Coordinates of the start point (x, y).
    end_point : tuple
        Coordinates of the end point (x, y).
    color : str, optional
        Color of the arrow and line. (Default is 'black')
    line_thickness : float, optional
        Thickness of the line. (Default is 1)

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_double_arrowhead(start_point=(0, 0), end_point=(1, 1), color='black', line_thickness=1)
    >>> plt.show()
    """
    start_point = list(start_point)
    end_point = list(end_point)
    modified_start = start_point.copy()
    modified_end = end_point.copy()
    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]
    modified_start[0] += 0.08 * dx / ((dx**2 + dy**2) ** 0.5)
    modified_start[1] += 0.08 * dy / ((dx**2 + dy**2) ** 0.5)
    modified_end[0] -= 0.08 * dx / ((dx**2 + dy**2) ** 0.5)
    modified_end[1] -= 0.08 * dy / ((dx**2 + dy**2) ** 0.5)
    dx = modified_end[0] - modified_start[0]
    dy = modified_end[1] - modified_start[1]
    plt.plot(
        [start_point[0], end_point[0]],
        [start_point[1], end_point[1]],
        color=color,
        linewidth=line_thickness,
    )
    plt.arrow(
        modified_start[0],
        modified_start[1],
        dx,
        dy,
        head_width=0.05,
        head_length=0.08,
        color=color,
        linewidth=line_thickness,
    )
    plt.arrow(
        modified_end[0],
        modified_end[1],
        -dx,
        -dy,
        head_width=0.05,
        head_length=0.08,
        color=color,
        linewidth=line_thickness,
    )


def draw_custom_arrow_end(
    start_point: tuple,
    end_point: tuple,
    color: str = "black",
    line_thickness: float = 1,
) -> None:
    """
    >>> draw_custom_arrow_end(
        start_point: tuple,
        end_point: tuple,
        color: str = 'black',
        line_thickness: float = 1
    ) -> None

    Draws a custom arrow at the end of a line segment.

    Parameters
    ----------
    start_point : tuple
        Coordinates of the start point (x, y).
    end_point : tuple
        Coordinates of the end point (x, y).
    color : str, optional
        Color of the arrow and line. (Default is 'black')
    line_thickness : float, optional
        Thickness of the line. (Default is 1)

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_custom_arrow_end(start_point=(0, 0), end_point=(1, 1), color='black', line_thickness=1)
    >>> plt.show()
    """
    start_point = list(start_point)
    end_point = list(end_point)
    modified_start = start_point.copy()
    modified_end = end_point.copy()
    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]
    modified_start[0] += 10 * dx / ((dx**2 + dy**2) ** 0.5)
    modified_start[1] += 10 * dy / ((dx**2 + dy**2) ** 0.5)
    modified_end[0] -= 10 * dx / ((dx**2 + dy**2) ** 0.5)
    modified_end[1] -= 10 * dy / ((dx**2 + dy**2) ** 0.5)
    dx = modified_end[0] - modified_start[0]
    dy = modified_end[1] - modified_start[1]
    plt.plot(
        [start_point[0], end_point[0]],
        [start_point[1], end_point[1]],
        color=color,
        linewidth=line_thickness,
    )
    plt.arrow(
        modified_start[0],
        modified_start[1],
        dx,
        dy,
        head_width=10,
        head_length=10,
        color=color,
        linewidth=line_thickness,
    )


def draw_two_axes(
    arrow_length: float,
    line_thickness: float,
    offset_text: float,
    longx: float,
    negativeaxis_y: int,
    negativeaxis_x: int,
) -> plt.Axes:
    """
    >>> draw_two_axes(
        arrow_length: float,
        line_thickness: float,
        offset_text: float,
        longx: float,
        negativeaxis_y: int,
        negativeaxis_x: int
    ) -> plt.Axes

    Draws two axes representing the x and y directions.

    Parameters
    ----------
    arrow_length : float
        Length of the arrows representing the axes.
    line_thickness : float
        Thickness of the arrows representing the axes.
    offset_text : float
        Offset for the axis labels.
    longx : float
        Length factor for the x-axis.
    negativeaxis_y : int
        Flag indicating whether to draw the negative y-axis.
    negativeaxis_x : int
        Flag indicating whether to draw the negative x-axis.

    Returns
    -------
    * `plt.Axes` :
        Axes object.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> ax = pltdraw.draw_two_axes(arrow_length=1.0, line_thickness=1.5, offset_text=0.1, longx=1.5, negativeaxis_y=1, negativeaxis_x=1)
    >>> plt.show()
    """
    fig, ax = plt.subplots()
    ax.arrow(
        0,
        0,
        0,
        arrow_length,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=line_thickness,
    )
    ax.text(0, arrow_length + offset_text, "y", fontsize=12, ha="center", va="bottom")

    if negativeaxis_y == 1:
        ax.arrow(
            0,
            0,
            0,
            -arrow_length,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=line_thickness,
        )

    ax.arrow(
        0,
        0,
        1.5 * arrow_length,
        0,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=line_thickness,
    )
    ax.text(
        1.5 * arrow_length + offset_text, 0, "x", fontsize=12, ha="left", va="center"
    )

    if negativeaxis_x == 1:
        ax.arrow(
            0,
            0,
            -arrow_length,
            0,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=line_thickness,
        )

    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    plt.axis("equal")
    return ax


def vertical_arrow_rain(
    quantity_arrows: int, start_point: tuple, final_point: tuple, y_origin: float
) -> None:
    """
    >>> vertical_arrow_rain(
        quantity_arrows: int,
        start_point: tuple,
        final_point: tuple,
        y_origin: float
    ) -> None

    Draws a specific quantity of arrows from equidistant points on a segment that extends from start_point to final_point, with all arrows pointing to y_origin.

    Parameters
    ----------
    quantity_arrows : int
        Number of arrows to draw.
    start_point : tuple
        Tuple (x, y) representing the starting point of the segment.
    final_point : tuple
        Tuple (x, y) representing the final point of the segment.
    y_origin : float
        y-coordinate to which all arrows should point.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.vertical_arrow_rain(quantity_arrows=5, start_point=(0, 1), final_point=(1, 1), y_origin=0)
    >>> plt.show()
    """
    x_start, y_start = start_point
    x_final, y_final = final_point
    x_points = [
        x_start + i * (x_final - x_start) / (quantity_arrows - 1)
        for i in range(quantity_arrows)
    ]
    y_points = [
        y_start + i * (y_final - y_start) / (quantity_arrows - 1)
        for i in range(quantity_arrows)
    ]
    for x, y in zip(x_points, y_points):
        plt.arrow(
            x, y, 0, y_origin - y, head_width=5, head_length=10, fc="blue", ec="blue"
        )


def draw_rain_arrows_horizontal(
    quantity_arrows: int, x_origin: float, start_point: tuple, final_point: tuple
) -> None:
    """
    >>> draw_rain_arrows_horizontal(
        quantity_arrows: int,
        x_origin: float,
        start_point: tuple,
        final_point: tuple
    ) -> None

    Draws a specific quantity of arrows from a vertical line at x_origin to equidistant points on a segment that extends from start_point to final_point.

    Parameters
    ----------
    quantity_arrows : int
        Number of arrows to draw.
    x_origin : float
        x-coordinate from which all arrows originate.
    start_point : tuple
        Tuple (x, y) representing the starting point of the segment.
    final_point : tuple
        Tuple (x, y) representing the final point of the segment.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_rain_arrows_horizontal(quantity_arrows=5, x_origin=0, start_point=(0, 1), final_point=(1, 1))
    >>> plt.show()
    """
    x_start, y_start = start_point
    x_final, y_final = final_point
    x_points = [
        x_start + i * (x_final - x_start) / (quantity_arrows - 1)
        for i in range(quantity_arrows - 1)
    ]
    y_points = [
        y_start + i * (y_final - y_start) / (quantity_arrows - 1)
        for i in range(quantity_arrows - 1)
    ]
    for x, y in zip(x_points, y_points):
        plt.arrow(
            x_origin,
            y,
            x - x_origin,
            0,
            head_width=5,
            head_length=10,
            fc="blue",
            ec="blue",
        )


def calculate_angle(start_point: tuple, final_point: tuple) -> float:
    """
    >>> calculate_angle(
        start_point: tuple,
        final_point: tuple
    ) -> float

    Calculates the angle (in degrees) between two points.

    Parameters
    ----------
    start_point : tuple
        Tuple (x, y) representing the starting point.
    final_point : tuple
        Tuple (x, y) representing the final point.

    Returns
    -------
    * `float` :
        The angle in degrees between the two points.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.calculate_angle(start_point=(0, 0), final_point=(1, 1))
    45.0
    """
    delta_x = final_point[0] - start_point[0]
    delta_y = final_point[1] - start_point[1]
    angle_rad = math.atan2(delta_y, delta_x)
    angle_degrees = math.degrees(angle_rad)
    if angle_degrees < 0:
        angle_degrees += 360
    return angle_degrees


def draw_segment_1(start: Union[tuple, list], end: Union[tuple, list]) -> None:
    """
    >>> draw_segment_1(
        start: Union[tuple, list],
        end: Union[tuple, list]
    ) -> None

    Draws a line segment in black ('k').

    Parameters
    ----------
    start : tuple or list
        The coordinates of the starting point [x1, y1].
    end : tuple or list
        The coordinates of the ending point [x2, y2].

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_segment_1((0, 0), (10, 0))
    >>> plt.show()
    """
    plt.plot([start[0], end[0]], [start[1], end[1]], color="k")


def draw_segment_2(start: Union[tuple, list], end: Union[tuple, list]) -> None:
    """
    >>> draw_segment_2(
        start: Union[tuple, list],
        end: Union[tuple, list]
    ) -> None

    Draws a line segment in red ('r').

    Parameters
    ----------
    start : tuple or list
        The coordinates of the starting point [x1, y1].
    end : tuple or list
        The coordinates of the ending point [x2, y2].

    Examples
    --------
    >>> import matplotlib.pyplot as pltdraw
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_segment_2((0, 2.6), (10, 1))
    >>> plt.show()
    """
    plt.plot([start[0], end[0]], [start[1], end[1]], color="r")


def draw_segment_3(start: Union[tuple, list], end: Union[tuple, list]) -> None:
    """
    >>> draw_segment_3(
        start: Union[tuple, list],
        end: Union[tuple, list]
    ) -> None

    Draws a line segment in blue ('b').

    Parameters
    ----------
    start : tuple or list
        The coordinates of the starting point [x1, y1].
    end : tuple or list
        The coordinates of the ending point [x2, y2].

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_segment_3((0, 2.6), (10, 1))
    >>> plt.show()
    """
    plt.plot([start[0], end[0]], [start[1], end[1]], color="b")


def get_arc_points(
    start_angle: float, end_angle: float, radius: float, center: Union[tuple, list]
) -> Tuple[np.ndarray, np.ndarray]:
    """
    >>> get_arc_points(
        start_angle: float,
        end_angle: float,
        radius: float,
        center: Union[tuple, list]
    ) -> Tuple[np.ndarray, np.ndarray]

    Calculates points along a circular arc defined by a start angle and an end angle.

    Parameters
    ----------
    start_angle : float
        The starting angle of the arc in degrees.
    end_angle : float
        The ending angle of the arc in degrees.
    radius : float
        The radius of the arc.
    center : tuple or list
        The coordinates of the center of the arc [cx, cy].

    Returns
    -------
    * `Tuple[np.ndarray, np.ndarray]` :
        The x and y coordinates of the arc points.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> arc_points_x1, arc_points_y1 = pltdraw.get_arc_points(90, 240, 0.25, (0, -0.25))
    >>> plt.plot(arc_points_x1, arc_points_y1, 'k')
    >>> plt.show()
    """
    angles = np.linspace(np.radians(start_angle), np.radians(end_angle), 100)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


__all__ = [
    "draw_arrow",
    "calculate_midpoint",
    "draw_arc_circumference",
    "create_blank_image",
    "draw_three_axes",
    "draw_two_inclined_axes",
    "plot_segment_pixels",
    "plot_annotate_arrow",
    "draw_custom_arrow",
    "calculate_arrow_endpoint_pixels",
    "plot_segment",
    "plot_segment_dashed",
    "draw_custom_circle",
    "draw_rounded_rectangle",
    "calculate_intersection_point",
    "draw_segment",
    "plot_annotate_arrow_end",
    "draw_arc_with_text",
    "draw_three_axes_rotated",
    "draw_double_arrowhead",
    "draw_custom_arrow_end",
    "draw_two_axes",
    "vertical_arrow_rain",
    "draw_rain_arrows_horizontal",
    "calculate_angle",
    "draw_segment_1",
    "draw_segment_2",
    "draw_segment_3",
    "get_arc_points",
]
