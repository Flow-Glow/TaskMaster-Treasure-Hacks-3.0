"""
A class to represent a task
"""

import flet as ft


class Task(ft.UserControl):

    def __init__(self, task_name, duration, remove_func) -> None:
        super().__init__()
        self.task_name = task_name
        self.task_duration = duration
        self.remove = remove_func

    def build(self):
        self.task_checkbox = ft.Checkbox(
            label=f"{self.task_name} - {int(self.task_duration)} minutes")

        # Display the task to the user with the option to edit or delete
        self.display_task = ft.Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                # Display the checkbox
                self.task_checkbox,
                # Display the edit and delete icon
                ft.Row(
                    spacing=0,
                    controls=[
                        # Edit icon
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit",
                            icon_color=ft.colors.BLACK,
                        ),
                        # Delete Icon
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete",
                            icon_color=ft.colors.RED,
                            on_click=self.on_remove_task_clicked
                        ),
                    ],
                ),
            ],
        )
        return ft.Column(controls=[self.display_task])

    def on_remove_task_clicked(self, e):
        self.remove(self)
