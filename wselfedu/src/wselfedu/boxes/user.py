"""User boxes."""

import toga
from toga.style import Pack
from toga.widgets.base import StyleT
from travertino.constants import COLUMN

from wselfedu.boxes.base import ColumnFlexBox
from wselfedu.contrib.http_requests import send_post_request

USER_REGISTRATION_SCHEMA_PATH = '/api/v1/auth/users/'


class UserRegistrationBox(toga.Box):
    """User Registration box."""

    def __init__(
        self,
        *args: object,
        style: StyleT | None = None,
        **kwargs: object,
    ) -> None:
        """Construct the User Registration box."""
        style = style or Pack(direction=COLUMN)
        super().__init__(*args, style=style, **kwargs)

        # User Registration box widgets.
        user_registration_box_label = toga.Label(
            'Регистрация нового пользователя',
        )
        self.username_input = toga.TextInput(
            placeholder='Введите имя',
        )
        self.password_input = toga.PasswordInput(
            placeholder='Введите пароль',
        )
        btn_registrate_user = toga.Button(
            'Зарегистрироваться',
            on_press=self.registrate_user_btn_handler,
            style=Pack(flex=1),
        )

        # User Registration box widget DOM.
        self.add(
            user_registration_box_label,
            self.username_input,
            self.password_input,
            btn_registrate_user,
        )

    def registrate_user_btn_handler(self, widget: toga.Widget) -> None:
        """Registrate user, button handler.

        Displays a user registration check dialog box.
        """
        user_registration_data = {
            'username': self.username_input.value,
            'password': self.password_input.value,
        }
        title_error = 'Регистрация не закончена:'
        first_massage_index = 0

        # Gets the response to the API request.
        response = send_post_request(
            path=USER_REGISTRATION_SCHEMA_PATH,
            payload=user_registration_data,
        )
        id_response = response.get('id')
        username_response = response.get('username')
        password_response = response.get('password')

        # Displays a user registration check dialog box.
        if id_response:
            self.app.main_window.info_dialog(
                'Регистрация завершена', 'Поздравляю!'
            )
        elif username_response:
            self.app.main_window.info_dialog(
                title_error, username_response[first_massage_index]
            )
        elif password_response:
            self.app.main_window.info_dialog(
                title_error, password_response[first_massage_index]
            )
        else:
            self.app.main_window.info_dialog(
                title_error, 'Неизвестная ошибка, попробуйте еще раз'
            )

    def goto_user_box_btn_handler(self, widget: Widget) -> None:
        """Go to User Profile box, button handler."""
        self.app.main_window.content = self.app.user_box

class LoginBox(toga.Box):
    """Log in box."""

    def __init__(self) -> None:
        """Construct the Log in box."""
        login_box_style = Pack(direction=COLUMN)
        super().__init__(style=login_box_style)

        # Log in box widgets.
        login_box_label = toga.Label(
            'Вход в приложение',
        )
        self.username_input = toga.TextInput(
            placeholder='Введите имя',
        )
        self.password_input = toga.PasswordInput(
            placeholder='Введите пароль',
        )
        btn_submit = toga.Button(
            'Войти',
            on_press=self.login_submit_btn_handler,
            style=Pack(flex=1),
        )
        btn_goto_user_box = toga.Button(
            'Профиль',
            on_press=self.goto_user_box_btn_handler,
            style=Pack(flex=1),
        )

        # Log in box widget DOM.
        self.add(
            btn_goto_user_box,
            login_box_label,
            self.username_input,
            self.password_input,
            btn_submit,
        )

    def login_submit_btn_handler(self, widget: Widget) -> None:
        """Submit log in, button handler."""
        user_login_data = {
            'username': self.username_input.value,
            'password': self.password_input.value,
        }

    def goto_user_box_btn_handler(self, widget: Widget) -> None:
        """Go to User Profile box, button handler."""
        self.app.main_window.content = self.app.user_box


class UserBox(toga.Box):
    """User box."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the User Box."""
        super().__init__(*args, **kwargs)

        # User box widgets.
        self.user_registration_box = UserRegistrationBox()
        self.login_box = LoginBox()
        btn_goto_main_box = toga.Button(
            'На главную',
            on_press=self.goto_main_box_btn_handler,
            style=Pack(flex=1),
        )
        btn_login_box = toga.Button(
            'Войти в приложение',
            on_press=self.goto_login_box_btn_handler,
            style=Pack(flex=1),
        )
        btn_goto_user_registration_box = toga.Button(
            'Регистрация',
            on_press=self.goto_user_registration_box_btn_handler,
            style=Pack(flex=1),
        )

        # Navigation box split into pairs.
        pair_split_box = toga.Box()
        left_split_box = ColumnFlexBox()
        right_split_box = ColumnFlexBox()

        # Word box widget DOM.
        self.add(
            pair_split_box,
        )
        pair_split_box.add(left_split_box, right_split_box)
        left_split_box.add(
            btn_goto_main_box,
            btn_login_box,
        )
        right_split_box.add(
            btn_goto_user_registration_box,
        )

    def goto_main_box_btn_handler(self, widget: toga.Widget) -> None:
        """Go to Main box, button handler."""
        self.app.main_window.content = self.app.main_box

    def goto_user_registration_box_btn_handler(
        self, widget: toga.Widget
    ) -> None:
        """Go to User Registration box, button handler."""
        self.app.main_window.content = self.user_registration_box

    def goto_login_box_btn_handler(self, widget: Widget) -> None:
        """Go to Log in box, button handler."""
        self.app.main_window.content = self.login_box
