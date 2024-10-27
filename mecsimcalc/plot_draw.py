from typing import Union, Tuple, Optional, Dict, Any
import matplotlib.pyplot as plt
import numpy as np
import math


def blank_canvas(width: int = 800, height: int = 600, color: str = "white") -> plt.Axes:
    """
    >>> blank_canvas(width: int = 800, height: int = 600, color: str = "white") -> plt.Axes

    Creates a blank canvas with specified width, height, and background color.

    Parameters
    ----------
    width : int, optional
        The width of the canvas in pixels (Default is 800).
    height : int, optional
        The height of the canvas in pixels (Default is 600).
    color : str, optional
        The background color of the canvas (Default is 'white').

    Returns
    -------
    * `plt.Axes`
        The Axes object of the created blank canvas.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> import matplotlib.pyplot as plt
    >>> ax = pltdraw.blank_canvas()
    >>> plt.show()
    """
    fig, ax = plt.subplots(figsize=(width / 100, height / 100))
    ax.set_facecolor(color)
    ax.tick_params(
        axis="both",
        which="both",
        bottom=False,
        top=False,
        left=False,
        right=False,
        labelbottom=False,
        labelleft=False,
    )
    ax.grid(True, alpha=0.5)
    ax.minorticks_on()
    ax.grid(which="minor", linestyle=":", linewidth="0.5", color="gray")
    return ax


def draw_line(
    start: Tuple[float, float],
    end: Tuple[float, float],
    color: str = "black",
    line_width: Optional[float] = None,
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> draw_line(
        start: Tuple[float, float],
        end: Tuple[float, float],
        color: str = 'black',
        line_width: Optional[float] = None,
        ax: Optional[plt.Axes] = None
    ) -> None

    Draws a line between two points with a specified line_width and color.

    Parameters
    ----------
    start : Tuple[float, float]
        The coordinates of the starting point (x, y).
    end : Tuple[float, float]
        The coordinates of the final point (x, y).
    line_width : float, optional
        The width of the segment. (Default is 0.001)
    color : str, optional
        The color of the segment. (Default is 'black')
    ax : Optional[plt.Axes], optional
        The Axes object to draw the segment on. If None, uses the current Axes

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_line((0, 0), (1, 1), line_width=0.005, color='blue')
    >>> plt.show()
    """
    ax = ax or plt.gca()
    if line_width is None:
        ax.plot(
            [start[0], end[0]], [start[1], end[1]], color=color, linewidth=line_width
        )
    else:
        x_initial, y_initial = start
        x_final, y_final = end
        angle = np.arctan2(y_final - y_initial, y_final - x_initial)
        offset_x = np.sin(angle) * line_width / 2
        offset_y = np.cos(angle) * line_width / 2
        x1 = x_initial + offset_x
        y1 = y_initial - offset_y
        x2 = x_initial - offset_x
        y2 = y_initial + offset_y
        x3 = x_final - offset_x
        y3 = y_final + offset_y
        x4 = x_final + offset_x
        y4 = y_final - offset_y
        plt.fill([x1, x2, x3, x4, x1], [y1, y2, y3, y4, y1], color=color)


def draw_arrow(
    start: Union[tuple, list],
    end: Union[tuple, list],
    thickness: float = 5,
    color: str = "black",
    text: str = "",
    text_offset: float = 0.1,
    head_width: float = 0.08,
    head_length: float = 0.08,
    fontsize: float = 12,
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> draw_arrow(
        start: Union[tuple, list],
        end: Union[tuple, list],
        thickness: float = 5,
        color: str = "black",
        text: Optional[str] = None,
        text_offset: float = 0.1,
        head_width: float = 0.08,
        head_length: float = 0.08,
        fontsize: float = 12,
        ax: Optional[plt.Axes] = None,
    ) -> None

    Draws an arrow between two points on a plot with optional text annotation.

    Parameters
    ----------
    start : Union[tuple, list]
        The starting point of the arrow (x, y).
    end : Union[tuple, list]
        The ending point of the arrow (x, y).
    thickness : float, optional
        The thickness of the arrow line. (Default is 5)
    color : str, optional
        The color of the arrow. (Default is 'black')
    text : Optional[str], optional
        Text to display near the arrow. (Default is None)
    text_offset : float, optional
        Distance from the arrow end point where the text will be placed. (Default is 0.1)
    head_width : float, optional
        Width of the arrow head. (Default is 0.08)
    head_length : float, optional
        Length of the arrow head. (Default is 0.08)
    fontsize : float, optional
        Font size of the text. (Default is 12)
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes. (Default is None)


    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> import matplotlib.pyplot as plt
    >>> pltdraw.draw_arrow((0, 0), (1, 1), thickness=2, color='red', text='Arrow', text_offset=0.1, head_width=0.1, head_length=0.1, fontsize=10)
    >>> plt.xlim(-1, 2)
    >>> plt.ylim(-1, 2)
    >>> plt.show()
    """
    ax = ax or plt.gca()
    start, end = np.array(start), np.array(end)
    ax.arrow(
        start[0],
        start[1],
        end[0] - start[0],
        end[1] - start[1],
        head_width=head_width,
        head_length=head_length,
        linewidth=thickness,
        color=color,
        length_includes_head=True,
    )
    if text:
        arrow_vector = end - start
        text_position = end + text_offset * arrow_vector / np.linalg.norm(arrow_vector)
        ax.text(text_position[0], text_position[1], text, fontsize=fontsize)


def draw_double_arrowhead(
    start: Tuple[float, float],
    end: Tuple[float, float],
    color: str = "black",
    line_thickness: float = 1,
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> draw_double_arrowhead(
        start: Tuple[float, float],
        end: Tuple[float, float],
        color: str = 'black',
        line_thickness: float = 1
        ax: Optional[plt.Axes] = None
    ) -> None

    Draws a double arrowhead between two points.

    Parameters
    ----------
    start : Tuple[float, float]
        Coordinates of the start point (x, y).
    end : Tuple[float, float]
        Coordinates of the end point (x, y).
    color : str, optional
        Color of the arrow and line. (Default is 'black')
    line_thickness : float, optional
        Thickness of the line. (Default is 1)
    ax : Optional[plt.Axes], optional
        The Axes object to draw the plot on. If None, uses the current Axes.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_double_arrowhead(start=(0, 0), end=(1, 1))
    >>> plt.show()
    """
    ax = ax or plt.gca()

    start = list(start)
    end = list(end)
    modified_start = start.copy()
    modified_end = end.copy()
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    modified_start[0] += 0.08 * dx / ((dx**2 + dy**2) ** 0.5)
    modified_start[1] += 0.08 * dy / ((dx**2 + dy**2) ** 0.5)
    modified_end[0] -= 0.08 * dx / ((dx**2 + dy**2) ** 0.5)
    modified_end[1] -= 0.08 * dy / ((dx**2 + dy**2) ** 0.5)
    dx = modified_end[0] - modified_start[0]
    dy = modified_end[1] - modified_start[1]
    plt.plot(
        [start[0], end[0]],
        [start[1], end[1]],
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


def vertical_arrow_rain(
    quantity: int,
    start: Tuple[float, float],
    end: Tuple[float, float],
    y_origin: float = 0,
    arrow_color: str = "blue",
    head_width: float = 0.05,
    head_length: float = 0.1,
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> def vertical_arrow_rain(
        quantity: int,
        start: Tuple[float, float],
        end: Tuple[float, float],
        y_origin: float = 0,
        arrow_color: str = "blue",
        head_width: float = 0.05,
        head_length: float = 0.1,
        ax: Optional[plt.Axes] = None
    ) -> None:

    Draws a specific quantity of arrows from equidistant points on a segment that extends from start to end,
    with all arrows pointing to y_origin.

    Parameters
    ----------
    quantity : int
        Number of arrows to draw.
    start : Tuple[float, float]
        Tuple (x, y) representing the starting point of the segment.
    end : Tuple[float, float]
        Tuple (x, y) representing the final point of the segment.
    y_origin : float, optional
        y-coordinate to which all arrows should point. Default is 0.
    arrow_color : str, optional
        Color of the arrows. Default is "blue".
    head_width : float, optional
        Width of the arrow heads. Default is 0.05.
    head_length : float, optional
        Length of the arrow heads. Default is 0.1.
    ax : Optional[plt.Axes], optional

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> fig, ax = plt.subplots()
    >>> pltdraw.vertical_arrow_rain(quantity=5, start=(0, 1), end=(1, 1), y_origin=0)
    >>> plt.show()
    """
    ax = ax or plt.gca()

    if quantity < 2:
        raise ValueError("quantity must be at least 2.")

    x_initial, y_initial = start
    x_final, y_final = end

    x_points = [
        x_initial + i * (x_final - x_initial) / (quantity - 1) for i in range(quantity)
    ]
    y_points = [
        y_initial + i * (y_final - y_initial) / (quantity - 1) for i in range(quantity)
    ]

    for x, y in zip(x_points, y_points):
        plt.arrow(
            x,
            y,
            0,
            y_origin - y,
            head_width=head_width,
            head_length=head_length,
            fc=arrow_color,
            ec=arrow_color,
        )


def horizontal_arrow_rain(
    quantity: int,
    start: Tuple[float, float],
    end: Tuple[float, float],
    x_origin: float = 0,
    arrow_color: str = "blue",
    head_width: float = 0.05,
    head_length: float = 0.1,
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> def horizontal_arrow_rain(
        quantity: int,
        start: Tuple[float, float],
        end: Tuple[float, float],
        x_origin: float = 0,
        arrow_color: str = "blue",
        head_width: float = 0.05,
        head_length: float = 0.1,
        ax: Optional[plt.Axes] = None,
    ) -> None:

    Draws a specific quantity of arrows from equidistant points on a segment that extends from start to end,
    with all arrows pointing to x_origin.

    Parameters
    ----------
    quantity : int
        Number of arrows to draw.
    start : Tuple[float, float]
        Tuple (x, y) representing the starting point of the segment.
    end : Tuple[float, float]
        Tuple (x, y) representing the final point of the segment.
    x_origin : float, optional
        x-coordinate to which all arrows should point. Default is 0.
    arrow_color : str, optional
        Color of the arrows. Default is "blue".
    head_width : float, optional
        Width of the arrow heads. Default is 0.05.
    head_length : float, optional
        Length of the arrow heads. Default is 0.1.
    ax : Optional[plt.Axes], optional

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots()
    >>> horizontal_arrow_rain(quantity=5, start=(1, 0), end=(1, 1), x_origin=0)
    >>> plt.show()
    """
    ax = ax or plt.gca()

    if quantity < 2:
        raise ValueError("quantity must be at least 2.")

    x_initial, y_initial = start
    x_final, y_final = end

    x_points = [
        x_initial + i * (x_final - x_initial) / (quantity - 1) for i in range(quantity)
    ]
    y_points = [
        y_initial + i * (y_final - y_initial) / (quantity - 1) for i in range(quantity)
    ]

    for x, y in zip(x_points, y_points):
        plt.arrow(
            x,
            y,
            x_origin - x,
            0,
            head_width=head_width,
            head_length=head_length,
            fc=arrow_color,
            ec=arrow_color,
        )


def draw_circle(
    center: Tuple[float, float] = (0, 0),
    radius: float = 10,
    color: str = "black",
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> draw_circle(
        center: Tuple[float, float] = (0, 0),
        radius: float = 10,
        color: str = "black",
        ax: Optional[plt.Axes] = None
    ) -> None:

    Draws a custom circle on a given axis.

    Parameters
    ----------
    center : Tuple[float, float], optional
        The center point of the circle (x, y). Default is (0, 0).
    radius : float, optional
        The radius of the circle. (Default is 10)
    color : str, optional
        The color of the circle. (Default is 'black')
    ax : Optional[plt.Axes], optional
        The Axes object to draw the circle on. If None, creates a new figure and axis.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_circle((100, 100), radius=20, color='red')
    >>> plt.show()
    """
    ax = ax or plt.gca()

    # Calculate the area in points^2 for the scatter size parameter
    area = np.pi * (radius**2)

    ax.scatter(center[0], center[1], s=area, color=color)


def draw_arc(
    radius: float,
    start_angle: float,
    end_angle: float,
    center: Tuple[float, float] = (0, 0),
    degrees: bool = False,
    color: str = "red",
    text: str = "",
    text_offset: float = 0.1,
    fontsize: float = 12,
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> def draw_arc(
        radius: float,
        start_angle: float,
        end_angle: float,
        center: Tuple[float, float] = (0, 0),
        degrees: bool = False,
        color: str = "red",
        text: str = "",
        text_offset: float = 0.1,
        fontsize: float = 12,
        ax: Optional[plt.Axes] = None,
    ) -> None:

    Draws an arc of a circle with a given radius between two angles.

    Parameters
    ----------
    radius : float
        The radius of the arc.
    start_angle : float
        The starting angle of the arc in radians.
    end_angle : float
        The ending angle of the arc in radians.
    center : tuple, optional
        The center of the arc (Default is (0, 0)).
    degrees : bool, optional
        Whether the angles are given in degrees (Default is False).
    color : str, optional
        The color of the arc (Default is 'red').
    text : str, optional
        Text to display near the arc (Default is '').
    text_offset : float, optional
        Distance from the arc where the text will be placed (Default is 0.1).
    fontsize : int, optional
        Font size of the text (Default is 12).
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes (Default is None).


    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> import matplotlib.pyplot as plt
    >>> pltdraw.draw_arc(5, 0, 90, degrees=True)
    >>> plt.show()
    """
    ax = ax or plt.gca()
    if degrees:
        start_angle = np.radians(start_angle)
        end_angle = np.radians(end_angle)

    if abs(end_angle - start_angle) > 2 * np.pi:
        end_angle = 2 * np.pi
        start_angle = 0

    angles = np.linspace(start_angle, end_angle, 200)
    x = radius * np.cos(angles) + center[0]
    y = radius * np.sin(angles) + center[1]
    ax.plot(x, y, color=color)
    ax.axis("equal")

    if text:
        mid_angle = (start_angle + end_angle) / 2
        text_x = center[0] + radius * np.cos(mid_angle) * (1 + text_offset)
        text_y = center[1] + radius * np.sin(mid_angle) * (1 + text_offset)

        ax.text(
            text_x,
            text_y,
            text,
            fontsize=fontsize,
            ha="center",
            va="center",
        )


def draw_rounded_rectangle(
    width: float,
    height: float,
    center: Tuple[float, float] = (0, 0),
    corner_radius: float = 0.5,
    color: str = "black",
    ax: Optional[plt.Axes] = None,
) -> None:
    """
    >>> def draw_rounded_rectangle(
        width: float,
        height: float,
        center: Tuple[float, float] = (0, 0),
        corner_radius: float = 0.5,
        color: str = "black",
        ax: Optional[plt.Axes] = None,
    ) -> None:

    Draws a rounded rectangle with specified properties.

    Parameters
    ----------
    width : float
        The width of the rounded rectangle.
    height : float
        The height of the rounded rectangle.
    center : Tuple[float, float], optional
        The center point of the rectangle (x, y). Default is (0, 0).
    corner_radius : float, optional
        The radius of the corners. Default is 0.5.
    color : str, optional
        The color of the rectangle. (Default is 'black')
    ax : Optional[plt.Axes], optional
        The Axes object to draw the rectangle on. If None, uses the current Axes.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.draw_rounded_rectangle(4, 2, center = (0,0), corner_radius = 0.5,  color='blue')
    >>> plt.show()
    """
    ax = ax or plt.gca()

    x_center, y_center = center
    x1 = x_center - width / 2
    y1 = y_center - height / 2
    x2 = x_center + width / 2
    y2 = y_center + height / 2

    # Draw the straight edges
    plt.plot([x1 + corner_radius, x2 - corner_radius], [y1, y1], color=color)
    plt.plot([x2, x2], [y1 + corner_radius, y2 - corner_radius], color=color)
    plt.plot([x2 - corner_radius, x1 + corner_radius], [y2, y2], color=color)
    plt.plot([x1, x1], [y2 - corner_radius, y1 + corner_radius], color=color)

    # Draw the corners
    corner_angles = np.linspace(np.pi, 1.5 * np.pi, 50)
    plt.plot(
        x1 + corner_radius + corner_radius * np.cos(corner_angles),
        y1 + corner_radius + corner_radius * np.sin(corner_angles),
        color=color,
    )  # bottom-left corner

    corner_angles = np.linspace(1.5 * np.pi, 2 * np.pi, 50)
    plt.plot(
        x2 - corner_radius + corner_radius * np.cos(corner_angles),
        y1 + corner_radius + corner_radius * np.sin(corner_angles),
        color=color,
    )  # bottom-right corner

    corner_angles = np.linspace(0, 0.5 * np.pi, 50)
    plt.plot(
        x2 - corner_radius + corner_radius * np.cos(corner_angles),
        y2 - corner_radius + corner_radius * np.sin(corner_angles),
        color=color,
    )  # top-right corner

    corner_angles = np.linspace(0.5 * np.pi, np.pi, 50)
    plt.plot(
        x1 + corner_radius + corner_radius * np.cos(corner_angles),
        y2 - corner_radius + corner_radius * np.sin(corner_angles),
        color=color,
    )  # top-left corner


def draw_two_axes(
    arrow_length: float,
    line_thickness: float = 1.5,
    text_offset: float = 0.1,
    negative_y: bool = False,
    negative_x: bool = False,
    ax: Optional[plt.Axes] = None,
) -> plt.Axes:
    """
    >>> def draw_two_axes(
        arrow_length: float,
        line_thickness: float = 1.5,
        text_offset: float = 0.1,
        negative_y: bool = False,
        negative_x: bool = False,
        ax: Optional[plt.Axes] = None
    ) -> plt.Axes:

    Draws two axes representing the x and y directions.

    Parameters
    ----------
    arrow_length : float
        Length of the arrows representing the axes.
    line_thickness : float, optional
        Thickness of the arrows representing the axes. (Default is 1.5)
    text_offset : float, optional
        Offset for the axis labels. (Default is 0.1)
    negative_y : bool, optional
        Indicating whether to draw the negative y-axis.
    negative_x : bool, optional
        Indicating whether to draw the negative x-axis.

    Returns
    -------
    * `plt.Axes` :
        Axes object.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> ax = pltdraw.draw_two_axes(arrow_length=1.0, negative_y=True, negative_x=True)
    >>> plt.show()
    """
    longx = 1
    ax = ax or plt.gca()

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
    ax.text(0, arrow_length + text_offset, "y", fontsize=12, ha="center", va="bottom")

    if negative_y:
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
        longx * arrow_length,
        0,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=line_thickness,
    )
    ax.text(
        longx * arrow_length + text_offset, 0, "x", fontsize=12, ha="left", va="center"
    )

    if negative_x:
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


def draw_two_inclined_axes(
    arrow_length: float,
    arrow_thickness: float = 2.0,
    text_offset: float = 0.1,
    negative_y: bool = False,
    negative_x: bool = False,
    ax: Optional[plt.Axes] = None,
) -> plt.Axes:
    """
    >>> def draw_two_inclined_axes(
        arrow_length: float,
        arrow_thickness: float = 2.0,
        text_offset: float = 0.1,
        negative_y: bool = False,
        negative_x: bool = False,
        ax: Optional[plt.Axes] = None
    ) -> plt.Axes:

    Draws two inclined axes (x and y) with optional negative directions.

    Parameters
    ----------
    arrow_length : float
        The length of the arrows representing the axes.
    arrow_thickness : float, optional
        The thickness of the arrows (Default is 2.0).
    text_offset : float, optional
        The distance between the end of the arrow and the label text (Default is 0.1).
    negative_y : bool, optional
        Whether to draw the negative y-axis (Default is False).
    negative_x : bool, optional
        Whether to draw the negative x-axis (Default is False).
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes (Default is None).

    Returns
    -------
    * `plt.Axes`
        The Axes object with the drawn axes.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> import matplotlib.pyplot as plt
    >>> ax = pltdraw.draw_two_inclined_axes(arrow_length=1, arrow_thickness=2, text_offset=0.1, negative_y=True, negative_x=True)
    >>> plt.show()
    """
    longx = 1.5
    ax = ax or plt.gca()
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
    ax.text(arrow_length + text_offset, 0, "x", fontsize=12, ha="left", va="center")

    if negative_x:
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
        arrow_length / longx + text_offset / 1.5,
        arrow_length / longx + text_offset / 1.5,
        "y",
        fontsize=12,
        ha="left",
        va="bottom",
    )

    if negative_y:
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
    ax.axis("equal")
    return ax


def draw_three_axes(
    arrow_length: float,
    arrow_thickness: float = 2.0,
    text_offset: float = 0.1,
    negative_y: bool = False,
    negative_x: bool = False,
    ax: Optional[plt.Axes] = None,
) -> plt.Axes:
    """
    >>> def draw_three_axes(
        arrow_length: float,
        arrow_thickness: float = 2.0,
        text_offset: float = 0.1,
        negative_y: bool = False,
        negative_x: bool = False,
        ax: Optional[plt.Axes] = None
    ) -> plt.Axes:

    Draws a set of three axes (x, y, z) with optional negative directions for x and y.

    Parameters
    ----------
    arrow_length : float
        The length of the arrows representing the axes.
    arrow_thickness : float, optional
        The thickness of the arrows (Default is 2.0).
    text_offset : float, optional
        The distance between the end of the arrow and the label text (Default is 0.1).
    negative_y : bool, optional
        Whether to draw the negative y-axis (Default is False).
    negative_x : bool, optional
        Whether to draw the negative x-axis (Default is False).
    ax : Optional[plt.Axes], optional
        Matplotlib Axes object to draw on. If None, uses current Axes (Default is None).

    Returns
    -------
    * `plt.Axes`
        The Axes object with the drawn axes.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> import matplotlib.pyplot as plt
    >>> ax = pltdraw.draw_three_axes(arrow_length=1, arrow_thickness=2, text_offset=0.1, negative_y=True, negative_x=True)
    >>> plt.show()
    """
    longx = 2
    ax = ax or plt.gca()
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
    ax.text(0, arrow_length + text_offset, "z", fontsize=12, ha="center", va="bottom")

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
    ax.text(arrow_length + text_offset, 0, "y", fontsize=12, ha="left", va="center")

    if negative_y:
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
        -arrow_length / longx - text_offset / 1.5,
        -arrow_length / longx - text_offset / 1.5,
        "x",
        fontsize=12,
        ha="right",
        va="top",
    )

    if negative_x:
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
    ax.axis("equal")
    return ax


def draw_three_axes_rotated(
    arrow_length: float,
    line_thickness: float = 1.5,
    text_offset: float = 0.2,
    negative_y: bool = False,
    negative_x: bool = False,
    ax: Optional[plt.Axes] = None,
) -> plt.Axes:
    """
    >>> draw_three_axes_rotated(
        arrow_length: float,
        line_thickness: float = 1.5,
        text_offset: float = 0.2,
        negative_y: bool = False,
        negative_x: bool = False,
        ax: Optional[plt.Axes] = None
    ) -> plt.Axes

    Draws three rotated axes in a 3D coordinate system.

    Parameters
    ----------
    arrow_length : float
        The length of the arrow.
    line_thickness : float
        The thickness of the line. (Default is 1.5)
    text_offset : float
        The offset of the text from the arrow. (Default is 0.2)
    negative_y : bool
        Whether to include negative y-axis (default is False).
    negative_x : bool
        Whether to include negative x-axis (default is False).
    ax : Optional[plt.Axes], optional
        The Axes object to draw the plot on. If None, uses the current Axes.

    Returns
    -------
    * `plt.Axes` :
        The matplotlib Axes object containing the plot.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> ax = pltdraw.draw_three_axes_rotated(arrow_length=1.0, negative_y=True, negative_x=True)
    >>> plt.show()
    """
    ax = ax or plt.gca()

    angle = np.radians(30)

    longx = 1

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
    ax.text(0, arrow_length + text_offset, "z", fontsize=12, ha="center", va="bottom")

    ax.arrow(
        0,
        0,
        -arrow_length * np.cos(angle) / longx,
        -arrow_length * np.sin(angle) / longx,
        head_width=0.05,
        head_length=0.1,
        fc="gray",
        ec="gray",
        lw=line_thickness,
    )
    ax.text(
        -arrow_length * np.cos(angle) / longx - text_offset,
        -arrow_length * np.sin(angle) / longx - text_offset,
        "x",
        fontsize=12,
        ha="left",
        va="center",
    )

    if negative_x:
        ax.arrow(
            0,
            0,
            arrow_length * np.cos(angle) / longx,
            arrow_length * np.sin(angle) / longx,
            head_width=0,
            head_length=0,
            fc="gray",
            ec="gray",
            lw=line_thickness,
        )
        ax.arrow(
            0,
            0,
            arrow_length * np.cos(angle) / longx,
            -arrow_length * np.sin(angle) / longx,
            head_width=0.05,
            head_length=0.1,
            fc="gray",
            ec="gray",
            lw=line_thickness,
        )
        ax.text(
            arrow_length * np.cos(angle) / longx + 2 * text_offset / 1.5,
            -arrow_length * np.sin(angle) / longx - text_offset / 1.5,
            "y",
            fontsize=12,
            ha="right",
            va="top",
        )

    if negative_y:
        ax.arrow(
            0,
            0,
            -arrow_length * np.cos(angle) / longx,
            arrow_length * np.sin(angle) / longx,
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


def calculate_midpoint(
    coord1: Tuple[float, float], coord2: Tuple[float, float]
) -> Tuple[float, float]:
    """
    >>> calculate_midpoint(
        coord1: Tuple[float, float],
        coord2: Tuple[float, float]
    ) -> Tuple[float, float]

    Calculates the midpoint between two coordinates.

    Parameters
    ----------
    coord1 : Tuple[float, float]
        The first coordinate (x, y).
    coord2 : Tuple[float, float]
        The second coordinate (x, y).

    Returns
    -------
    * `Tuple[float, float]`
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
    return (x1 + x2) / 2, (y1 + y2) / 2


def calculate_intersection_point(
    point1: Tuple[float, float],
    angle1: float,
    point2: Tuple[float, float],
    angle2: float,
    degrees: bool = False,
) -> Tuple[float, float]:
    """
    >>> def calculate_intersection_point(
        point1: Tuple[float, float],
        angle1: float,
        point2: Tuple[float, float],
        angle2: float,
        degrees: bool = False
    ) -> Tuple[float, float]:

    Calculates the intersection point of two lines defined by points and angles.

    Parameters
    ----------
    point1 : Tuple[float, float]
        The coordinates of the first point (x, y) through which the first line passes.
    angle1 : float
        The angle of the first line in degrees or radians.
    point2 : Tuple[float, float]
        The coordinates of the second point (x, y) through which the second line passes.
    angle2 : float
        The angle of the second line in degrees or radians.
    degrees : bool, optional
        Whether the angles are given in degrees (Default is False).

    Returns
    -------
    * `Tuple[float, float]`
        The coordinates of the intersection point (x, y). (None, None) if the lines are parallel.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.calculate_intersection_point((0, 0), 45, (1, 1), 135, degrees=True)
    (1.0, 0.9999999999999999)
    """
    if degrees:
        angle1 = np.radians(angle1)
        angle2 = np.radians(angle2)

    x1, y1 = point1
    x2, y2 = point2

    # Calculate the slopes of the lines
    m1 = np.tan(angle1)
    m2 = np.tan(angle2)

    # lines are parallel so they don't intersect
    if m1 == m2:
        return None, None

    b1 = y1 - m1 * x1
    b2 = y2 - m2 * x2

    intersection_x = float((b2 - b1) / (m1 - m2))
    intersection_y = float(m1 * intersection_x + b1)

    return intersection_x, intersection_y


def calculate_arrow_endpoint(
    start: tuple, angle: float, length: float, degrees: bool = False
) -> tuple:
    """
    >>> def calculate_arrow_endpoint(
        start: tuple, angle: float, length: float, degrees: bool = False
    ) -> tuple:

    Calculates the end point of an arrow in pixel coordinates.

    Parameters
    ----------
    start : tuple
        The starting point of the arrow (x, y) in pixel coordinates.
    angle : float
        The angle of the arrow in degrees or radians.
    length : float
        The length of the arrow.
    degrees : bool, optional
        Whether the angle is given in degrees (Default is False).

    Returns
    -------
    * `Tuple[float, float]`
        The end point of the arrow (x, y) in pixel coordinates.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.calculate_arrow_endpoint((100, 200), 45, 50, degrees=True)
    (135.35533905932738, 235.35533905932738)
    """
    if degrees:
        angle = np.radians(angle)

    # Normalize angle to [0, 2*pi)
    angle = angle % (2 * np.pi)

    end_x = float(start[0] + length * np.cos(angle))
    end_y = float(start[1] + length * np.sin(angle))

    return end_x, end_y


def calculate_angle(
    start: Tuple[float, float], end: Tuple[float, float], degrees: bool = False
) -> float:
    """
    >>> calculate_angle(
        start: Tuple[float, float],
        end: Tuple[float, float],
        degrees: bool = False
    ) -> float

    Calculates the angle between two points.

    Parameters
    ----------
    start : Tuple[float, float]
        Tuple (x, y) representing the starting point.
    end : Tuple[float, float]
        Tuple (x, y) representing the final point.
    degrees : bool, optional
        Whether to return the angle in degrees (Default is False).

    Returns
    -------
    * `float` :
        The angle between the two points.

    Examples
    --------
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> pltdraw.calculate_angle(start=(0, 0), end=(1, 1), degrees=True)
    45.0
    """
    delta_x = end[0] - start[0]
    delta_y = end[1] - start[1]
    angle_rad = math.atan2(delta_y, delta_x)

    # normalize angle to [0, 2*pi)
    angle_rad = angle_rad % (2 * math.pi)

    return math.degrees(angle_rad) if degrees else angle_rad


def get_arc_points(
    start_angle: float,
    end_angle: float,
    radius: float,
    center: Tuple[float, float] = (0, 0),
    degrees: bool = False,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    >>> def get_arc_points(
        start_angle: float,
        end_angle: float,
        radius: float,
        center: Tuple[float, float] = (0, 0),
        degrees: bool = False
    ) -> Tuple[np.ndarray, np.ndarray]:

    Calculates points along a circular arc defined by a start angle and an end angle.

    Parameters
    ----------
    start_angle : float
        The starting angle of the arc in degrees or radians.
    end_angle : float
        The ending angle of the arc in degrees or radians.
    radius : float
        The radius of the arc.
    center : Tuple[float, float], optional
        The coordinates of the center of the arc [cx, cy]. (Default is (0, 0))
    degrees : bool, optional
        Whether the angles are given in degrees (Default is False).

    Returns
    -------
    * `Tuple[np.ndarray, np.ndarray]`
        The x and y coordinates of the arc points.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> import numpy as np
    >>> import mecsimcalc.plot_draw as pltdraw
    >>> arc_points_x1, arc_points_y1 = pltdraw.get_arc_points(90, 240, 0.25, (0, -0.25), degrees=True)
    >>> plt.plot(arc_points_x1, arc_points_y1, 'k')
    >>> plt.show()
    """
    if degrees:
        start_angle = np.radians(start_angle)
        end_angle = np.radians(end_angle)

    angles = np.linspace(start_angle, end_angle, 100)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return x, y


__all__ = [
    "draw_arrow",
    "calculate_midpoint",
    "draw_arc",
    "blank_canvas",
    "draw_three_axes",
    "draw_two_inclined_axes",
    "calculate_arrow_endpoint",
    "draw_circle",
    "draw_rounded_rectangle",
    "calculate_intersection_point",
    "draw_line",
    "draw_three_axes_rotated",
    "draw_double_arrowhead",
    "draw_two_axes",
    "vertical_arrow_rain",
    "horizontal_arrow_rain",
    "calculate_angle",
    "get_arc_points",
]
