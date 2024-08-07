import sys
import os

import matplotlib.pyplot as plt
import numpy as np

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc")

from plot_draw import *


def make_plt():
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)
    plt.plot(x, y, label="sin(x)")
    plt.title("A Simple Plot")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.legend()
    run_all_functions()
    return plt


def run_all_functions():
    # Draw a basic arrow
    draw_arrow(start=(0.1, 0.1), end=(0.3, 0.3), text="Arrow")

    # Calculate the midpoint between two coordinates
    assert calculate_midpoint((0, 0), (1, 1)) == (0.5, 0.5)

    # Draw an arc of a circumference
    draw_arc(radius=0.5, start_angle=0, end_angle=np.pi / 2)

    create_blank_canvas()

    # Draw three axes
    draw_three_axes(
        arrow_length=0.4,
        arrow_thickness=2,
        offset_text=0.05,
        longx=1.5,
        axis_y_negative=True,
        axis_x_negative=True,
    )

    # Draw two inclined axes
    draw_two_inclined_axes(
        arrow_length=0.4,
        arrow_thickness=2,
        text_offset=0.05,
        longx=1.5,
        draw_negative_y=True,
        draw_negative_x=True,
    )

    # Plot a segment in pixels
    assert plot_line_segment(
        (100, 200), (400, 500), label="Segment", min_spacing=20
    ) == (400, 500)

    # plot annotation arrow
    start = (100, 200)
    angle = 45
    length = 100
    x, y = plot_annotate_arrow(start, angle, length, text="Arrow", degrees=True)
    assert round(x, 2), round(y, 2) == (170.71, 270.71)

    # Draw a custom arrow
    draw_custom_arrow(
        plt,
        start_point=(200, 200),
        point_2=(300, 300),
        factor=0.5,
        max_value=400,
        arrow_vector_length=100,
        arrow_width=10,
        text="Custom Arrow",
    )

    # Calculate arrow endpoint in pixels
    x, y = calculate_arrow_endpoint_pixels(
        (100, 200), angle=45, length=50, degrees=True
    )
    assert (round(x, 2), round(y, 2)) == (135.36, 235.36)

    # Plot a segment with properties
    x, y = plot_segment((100, 200), 45, 50, text="Value", degrees=True)
    assert (round(x, 2), round(y, 2)) == (135.36, 235.36)

    # Plot a dashed segment
    x, y = plot_segment_dashed((100, 200), 45, 50, text="Value", degrees=True)
    assert (round(x, 2), round(y, 2)) == (135.36, 235.36)

    # Draw a custom circle
    draw_custom_circle((100, 100), radius=20, color="red")

    # Draw a rounded rectangle
    draw_rounded_rectangle((0, 0), 4, 2, 0.5, color="blue")

    # Calculate intersection point
    intersection_point = calculate_intersection_point((0, 0), 45, (1, 1), 135)
    assert intersection_point == (1.0, 0.9999999999999999)

    # Draw a segment
    draw_segment((0.2, 0.2), (0.8, 0.8))

    x, y = plot_annotate_arrow_end(
        (1, 1),
        45,
        1,
        text="End",
        text_offset=0.5,
        fontsize=12,
        text_align={"ha": "center", "va": "top"},
        degrees=True,
    )
    assert round(x, 2), round(y, 2) == (10.90, 10.90)

    # Draw three rotated axes
    draw_three_axes_rotated(
        arrow_length=0.4,
        line_thickness=2,
        offset_text=0.05,
        longx=1.5,
        negativeaxis_y=1,
        negativeaxis_x=1,
    )

    # Draw a double arrowhead
    draw_double_arrowhead((0.1, 0.1), (0.4, 0.4))

    # Draw custom arrow end
    draw_custom_arrow_end((0.1, 0.1), (0.4, 0.4))

    # Draw two axes
    draw_two_axes(
        arrow_length=0.4,
        line_thickness=2,
        offset_text=0.05,
        longx=1.5,
        negativeaxis_y=1,
        negativeaxis_x=1,
    )

    # Vertical arrow rain
    vertical_arrow_rain(
        quantity_arrows=5, start_point=(0.1, 0.9), final_point=(0.9, 0.9), y_origin=0.5
    )

    # Horizontal arrow rain
    draw_rain_arrows_horizontal(
        quantity_arrows=5, x_origin=0.5, start_point=(0.1, 0.1), final_point=(0.1, 0.9)
    )

    # Calculate angle between two points
    angle = calculate_angle((0, 0), (1, 1))
    assert angle == 45

    # Draw segments in different colors
    draw_segment_1((0.1, 0.1), (0.4, 0.4))
    draw_segment_2((0.4, 0.4), (0.7, 0.7))
    draw_segment_3((0.7, 0.7), (1.0, 1.0))

    # Get arc points
    x, y = get_arc_points(start_angle=0, end_angle=180, radius=0.5, center=(0.5, 0.5))
    plt.plot(x, y, color="green")
