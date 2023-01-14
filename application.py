"""
Instance of the application
"""

import flet as ft
from task import *

class App(ft.UserControl):

    def build(self):
        self.task_input_field = ft.TextField(hint_text="Add your task", autofocus=True, width=500)
        return ft.Column(controls=[
            #First row for title
            ft.Row([ft.Text(value="Todos", style="displayLarge")], alignment="center"),
            #Second for for the inputting task
            ft.Row([self.task_input_field], alignment="center"),
        ])
