# included in __all__: import using "from mecsimcalc import *" or "import mecsimcalc"

from .file_utils.general_utils import input_to_file, metadata_to_filetype

from .file_utils.image_utils import input_to_PIL, file_to_PIL, print_image


from .file_utils.plotting_utils import (
    print_plot,
    print_animation,
    animate_plot,
    plot_slider,
)


from .file_utils.spreadsheet_utils import (
    input_to_dataframe,
    file_to_dataframe,
    print_dataframe,
)

from .file_utils.table_utils import table_to_dataframe, print_table

from .file_utils.text_utils import string_to_file

from .file_utils.quiz_utils import append_to_google_sheet, send_gmail

# not included in __all__: import using "from mecsimcalc.plot_draw import *" or "import mecsimcalc.plot_draw"
from .plot_draw import *


__all__ = [
    "input_to_dataframe",
    "file_to_dataframe",
    "input_to_file",
    "input_to_PIL",
    "table_to_dataframe",
    "print_dataframe",
    "print_image",
    "string_to_file",
    "print_table",
    "print_plot",
    "metadata_to_filetype",
    "file_to_PIL",
    "append_to_google_sheet",
    "send_gmail",
    "print_animation",
    "animate_plot",
    "plot_slider",
]
