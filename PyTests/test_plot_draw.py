import sys
import os

import matplotlib.pyplot as plt
import numpy as np

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc")

from plotting_utils import print_plot
from plot_draw import *


def test_print_plot():
    # convert file data to pillow image
    plt = make_plt()

    # try converting plot to html img
    plt_html = print_plot(plt)

    # check that html img is correct
    assert plt_html.startswith("<img src='data:image/png;base64,")

    # check that html img is correct with download
    plt_html, downloadHTMLplt = print_plot(plt, download=True)

    # check that html img is correct with download
    assert plt_html.startswith("<img src='data:image/png;base64,")

    # check that download is correct
    assert downloadHTMLplt.startswith("<a href='data:image/png;base64,")



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
    midpoint = calculate_midpoint((0, 0), (1, 1))
    print(f"Midpoint: {midpoint}")

    # Draw an arc of a circumference
    draw_arc_circumference(radius=0.5, initial_angle=0, final_angle=np.pi / 2)

    # Draw three axes
    draw_three_axes(arrow_length=0.4, arrow_thickness=2, offset_text=0.05, longx=1.5, axis_y_negative=True, axis_x_negative=True)

    # Draw two inclined axes
    draw_two_inclined_axes(arrow_length=0.4, arrow_thickness=2, offset_text=0.05, longx=1.5, axis_y_negative=True, axis_x_negative=True)

    # Plot a segment in pixels
    plot_segment_pixels((100, 100), (200, 200), text="Segment", min_spacing=20)

    # Plot and annotate an arrow
    plot_annotate_arrow((0.2, 0.2), trig_angle=45, vec_length=0.2, text="Annotated Arrow")

    # Draw a custom arrow
    draw_custom_arrow(plt, start_point=(200, 200), point_2=(300, 300), factor=0.5, max_value=400, arrow_vector_length=100, arrow_width=10, text="Custom Arrow")

    # Calculate arrow endpoint in pixels
    arrow_endpoint = calculate_arrow_endpoint_pixels((100, 100), trig_angle=45, vec_length=50)
    print(f"Arrow endpoint: {arrow_endpoint}")

    # Plot a segment with properties
    plot_segment((0.1, 0.1), trig_angle=45, vec_length=0.3, text="Segment")

    # Plot a dashed segment
    plot_segment_dashed((0.1, 0.1), trig_angle=135, vec_length=0.3, text="Dashed Segment")

    # Draw a custom circle
    draw_custom_circle(plt, center_point=(300, 300), circle_size=50)

    # Draw a rounded rectangle
    draw_rounded_rectangle((0.5, 0.5), width=0.2, height=0.1, radius=0.05)

    # Calculate intersection point
    intersection_point = calculate_intersection_point((0, 0), 45, (1, 1), 135)
    print(f"Intersection point: {intersection_point}")

    # Draw a segment
    draw_segment((0.2, 0.2), (0.8, 0.8))

    # Draw three rotated axes
    draw_three_axes_rotated(arrow_length=0.4, line_thickness=2, offset_text=0.05, longx=1.5, negativeaxis_y=1, negativeaxis_x=1)

    # Draw a double arrowhead
    draw_double_arrowhead((0.1, 0.1), (0.4, 0.4))

    # Draw custom arrow end
    draw_custom_arrow_end((0.1, 0.1), (0.4, 0.4))

    # Draw two axes
    draw_two_axes(arrow_length=0.4, line_thickness=2, offset_text=0.05, longx=1.5, negativeaxis_y=1, negativeaxis_x=1)

    # Vertical arrow rain
    vertical_arrow_rain(quantity_arrows=5, start_point=(0.1, 0.9), final_point=(0.9, 0.9), y_origin=0.5)

    # Horizontal arrow rain
    draw_rain_arrows_horizontal(quantity_arrows=5, x_origin=0.5, start_point=(0.1, 0.1), final_point=(0.1, 0.9))

    # Calculate angle between two points
    angle = calculate_angle((0, 0), (1, 1))
    print(f"Angle: {angle}")

    # Draw segments in different colors
    draw_segment_1((0.1, 0.1), (0.4, 0.4))
    draw_segment_2((0.4, 0.4), (0.7, 0.7))
    draw_segment_3((0.7, 0.7), (1.0, 1.0))

    # Get arc points
    x, y = get_arc_points(start_angle=0, end_angle=180, radius=0.5, center=(0.5, 0.5))
    plt.plot(x, y, color='green')

