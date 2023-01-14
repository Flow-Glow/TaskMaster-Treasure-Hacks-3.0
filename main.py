# Path: Main.py
import flet
from modules.application import App
from flet import Page
import time


def main(page: Page):
    page.title = "Task Master"
    page.horizontal_alignment = "center"
    page.update()

    # create an instance of hell the app
    app = App()
    page.add(app)



if __name__ == "__main__":
    flet.app(target=main)
