"""English-Russian dictionary."""

import toga
from toga import Widget
from toga.style import Pack
from travertino.constants import COLUMN

from wselfedu.boxes.base import ColumnFlexBox
from wselfedu.contrib.http_requests import send_get_request, send_post_request

WORDS_PATH = 'api/v1/word/'
FIELDS = {
    'word_eng': 'Слово по-русски',
    'word_rus': 'Слово по-английски',
}
"""Word input field labels (`dict[str, str]`).
"""


class CreateWordBox(toga.Box):
    """Create Word Box."""

    def __init__(self) -> None:
        """Construct the Create Word box."""
        box_style = Pack(direction=COLUMN)
        super().__init__(style=box_style)

        # Create Word box widgets.
        self.box_msg_label = toga.Label('Добавить слово')
        self.eng_word_input = toga.TextInput(placeholder=FIELDS['word_eng'])
        self.rus_word_input = toga.TextInput(placeholder=FIELDS['word_rus'])
        btn_create_word_submit = toga.Button(
            text='Добавить', on_press=self.create_word_handler
        )

        # Create Word box widget DOM.
        self.add(
            self.box_msg_label,
            self.eng_word_input,
            self.rus_word_input,
            btn_create_word_submit,
        )
        self.eng_word_input.focus()

    def create_word_handler(self, widget: Widget) -> None:
        """Add translation of word to English-Russian dictionary."""
        word_translation = {
            'word_eng': self.eng_word_input.value,
            'word_rus': self.rus_word_input.value,
        }

        # Gets the response to the API request.
        response = send_post_request(path=WORDS_PATH, payload=word_translation)
        is_success = response.get('id')

        # The message about the result of adding a word is displayed
        # in the box message label.
        if is_success:
            msg = (
                f'Добавлено слово: "{self.eng_word_input.value}"'
                f' - "{self.rus_word_input.value}"'
            )
            self.eng_word_input.value = None
            self.rus_word_input.value = None
        else:
            msg = ['Слово не добавлено:']
            for field, message in response.items():
                msg.append(f'{FIELDS[field]} - {message.pop()}')
            msg = '\n'.join(msg)
        self.box_msg_label.text = msg


class WordBox(toga.Box):
    """English-Russian dictionary box."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the English-Russian dictionary box."""
        super().__init__(*args, **kwargs)

        # Initialize the box widgets.
        self.create_word_box = CreateWordBox()

        # Box table.
        self.word_table = toga.Table(
            headings=['ID', 'По-английски', 'По-русски'],
            accessors=['id', 'word_eng', 'word_rus'],
        )

        # Box buttons.
        btn_create = toga.Button(
            'Добавить',
            on_press=self.goto_create_word_handler,
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

        # Navigation box split into pairs.
        pair_split_box = toga.Box()
        left_split_box = ColumnFlexBox()
        right_split_box = ColumnFlexBox()

        # Word box widget DOM.
        self.add(
            pair_split_box,
            self.word_table,
        )
        pair_split_box.add(left_split_box, right_split_box)
        left_split_box.add(
            btn_goto_main_box,
            btn_update,
        )
        right_split_box.add(
            btn_create,
            btn_delete,
        )

    # Button callback functions.
    def goto_create_word_handler(self, widget: Widget) -> None:
        """Add word to dictionary, button handler."""
        self.app.main_window.content = self.create_word_box

    def update_word_handler(self, widget: Widget) -> None:
        """Update word, button handler."""
        pass

    def delete_word_handler(self, widget: Widget) -> None:
        """Delete word, button handler."""
        pass

    def goto_main_box_handler(self, widget: Widget) -> None:
        """Go to Main box, button handler."""
        self.app.main_window.content = self.app.main_box

    def fill_table(self, url: str | None = None) -> None:
        """Fill the Word Table box."""
        word_response = send_get_request(WORDS_PATH, url)
        self.word_table.data = word_response['results']
