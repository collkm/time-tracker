import tkinter as tk


class ToggleButton(tk.Button):
    """A toggle button with configurable callback."""

    def __init__(self, parent, on_text='', off_text='', on_command=None, off_command=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.is_on = False
        self.off_text = off_text
        self.on_text = on_text
        self.on_command = on_command
        self.off_command = off_command
        self.config(text = self.off_text, command=self.toggle)

    def toggle(self):
        """
        Toggles the button state and triggers toggle callback.
        If toggled `On`, the `on_command` triggers and `on_text` is displayed.
        If toggled `Off`, the `off_command` triggers and `off_text` is displayed.
        """
        self.is_on = not self.is_on
        if self.is_on:
            self.config(text=self.on_text)
            if self.on_command:
                self.on_command()
        else:
            self.config(text=self.off_text)
            if self.off_command:
                self.off_command()