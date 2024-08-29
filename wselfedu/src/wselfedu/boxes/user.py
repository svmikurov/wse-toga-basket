"""User box."""

import toga
from toga.style import Pack
from travertino.constants import COLUMN


class UserBox(toga.Box):
    """User box."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the User Box."""
        super().__init__(*args, **kwargs)

        # Box buttons.
        btn_goto_main_box = toga.Button(
            'На главную',
            on_press=self.goto_main_box_handler,
            style=Pack(flex=1),
        )

        # Navigation box is split into two parts.
        split_navigation_box = toga.Box()
        left_box = toga.Box(style=Pack(flex=1, direction=COLUMN))
        right_box = toga.Box(style=Pack(flex=1, direction=COLUMN))

        # Word box widget DOM.
        self.add(
            split_navigation_box,
        )
        split_navigation_box.add(left_box, right_box)
        left_box.add(btn_goto_main_box)
        right_box.add()

    def goto_main_box_handler(self, widget: toga.Widget) -> None:
        """Go to Main box, button handler."""
        self.app.main_window.content = self.app.main_box
