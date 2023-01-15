from flet import (
    Column,
    Container,
    ElevatedButton,
    Row,
    Text,
    colors,
    MainAxisAlignment,
    Padding,
    border,
    TextField,
    border_radius,
    Margin
)

from modules.application import App
from modules.Utils import fb


class Login(Container):

    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Container Prop
        self.password = None
        self.username = None
        self.loading = None
        self.firebase = fb()
        self.app = app
        self.expand = True
        self.content = Column(
            [
                Row([self.LoginContainer()], alignment=MainAxisAlignment.CENTER)
            ],
            alignment=MainAxisAlignment.CENTER
        )

    def Login(self, e):
        if self.username.value == "" or self.password.value == "":
            self.username.error_text = "Please provide username"
            self.password.error_text = "Please provide password"
            self.update()
            return
        else:
            self.loading.visible = True
            self.update()
            # check if user exists in db
            if self.firebase.check_exist(self.username.value):
                if self.firebase.get_data(self.username.value)["password"] == self.password.value:
                    self.app.remove(self)
                    self.app.add(App(self.username.value))
                else:
                    self.loading.visible = False
                    self.password.error_text = "Wrong password or username already exists"
                self.update()
                return
            else:
                self.firebase.set_data(self.username.value,
                                       {"password": self.password.value, "tasks": {}, "currency": 0, "productivity": 0})
                self.app.remove(self)
                self.app.add(App(self.username.value))
                self.update()


    def LoginContainer(self):
        # Login Page Data
        self.username = TextField(label="Username")
        self.password = TextField(label="Password", password=True)
        title = Container(Text(value="TaskMaster",
                               height=100, color=colors.CYAN,
                               font_family="Consolas", style="displayLarge"), padding=Padding(0, 10, 0, 20))
        self.loading = Container(Text(value="Loading..."), visible=False)
        return Container(
            Column([
                title,
                self.username,
                self.password,
                self.loading,
                ElevatedButton(
                    "Login", on_click=self.Login,autofocus=True)
            ], alignment=MainAxisAlignment.CENTER),
            padding=Padding(20, 20, 20, 20),
            margin=Margin(0, 0, 0, 20),
            bgcolor=colors.WHITE10,
            border=border.all(1),
            border_radius=border_radius.all(20),

        )
