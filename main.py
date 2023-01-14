# Path: Main.py
import flet
from modules.application import App
from modules.Login import Login
from flet import Page
import time


def main(page: Page):
    page.title = "Task Master"
    page.horizontal_alignment = "center"
    page.update()

    # login = Login(app=page)
    # page.add(login)
    
    # For testing the application without having to login
    app = App()
    page.add(app)

if __name__ == "__main__":
    flet.app(target=main)
