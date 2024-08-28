"""Web self education project."""

import httpx

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class WebSelfEducation(toga.App):
    """Web self education application class."""

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return WebSelfEducation()
