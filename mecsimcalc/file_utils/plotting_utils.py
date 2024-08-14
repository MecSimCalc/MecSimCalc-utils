import io
import os
import base64
from typing import Union, Tuple, Callable

import matplotlib.pyplot as plt
import matplotlib.figure as figure
from matplotlib.animation import FuncAnimation

import numpy as np
import plotly.graph_objects as go
import plotly.io as pio


def print_plot(
    plot_obj: Union[plt.Axes, figure.Figure],
    width: int = 500,
    dpi: int = 100,
    download: bool = False,
    download_text: str = "Download Plot",
    download_file_name: str = "myplot",
) -> Union[str, Tuple[str, str]]:
    """
    >>> print_plot(
        plot_obj: Union[plt.Axes, figure.Figure],
        width: int = 500,
        dpi: int = 100,
        download: bool = False,
        download_text: str = "Download Plot",
        download_file_name: str = "myplot"
    ) -> Union[str, Tuple[str, str]]

    Converts a matplotlib plot into an HTML image tag and optionally provides a download link for the image.

    Parameters
    ----------
    plot_obj : Union[plt.Axes, figure.Figure]
        The matplotlib plot to be converted.
    width : int, optional
        The width of the image in pixels. Defaults to `500`.
    dpi : int, optional
        The DPI of the image. Defaults to `100`.
    download : bool, optional
        If set to True, a download link will be provided. Defaults to `False`.
    download_text : str, optional
        The text to be displayed for the download link. Defaults to `"Download Plot"`.
    download_file_name : str, optional
        The name of the downloaded file. Defaults to `"myplot"`

    Returns
    -------
    * `Union[str, Tuple[str, str]]` :
        * If `download` is Fal0se, returns the HTML image as a string.
        * If `download` is True, returns a tuple consisting of the HTML image as a string and the download link as a string.


    Examples
    ----------
    **Without Download Link**:
    >>> fig, ax = plt.subplots()
    >>> ax.plot([1, 2, 3], [1, 2, 3])
    >>> plot = msc.print_plot(ax)
    >>> return {
        "plot": plot
    }

    **With Download Link and Custom Download Text**:
    >>> fig, ax = plt.subplots()
    >>> ax.plot([1, 2, 3], [1, 2, 3])
    >>> plot, download_link = msc.print_plot(ax, download=True, download_text="Download My Plot")
    >>> return {
        "plot": plot,
        "download_link": download_link
    }
    """
    file_type = "jpeg"

    if isinstance(plot_obj, plt.Axes):
        plot_obj = plot_obj.get_figure()

    # Save the plot to a buffer
    buffer = io.BytesIO()
    plot_obj.savefig(buffer, format=file_type, dpi=dpi)

    if hasattr(plot_obj, "close"):
        plot_obj.close()

    # generate image
    encoded_image = (
        f"data:image/{file_type};base64,{base64.b64encode(buffer.getvalue()).decode()}"
    )
    html_img = f"<img src='{encoded_image}' width='{width}'>"

    if not download:
        return html_img

    download_link = (
        f"<a href='{encoded_image}' "
        f"download='{download_file_name}.{file_type}'>{download_text}</a>"
    )
    return html_img, download_link


def print_animation(
    ani: FuncAnimation, fps: int = 30, save_dir: str = "/tmp/temp_animation.gif"
) -> str:
    """
    >>> print_ani(ani: FuncAnimation, fps: int = 30) -> str

    Converts a matplotlib animation into an HTML image tag.

    Parameters
    ----------
    ani : FuncAnimation
        The matplotlib animation to be converted.
    fps : int, optional
        Frames per second for the animation. Defaults to `30`.
    save_dir : str, optional
        The directory to save the animation. Defaults to `"/tmp/temp_animation.gif"`. (Note: The file will be deleted after the execution of the app is finished.)

    Returns
    -------
    * `str` :
        The HTML image tag as a string.

    Examples
    --------
    >>> fig, ax = plt.subplots()
    >>> x = np.linspace(0, 10, 1000)
    >>> y = np.sin(x)
    >>> line, = ax.plot(x, y)
    >>> def update(frame):
    >>>     line.set_ydata(np.sin(x + frame / 100))
    >>> ani = FuncAnimation(fig, update, frames=100)
    >>> animation = msc.print_animation(ani)
    >>> return {
        "animation": animation
    }
    """
    # Save the animation to a temporary file
    temp_file = save_dir
    if not temp_file.endswith(".gif"):
        temp_file += "temp_animation.gif"

    ani.save(temp_file, writer="pillow", fps=fps)

    # Read the file back into a bytes buffer
    with open(temp_file, "rb") as f:
        gif_bytes = f.read()

    # Remove the temporary file (but will get deleted when the execution of the app is finished anyway bc it is in the /tmp folder)
    os.remove(temp_file)

    # Convert the bytes buffer to a base64 string and return it as an image tag
    gif_base64 = base64.b64encode(gif_bytes).decode("utf-8")
    return f"<img src='data:image/gif;base64,{gif_base64}' />"


def animate_plot(
    x: np.ndarray,
    y: np.ndarray,
    duration: float = 3,
    fps: float = 15,
    x_label: str = "x",
    y_label: str = "y",
    title: str = "y = f(x)",
    show_axes: bool = True,
    follow_tip: bool = False,
    hold_last_frame: float = 1.0,
    save_dir: str = "/tmp/temp_animation.gif",
) -> str:
    """
    >>> animate_plot(
        x: np.ndarray,
        y: np.ndarray,
        duration: float = 3,
        fps: float = 15,
        x_label: str = "x",
        y_label: str = "y",
        title: str = "y = f(x)",
        show_axes: bool = True,
        follow_tip: bool = False,
        hold_last_frame: float = 1.0,
        save_dir: str = "/tmp/temp_animation.gif"
    ) -> str:
    Creates an animated plot from given x and y data and returns it as an HTML image tag.

    Parameters
    ----------
    x : np.ndarray
        The x-coordinates of the data points.
    y : np.ndarray
        The y-coordinates of the data points.
    duration : float, optional
        The duration of the animation in seconds. Defaults to `3`.
    fps : float, optional
        Frames per second for the animation. Defaults to 15.
    title : str, optional
        Title of the plot. Defaults to `"y = f(x)"`.
    show_axes : bool, optional
        Whether to show the x and y axes. Defaults to `True`.
    follow_tip : bool, optional
        Whether to follow the tip of the line as it moves along the x-axis. Defaults to `False`.
    hold_last_frame : float, optional
        The duration to hold the last frame in seconds. Defaults to `1.0`.
    save_dir : str, optional
        The directory to save the animation. Defaults to `"/tmp/temp_animation.gif"`. (Note: The file will be deleted after the execution of the app is finished.)

    Returns
    -------
    * `str` :
        The HTML image tag containing the animated plot.

    Examples
    --------
    >>> import numpy as np
    >>> import mecsimcalc as msc
    >>> x = np.linspace(0, 10, 100)
    >>> y = np.sin(x)
    >>> animation_html = msc.animate_plot(x, y, duration=4, title="Sine Wave", show_axes=True)
    >>> return {
        "animation": animation_html
    }
    """

    fig, ax = plt.subplots()
    (line,) = ax.plot([], [])  # line being drawn on the plot

    if fps > len(x) / duration:
        fps = len(x) / duration

    # Set the x and y limits of the plot (with some padding for y-axis)
    min_y = np.min(y) - 0.1 * (np.max(y) - np.min(y))
    max_y = np.max(y) + 0.1 * (np.max(y) - np.min(y))

    ax.set_ylim(min_y, max_y)
    ax.set_xlim(np.min(x), np.max(x))

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    if show_axes:
        plt.axhline(0, color="grey", linestyle="--", alpha=0.5)
        plt.axvline(0, color="grey", linestyle="--", alpha=0.5)

    # Initialize the plot (optimize performance by not redrawing the plot every frame)
    def init():
        line.set_data([], [])
        return (line,)

    # Function to update the plot
    def update(frame):
        frame_idx = int(frame)

        # shift the line by frame_idx (update the line data with the new x and y data)
        x_shift = x[:frame_idx]
        y_shift = y[:frame_idx]
        line.set_data(x_shift, y_shift)

        # Adjust x-axis limits based on the current frame (follow the line as it moves along the x-axis)
        if follow_tip and frame_idx < len(x):
            current_x = np.interp(frame, np.arange(len(x)), x)
            ax.set_xlim(current_x - max(x) / duration, current_x + max(x) / duration)
        return (line,)

    frames = np.linspace(0, len(x), int(duration * fps))
    frames = np.concatenate(
        [frames, np.full(int(fps * hold_last_frame), len(x))]
    )  # holds the last frame for a while

    ani = FuncAnimation(fig, update, init_func=init, frames=frames, blit=True)

    plt.close()
    return print_animation(
        ani, fps=fps, save_dir=save_dir
    )  # return the animation as an HTML image tag


def plot_slider(
    f_x: Callable[[float, np.ndarray], np.ndarray],
    x_range: Tuple[float, float],
    y_range: Tuple[float, float] = None,
    title: str = "",
    x_label: str = "x",
    y_label: str = "y",
    num_points: int = 250,
    initial_value: float = 1,
    step_size: float = 0.1,
    slider_range: Tuple[float, float] = (-10, 10),
) -> str:
    """
    >>> def plot_slider(
        f_x: Callable[[float, np.ndarray], np.ndarray],
        x_range: Tuple[float, float],
        y_range: Tuple[float, float] = None,
        title: str = "",
        x_label: str = "x",
        y_label: str = "y",
        num_points: int = 250,
        initial_value: float = 0,
        step_size: float = 0.1,
        slider_range: Tuple[float, float] = (-10, 10)
    ) -> str:

    Creates an interactive plot with a slider using Plotly, which allows the user to dynamically update the plot based on a parameter.

    Parameters
    ----------
    f_x : Callable[[float, np.ndarray], np.ndarray]
        A function that takes a float and an array of x-values, and returns an array of y-values.
    x_range : Tuple[float, float]
        A tuple defining the range of x-values (start, end) for the plot.
    y_range : Tuple[float, float], optional
        A tuple defining the range of y-values (start, end) for the plot. Defaults to None.
    title : str, optional
        Title of the plot. Defaults to `""`.
    x_label : str, optional
        Label for the x-axis. Defaults to `"x"`.
    y_label : str, optional
        Label for the y-axis. Defaults to `"y"`.
    num_points : int, optional
        Number of points to plot (line resolution). Defaults to `250`.
    initial_value : float, optional
        Initial value of the slider. Defaults to `1`.
    step_size : float, optional
        Step size for the slider. Defaults to `0.1`.
    slider_range : Tuple[float, float], optional
        Range for the slider values (start, end). Defaults to `(-10, 10)`.

    Returns
    -------
    * `str` :
        The HTML string containing the Plotly interactive plot.

    Examples
    --------
    >>> import mecsimcalc as msc
    >>> def parabola(a, x):
    >>>     return a * x ** 2
    >>> plot_html = msc.plot_slider(parabola, x_range=(-10, 10), y_range = (-100, 100))
    >>> return {
    >>>     "plot": plot_html
    >>> }
    """
    # Generate x values from the given range
    x = np.linspace(x_range[0], x_range[1], num_points)

    # Compute initial y values
    y = f_x(initial_value, x)

    # Create a Plotly figure
    fig = go.Figure()

    # Add initial plot
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            name=f"a={initial_value}",
            line=dict(color="#1f77b4"),
        )
    )

    # Generate slider steps
    slider_steps = [
        {
            "method": "update",
            "label": str(a),
        }
        for a in np.arange(slider_range[0], slider_range[1] + step_size, step_size)
    ]

    # Find the closest index to initial_value in the slider steps
    initial_value_index = min(
        range(len(slider_steps)),
        key=lambda i: abs(float(slider_steps[i]["label"]) - initial_value),
    )

    # Add slider for 'a'
    sliders = [
        {
            "active": initial_value_index,
            "currentvalue": {"prefix": "a="},
            "pad": {"t": 50},
            "steps": [
                {
                    "method": "update",
                    "label": str(round(a, 1)),
                    "args": [{"y": [f_x(a, x)]}],
                }
                for a in np.arange(
                    slider_range[0], slider_range[1] + step_size, step_size
                )
            ],
        }
    ]

    # Define layout for a color scheme that works on both light and dark themes
    layout = {
        "plot_bgcolor": "#2b2b2b",
        "paper_bgcolor": "#2b2b2b",
        "font": {"color": "#ffffff"},
        "title": {"text": title, "x": 0.5, "xanchor": "center"},
        "xaxis": {
            "title": x_label,
            "range": [x_range[0], x_range[1]],
            "color": "#ffffff",
        },
        "yaxis": {"title": y_label, "color": "#ffffff"},
    }

    if y_range:
        layout["yaxis"]["range"] = y_range
    else:
        layout["yaxis"]["autorange"] = True

    fig.update_layout(layout)
    fig.update_layout(sliders=sliders)

    # Convert Plotly figure to HTML
    return pio.to_html(fig, full_html=False)
