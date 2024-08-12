import sys
import os

import matplotlib.pyplot as plt
import numpy as np

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc")

from plot_draw import *


def test_all_functions():
    run_all_functions()


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
    draw_semicircle(radius=0.5, start_angle=0, end_angle=np.pi / 2)

    create_blank_canvas()

    # Draw three axes
    draw_three_axes(
        arrow_length=0.4,
        arrow_thickness=2,
        text_offset=0.05,
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

    # Draw a custom circle
    draw_circle((100, 100), radius=20, color="red")

    # Draw a rounded rectangle
    draw_rounded_rectangle(4, 2, center=(0, 0), corner_radius=0.5, color="blue")

    # Calculate intersection point
    intersection_point = calculate_intersection_point(
        (0, 0), 45, (1, 1), 135, degrees=True
    )
    assert intersection_point == (1.0, 0.9999999999999999)

    # Draw a line
    draw_line((0.2, 0.2), (0.8, 0.8))

    # Draw three rotated axes
    draw_three_axes_rotated(
        arrow_length=0.4,
        line_thickness=2,
        text_offset=0.05,
        longx=1.5,
        negativeaxis_y=1,
        negativeaxis_x=1,
    )

    # Draw a double arrowhead
    draw_double_arrowhead((0.1, 0.1), (0.4, 0.4))

    # Draw two axes
    draw_two_axes(
        arrow_length=0.4,
        line_thickness=2,
        text_offset=0.05,
        longx=1.5,
        negativeaxis_y=1,
        negativeaxis_x=1,
    )

    # Vertical arrow rain
    vertical_arrow_rain(
        quantity_arrows=5, start=(0.1, 0.9), end=(0.9, 0.9), y_origin=0.5
    )

    # Horizontal arrow rain
    horizontal_arrow_rain(
        quantity_arrows=5, x_origin=0.5, start=(0.1, 0.1), end=(0.1, 0.9)
    )

    # Calculate angle between two points
    angle = calculate_angle((0, 0), (1, 1), degrees=True)
    assert angle == 45

    # Get arc points
    x, y = get_arc_points(start_angle=0, end_angle=180, radius=0.5, center=(0.5, 0.5))
    plt.plot(x, y, color="green")
