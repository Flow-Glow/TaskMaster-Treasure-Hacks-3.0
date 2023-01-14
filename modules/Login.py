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


class Login(Container):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Container Prop
        self.password = None
        self.username = None
        self.loading = None
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
            pass

    def LoginContainer(self):
        # Login Page Data
        self.username = TextField(label="User name")
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
                    "Login", on_click=self.Login, )
            ], alignment=MainAxisAlignment.CENTER),
            padding=Padding(20, 20, 20, 20),
            margin=Margin(0, 0, 0, 20),
            bgcolor=colors.WHITE10,
            border=border.all(1),
            border_radius=border_radius.all(20),

        )
