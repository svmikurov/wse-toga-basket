"""Web self education application."""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from wselfedu.boxes.base import ColumnFlexBox
from wselfedu.boxes.user import LoginBox, UserBox
from wselfedu.boxes.word import WordBox


class WebSelfEducation(toga.App):
    """Web self education application class."""

    main_box: toga.Box
    user_box: UserBox
    word_box: WordBox

    btn_goto_main_box: toga.Button
    btn_goto_user_box: toga.Button
    btn_goto_word_box: toga.Button

    def startup(self) -> None:
        """Construct the main window and widgets for it."""
        # Initialize the box widgets to populate the main window.
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.user_box = UserBox(style=Pack(direction=COLUMN))
        self.word_box = WordBox(style=Pack(direction=COLUMN))

        # Main box widgets.
        btn_goto_word_box = toga.Button(
            'Словарь',
            on_press=self.goto_word_box_btn_handler,
            style=Pack(flex=1),
        )
        btn_goto_user_box = toga.Button(
            'Профиль',
            on_press=self.goto_user_box_btn_handler,
            style=Pack(flex=1),
        )

        # Navigation box split into pairs.
        pair_split_box = toga.Box()
        left_split_box = ColumnFlexBox()
        right_split_box = ColumnFlexBox()

        # Main box widget DOM.
        self.main_box.add(
            pair_split_box,
        )
        pair_split_box.add(left_split_box, right_split_box)
        left_split_box.add(
            btn_goto_user_box,
        )
        right_split_box.add(
            btn_goto_word_box,
        )

        # Construct and show the populated main window.
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def goto_main_box_btn_handler(self, widget: toga.Widget) -> None:
        """Go to Main box, button handler."""
        self.main_window.content = self.main_box

    def goto_user_box_btn_handler(self, widget: toga.Widget) -> None:
        """Go to User box, button handler."""
        self.main_window.content = self.user_box

    def goto_word_box_btn_handler(self, widget: toga.Widget) -> None:
        """Go to Word box, button handler."""
        self.main_window.content = self.word_box
        self.word_box.fill_table()


def main() -> WebSelfEducation:
    """Return the app instance."""
    return WebSelfEducation()
