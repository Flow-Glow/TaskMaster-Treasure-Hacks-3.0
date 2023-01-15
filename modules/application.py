"""
Instance of the application
"""

from modules.task import Task
import flet as ft
from modules.Utils import fb
import math


class App(ft.UserControl):

    def __init__(self, username, *args, **kwargs) -> None:
        self.username = username
        super().__init__(*args, **kwargs)
        # App Title
        self.title = ft.Text(value="TaskMaster", size=50,
                             height=100, color=ft.colors.CYAN,
                             font_family="Consolas")
        self.hello = ft.Text(value=f"Welcome {self.username} 👋", size=20,
                             height=30, color=ft.colors.CYAN,
                             font_family="Consolas")
        # A field for the user to input their task
        self.firebase = fb()
        self.task_input_field = ft.TextField(
            hint_text="Add a task and set duration!", autofocus=True, width=500, on_change=self.on_text_field_changed)
        # A button to add task
        self.add_button = ft.FloatingActionButton(icon=ft.icons.ADD, shape=ft.CircleBorder(
        ), bgcolor=ft.colors.CYAN_300, on_click=self.on_add_button_clicked)
        # A column
        self.task_list = ft.Column()
        # A responsive view for time slider
        self.time_slider = ft.Slider(
            min=1, max=60, divisions=59, label="Duration {value} minutes")
        self.time_slider_view = ft.Column(controls=[ft.Text(
            value="Choose duration via slider: "), self.time_slider], visible=False)
        self.data = dict(self.firebase.get_data(self.username))
        self.productivityBar = ft.ProgressBar(
            bgcolor="#eeeeee",
            value=self.data["productivity"],
            height=10,
            tooltip="Productivity Bar",
            expand=True,

        )

    def load_tasks(self):
        if 'Tasks' in self.data.keys():
            for task in self.data["Tasks"]:
                new_task = Task(task[0], task[1], self.delete_task, self.username)
                self.task_list.controls.append(new_task)

    def load_productivity(self):
        self.productivityBar.value = self.data["productivity"]
        self.update()

    def build(self):
        self.load_tasks()

        # This will return what the user see
        return ft.Column(
            width=585,
            controls=[
                # First row for title
                ft.Row([self.title], alignment="center"),
                # top left corner
                # Second row for hello message
                ft.Row([self.hello], alignment="center"),
                ft.Row([self.productivityBar], alignment="center"),
                # Second for the inputting task
                ft.Row([self.task_input_field, self.add_button],
                       alignment="center"),
                # Third row for task duration slider
                ft.Row([self.time_slider_view], alignment="center"),
                # Return self.column, so later we can add tasks below this column
                self.task_list,
                # put the productivity bar at the top right corner

            ])


    def on_add_button_clicked(self, e):
        if not self.task_input_field.value:
            # If the user didn't input anything display an error
            self.task_input_field.error_text = "Please enter your task"
        else:
            # Create a task instance
            new_task = Task(self.task_input_field.value,
                            self.time_slider.value, self.delete_task, self.username)
            # Add the new task to the list
            self.task_list.controls.append(new_task)
            # Remove the input field
            self.task_input_field.value = ""
            self.time_slider_view.visible = False

            self.data["Tasks"] = [[task.task_name, task.task_duration] for task in self.task_list.controls]
        self.firebase.set_data(self.username, self.data)
        self.update()

    # This function detect whenever the user enter anything to make the time slider view visible
    def on_text_field_changed(self, e):
        self.time_slider_view.visible = bool(self.task_input_field.value)

        self.update()

    # Function to remove a task from the list
    def delete_task(self, task: Task):
        self.task_list.controls.remove(task)
        self.data["Tasks"] = [[task.task_name, task.task_duration] for task in
                              self.task_list.controls]

        self.firebase.update_data(self.username, self.data)
        self.update()
