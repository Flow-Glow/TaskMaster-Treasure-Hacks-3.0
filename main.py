# Path: Main.py
import flet
from application import App
from flet import Page


def main(page: Page):
    page.title = "Task Master"
    page.horizontal_alignment = "center"
    page.update()

    # create an instance of the the app
    app = App()
    page.add(app)


flet.app(target=main)
