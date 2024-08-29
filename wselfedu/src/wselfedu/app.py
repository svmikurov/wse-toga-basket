"""Web self education application."""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from wselfedu.boxes.word import WordBox


class WebSelfEducation(toga.App):
    """Web self education application class."""

    main_box: toga.Box
    word_box: WordBox

    btn_goto_main_box: toga.Button
    btn_goto_word_box: toga.Button

    def startup(self) -> None:
        """Construct the main window and widgets for it."""
        # Initialize the box widgets to populate the main window.
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.word_box = WordBox(style=Pack(direction=COLUMN))

        # Main box widgets.
        navigation_box = toga.Box()
        self.btn_goto_word_box = toga.Button(
            'Словарь',
            on_press=self.goto_word_box_handler,
            style=Pack(flex=1),
        )

        # Main box widget DOM.
        self.main_box.add(
            navigation_box,
        )
        navigation_box.add(
            self.btn_goto_word_box,
        )

        # Construct and show the populated main window.
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def goto_main_box_handler(self, widget: toga.Widget) -> None:
        """Go to Main box, button handler."""
        self.main_window.content = self.main_box

    def goto_word_box_handler(self, widget: toga.Widget) -> None:
        """Go to Word box, button handler."""
        self.main_window.content = self.word_box
        self.word_box.fill_table()


def main() -> WebSelfEducation:
    """Return the app instance."""
    return WebSelfEducation()
