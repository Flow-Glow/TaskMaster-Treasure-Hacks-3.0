"""
Instance of the application
"""

from modules.task import Task
import flet as ft


class App(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()

    def build(self):

        self.title = ft.Text(value="TaskMaster", style="displayLarge",
                             height=100, color=ft.colors.CYAN_300, font_family="Consolas")
        self.task_input_field = ft.TextField(
            hint_text="Add your task", autofocus=True, width=500
        )
        self.add_button = ft.FloatingActionButton(
            icon=ft.icons.ADD, shape=ft.CircleBorder(), bgcolor=ft.colors.CYAN_300, on_click=self.on_add_button_clicked
        )

        return ft.Column(controls=[
            # First row for title
            ft.Row(
                [self.title],
                alignment="center"),
            # Second for the inputting task
            ft.Row(
                [self.task_input_field, self.add_button],
                alignment="center")
        ])

    def on_add_button_clicked(self, e):
        if not self.task_input_field.value:
            # If the user didn't input anything display an error
            self.task_input_field.error_text = "Please enter your task"
            self.update()
        else:
            # Create a task instance
            new_task = Task()
            # Add the new task to the page
            self.controls.append(new_task)
            # Remove
            self.task_input_field.current = ""
            self.update()
            self.task_input_field.current.focus()
