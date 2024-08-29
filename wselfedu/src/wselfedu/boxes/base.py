"""Base box."""

import toga
from toga.style import Pack
from travertino.constants import COLUMN


class ColumnFlexBox(toga.Box):
    """Column box with flex is True, box widget.

    Does not accept parameters.

    style = Pack(flex=1, direction=COLUMN)
    """

    def __init__(self) -> None:
        """Construct Column Box class."""
        style = Pack(flex=1, direction=COLUMN)
        super().__init__(style=style)
