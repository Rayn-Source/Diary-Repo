import itertools
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import *
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.settings import Settings
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.logger import Logger, LOG_LEVELS, LoggerHistory
from kivy.metrics import dp


class DiaryApp (App):
    def flushLayout(self, *args, **kwargs):
        self.mainlayout.clear_widgets()
        self.mainlayout.add_widget(self.narrator)
        self.narrator = ""

    def build(self):
        # Draw the mainlayout, which is float, for size and position hint controls
        self.mainlayout = FloatLayout()

        # Label for informing user, called narrator
        self.narrator = Label(
            size_hint=(0.15, 0.15),
            pos_hint={'center_x': 0.5, 'center_y': 0.9}
        )

        self.narrator.text = "Welcome to Diary Repo!"
        a = itertools.count(0,1)

        loginButton, NewUserButton, ExitButton = [Button(
            text=buttontext,
            size_hint=(0.15, None),
            height=dp(36),
            pos_hint={'center_x': (2*next(a)+1)/6, 'center_y': 0.25}
            ) for buttontext in [ "Login", "New User", "Exit"]
        ]
        loginButton.bind(on_press=self.LoginCurrentUser)
        ExitButton.bind(on_press=lambda _: App.get_running_app().stop())
        NewUserButton.bind(on_press=self.RegisterNewUser)
        for x in [loginButton, NewUserButton, ExitButton]:
            self.mainlayout.add_widget(x)
        self.mainlayout.add_widget(self.narrator)
        return self.mainlayout

    def RegisterNewUser(self, *args, **kwargs):
        self.flushLayout()

        Logger.debug("Registering new user")
        Reg_Form_Layout = GridLayout(
            pos_hint={'center_x': 0.5,},
            cols = 2,
            spacing = dp(12),
            size_hint=(0.8, 0.8),
            row_force_default=True,
            row_default_height = dp(27),
        )

        userinput, inputlist = {}, []
        def fillGrid(newuserattr):
            Reg_Form_Layout.add_widget(
                Label(
                    text=f'{newuserattr}: ', size_hint_x=None,
                    size_hint_y=0.2,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    valign='center', halign='center',
                )
            )
            Input1 = TextInput()
            Reg_Form_Layout.add_widget(TextInput(
                pos_hint={'center_x': 0.5, 'top': 3/4},
                multiline=False,
            ))

        returnButton, submitButton = [
            Button(text="Back to Main Menu",
                   size_hint=(0.15, 0.15),
                   pos_hint={'center_x': 2/5, 'center_y': 1/4},
                   ),
            Button(text='submit',
                   size_hint=(0.15, 0.15),
                   pos_hint={'center_x': 4/5, 'center_y': 1/4},
                   )
        ]
        for button in [returnButton, submitButton]:
            button.texture_size = button.size
        for x in ['Username','Password','Full name']:
            fillGrid(x)
            userinput[x] = ""
            pass
        for widget in [returnButton, submitButton, Reg_Form_Layout]:
            self.mainlayout.add_widget(widget)

    def LoginCurrentUser(self, *args, **kwargs):
        self.flushLayout()
        self.narrator.text = "Kindly key in login credentials!"

        LoginForm_Layout = GridLayout(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            cols=2,
            size_hint=(0.8, 0.8),
            row_force_default=True,
            row_default_height=dp(48),
        )


    def login_ok(self, profile, *args, **kwargs):
        # What would be the item to read?
        pass

    def Dashboard(self, *args, **kwargs):
        Logger.debug("Tracking: user logged in successfully with details:\n ")
        LogoutButton, ViewRecordsButton, ChangePasswordButton = [
            Button(text=buttontext) for buttontext in [
                "Log Out", "View Diary", "Change Password"
            ]
        ]

        # For Ryan to give the View Diary Records


if __name__ == '__main__':
    DiaryApp().run()
