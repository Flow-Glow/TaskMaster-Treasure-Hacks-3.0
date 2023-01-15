"""
A class to represent a task
"""

import flet as ft
from modules.Utils import fb


class Task(ft.UserControl):

    def __init__(self, task_name, duration, remove_func, username) -> None:
        super().__init__()
        self.task_name = task_name
        self.task_duration = duration
        self.remove = remove_func
        self.username = username
        self.firebase = fb()
        if self.task_duration is None:
            self.task_duration = 10
            return

    def build(self):

        self.task_checkbox = ft.Checkbox(
            label=f"{self.task_name} - {int(self.task_duration)} minutes")
        self.edit_name = ft.TextField(autofocus=True, width=500, height=60)
        self.edit_duration = ft.Slider(
            min=1, max=60, divisions=59, label="Duration {value} minutes", width=250, value=self.task_duration)
        self.pb = ft.ProgressBar()

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
                            on_click=self.on_edit_clicked
                        ),
                        # Delete Icon
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete",
                            icon_color=ft.colors.RED,
                            on_click=self.on_remove_task_clicked
                        ),
                        # Start Icon
                        ft.IconButton(
                            ft.icons.PLAY_CIRCLE,
                            tooltip="Start Timer",
                            icon_color=ft.colors.GREEN,
                            on_click=self.on_start_clicked
                        )

                    ],
                ),
            ],
        )

        # A form that is only visible when the user want to edit the task
        self.edit_view = ft.Row(
            visible=False,
            alignment="center",
            vertical_alignment="center",
            controls=[
                ft.Column(controls=[
                    self.edit_name,
                    ft.Row(controls=[ft.Text("Set new Duration: "),
                                     self.edit_duration]),
                    ft.IconButton(
                        icon=ft.icons.SAVE,
                        icon_color=ft.colors.BLUE,
                        tooltip="Save",
                        on_click=self.on_save_clicked

                    )
                ]
                )
            ]
        )

        # A timer that is only visible when the user start the task
        self.timer_view = ft.Column(controls=
            [ft.Text(self.task_name), self.pb], visible=False)

        # Return the controls
        return ft.Column(controls=[self.display_task, self.edit_view, ft.Column([self.timer_view])])

    def on_remove_task_clicked(self, e):
        self.remove(self)

    def on_edit_clicked(self, e):
        self.edit_name.value = self.task_name
        self.display_task.visible = False
        self.edit_view.visible = True
        self.update()

    # Change the label of the checkbox after edited
    def on_save_clicked(self, e):
        self.task_checkbox.label = f"{self.edit_name.value} - {int(self.edit_duration.value)} minutes"
        self.display_task.visible = True
        self.edit_view.visible = False
        data = dict(self.firebase.get_data(self.username))
        for i in range(len(data["Tasks"])):
            if data["Tasks"][i][0] == self.task_name:
                data["Tasks"][i][0] = self.edit_name.value
                data["Tasks"][i][1] = self.edit_duration.value
                break
        self.firebase.update_data(self.username, dict(data))
        self.update()

    def on_start_clicked(self, e):
        self.timer_view.visible = True
        self.update()
