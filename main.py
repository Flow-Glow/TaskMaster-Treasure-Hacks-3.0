# Path: Main.py
from . import modules
import flet
from flet import Page

def main(page: Page):
    page.title = "Task Master"
    page.horizontal_alignment = "center"
    page.update()

flet.app(target=main)
