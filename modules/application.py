"""
Instance of the application
"""

from modules.task import Task
import flet as ft


class App(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()

    def build(self):

        # App Title
        self.title = ft.Text(value="TaskMaster", style="displayLarge",
                             height=100, color=ft.colors.CYAN, font_family="Consolas")
        # A field for the user to input their task
        self.task_input_field = ft.TextField(
            hint_text="Add your task and set time below", autofocus=True, width=500, on_change=self.on_text_field_changed)
        # A button to add task 
        self.add_button = ft.FloatingActionButton(icon=ft.icons.ADD, shape=ft.CircleBorder(
        ), bgcolor=ft.colors.CYAN_300, on_click=self.on_add_button_clicked)
        # A column 
        self.columns = ft.Column()
        # Make a responsive view for time slider
        self.time_slider = ft.Slider(min=0, max=60, divisions=60, label="Duration {value} minutes")
        self.time_slider_view = ft.Column(controls=[ft.Text(value="Choose duration via slider: "), self.time_slider], visible=False)

        # This will return what the user see
        return ft.Column(
            width=585,
            controls=[
                # First row for title
                ft.Row([self.title], alignment="center"),
                # Second for the inputting task
                ft.Row([self.task_input_field, self.add_button], alignment="center"),
                # Third row for task duration slider
                ft.Row([self.time_slider_view], alignment="center"),
                # Return self.column so later we can add tasks below this column
                self.columns
            ])

    def on_add_button_clicked(self, e):
        if not self.task_input_field.value:
            # If the user didn't input anything display an error
            self.task_input_field.error_text = "Please enter your task"
            self.update()
        else:
            # Create a task instance
            new_task = Task(self.task_input_field.value)
            # Add the new task below the 'column'
            self.columns.controls.append(new_task)
            # Remove the input field
            self.task_input_field.value = ""
            self.time_slider_view.visible = False
            self.update()

    # This function detect whenever the user enter anything to make the time slider view visible
    def on_text_field_changed(self, e):
        if self.task_input_field.value:
            self.time_slider_view.visible = True
            self.update()
        else:
            self.time_slider_view.visible = False
            self.update()