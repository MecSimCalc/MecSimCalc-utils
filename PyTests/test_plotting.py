import sys
import os

import matplotlib.pyplot as plt
import numpy as np

# caution: path[0] is reserved for script path (or '' in REPL)
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)

sys.path.insert(1, f"{PARENT_DIR}/mecsimcalc/file_utils")

from plotting_utils import print_plot


def test_print_plot():
    # convert file data to pillow image
    fig = make_fig()
    plt = make_plt()
    ax = make_ax()

    # try converting plot to html img
    fig_html = print_plot(fig)
    plt_html = print_plot(plt)
    ax_html = print_plot(ax)

    # check that html img is correct
    assert fig_html.startswith("<img src='data:image/png;base64,")
    assert plt_html.startswith("<img src='data:image/png;base64,")
    assert ax_html.startswith("<img src='data:image/png;base64,")

    # check that html img is correct with download
    fig_html, downloadHTMLfig = print_plot(fig, download=True)
    plt_html, downloadHTMLplt = print_plot(plt, download=True)
    ax_html, downloadHTMLax = print_plot(ax, download=True)

    # check that html img is correct with download
    assert fig_html.startswith("<img src='data:image/png;base64,")
    assert plt_html.startswith("<img src='data:image/png;base64,")
    assert ax_html.startswith("<img src='data:image/png;base64,")

    # check that download is correct
    assert downloadHTMLfig.startswith("<a href='data:image/png;base64,")
    assert downloadHTMLplt.startswith("<a href='data:image/png;base64,")
    assert downloadHTMLax.startswith("<a href='data:image/png;base64,")


def make_fig():
    # make plot
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)
    ax.plot(x, y)
    return fig


def make_plt():
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)

    plt.plot(x, y, label="sin(x)")
    plt.title("A Simple Plot")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.legend()
    return plt


def make_ax():
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)

    ax = plt.axes()
    ax.plot(x, y, label="sin(x)")
    ax.set_title("A Simple Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("sin(x)")
    ax.legend()
    return ax
