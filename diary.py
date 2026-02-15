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
from win32comext.axscript.client.error import FormatForAX
import sqlite3
import pandas as pd

class DiaryApp (App):
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    def flushLayout(self, *args, **kwargs):
        self.mainlayout.clear_widgets()
        self.mainlayout.add_widget(self.narrator)
        self.narrator.text = ""

    def build(self):
        return self.MainMenu()

    def MainMenu(self):
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
        self.narrator.text = (f"Hello new user! Kindly key in "
                              f"a username, full name and password.")
        Logger.debug("Registering new user")
        Reg_Form_Layout = GridLayout(
            pos_hint={'center_x': 0.5,},
            cols = 2,
            spacing = dp(12),
            size_hint=(0.8, 0.8),
            row_force_default=True,
            row_default_height = dp(27),
        )
        userinput = {}
        for key in ['Username','Password','Full name']:
            userinput[key] = TextInput()
            Reg_Form_Layout.add_widget(
                Label(
                    text=f'{key}: ',
                    size_hint_x=None,
                    # size_hint_y=0,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    valign='center', halign='center',
                )
            )

            Reg_Form_Layout.add_widget( userinput[key])

        returnButton, submitButton = [
            Button(text="Back to Main Menu",
                   size_hint=(0.15, 0.15),
                   pos_hint={'center_x': 1/4, 'center_y': 1/4},
                   valign='center', halign='center'
                   ),

            Button(text='Submit',
                   size_hint=(0.15, 0.15),
                   pos_hint={'center_x': 3/4, 'center_y': 1/4},
                   valign='center', halign='center',
                   )
        ]
        returnButton.bind(on_press= self.build)
        submitButton.bind(on_press = self.RegisterNewUser)

        for button in [returnButton, submitButton]:
            button.text_size = button.size

        for widget in [returnButton, submitButton, Reg_Form_Layout]:
            self.mainlayout.add_widget(widget)

        if all(userinput.values()): self.check_input(userinput)

    def LoginCurrentUser(self, *args, **kwargs):
        self.flushLayout()
        self.narrator.text = "Kindly key in login credentials."

        LoginForm_Layout = GridLayout(
            pos_hint={'center_x': 0.5, 'y': 0},
            cols=2,
            size_hint=(0.8, 0.8),
            row_force_default=True,
            row_default_height=dp(48),
        )

    def check_input(self, profile, *args, **kwargs):
        print(profile)
        ProfileMatch = False
        self.ActiveUser = dict()
        for x in profile.values():
            self.cursor.execute("SELECT * FROM users WHERE UserName=?", (profile.get('Username'),))
            rows = self.cursor.fetchall()
        self.conn.close()

        if ProfileMatch and kwargs.get('mode',"") == 'login':
            match = False
        elif kwargs.get('mode',"") == 'register':
            match = True
        else: return False

    def Dashboard(self, *args, **kwargs):
        self.flushLayout()
        Logger.debug("Tracking: user logged in successfully with details:\n ")
        LogoutButton, ViewDiaryButton, ChangePasswordButton = [
            Button(text=buttontext) for buttontext in [
                "Log Out", "View Diary", "Change Password"
            ]
        ]

        ViewDiaryButton.bind(on_press=self.Diary) 

    def Diary(self, *args, **kwargs):
        self.flushLayout()
        self.narrator.text = "Diary entries: "
        self.Display = TextInput(multiline=True)

        self.narrator.text = "Welcome to Diary Repo!"
        # For Ryan to give the View Diary Records

if __name__ == '__main__':
    DiaryApp().run()
