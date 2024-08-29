"""English-Russian dictionary."""

import toga
from toga.style import Pack
from travertino.constants import COLUMN

from wselfedu.contrib.http_requests import send_get_request

WORDS_PATH = 'api/v1/word/'


class WordBox(toga.Box):
    """English-Russian dictionary box."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the English-Russian dictionary box."""
        super().__init__(*args, **kwargs)

        # Box table.
        self.word_table = toga.Table(
            headings=['ID', 'По-английски', 'По-русски'],
            accessors=['id', 'word_eng', 'word_rus'],
        )

        # Box buttons.
        btn_add = toga.Button(
            'Добавить',
            on_press=self.add_word_handler,
            style=Pack(flex=1),
        )
        btn_update = toga.Button(
            'Изменить',
            on_press=self.update_word_handler,
            style=Pack(flex=1),
        )
        btn_delete = toga.Button(
            'Удалить',
            on_press=self.delete_word_handler,
            style=Pack(flex=1),
        )
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
            self.word_table,
        )
        split_navigation_box.add(left_box, right_box)
        left_box.add(btn_goto_main_box, btn_update)
        right_box.add(btn_add, btn_delete)

    # Button callback functions.
    def add_word_handler(self, widget: toga.Widget) -> None:
        """Add word, button handler."""
        pass

    def update_word_handler(self, widget: toga.Widget) -> None:
        """Update word, button handler."""
        pass

    def delete_word_handler(self, widget: toga.Widget) -> None:
        """Delete word, button handler."""
        pass

    def goto_main_box_handler(self, widget: toga.Widget) -> None:
        """Go to Main box, button handler."""
        self.app.main_window.content = self.app.main_box

    def fill_table(self, url: str | None = None) -> None:
        """Fill the Word Table box."""
        word_response = send_get_request(WORDS_PATH, url)
        self.word_table.data = word_response['results']
