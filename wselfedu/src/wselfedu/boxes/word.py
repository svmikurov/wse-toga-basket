"""English-Russian dictionary."""

import toga


class WordBox(toga.Box):
    """English-Russian dictionary box."""

    def __init__(self):
        """Construct the English-Russian dictionary box."""
        super().__init__()

        # Table
        word_table = toga.Table(
            headings=['ID', 'По английски', 'по русски'],
            accessors=['id', 'word_eng', 'word_rus'],
        )

        # Buttons
        btn_update = toga.Button(
            'Изменить',
            on_press=self.update_word_handler,
        )
        btn_delete = toga.Button(
            'Удалить',
            on_press=self.delete_word_handler,
        )

        # Split box
        split_box = toga.Box()
        left_box = toga.Box()
        right_box = toga.Box()

        ##################
        # Build widget DOM
        self.add(
            split_box,
            word_table,
        )
        split_box.add(left_box, right_box)
        left_box.add(btn_update)
        right_box.add(btn_delete)

    ####################################################################
    # Button callback functions.
    def update_word_handler(self) -> None:
        """Update word button handler."""
        pass

    def delete_word_handler(self) -> None:
        """Delete word button handler."""
        pass
        # End Button callback functions.
        ################################
