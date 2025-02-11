import tkinter as tk
from frontend.ui_elements import ToggleButton


class TrackerWidget(tk.Frame):
    """Represents a time tracker widget."""
    # super().__init__()
    def __init__(self, parent, name, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.name = name
        self.status = 'Pending'

        self.button_start_stop = ToggleButton(self, 'stop', 'start', self.start_tracking, self.stop_tracking)
        self.button_start_stop.grid(column=0, row=0)
        self.label_name = tk.Label(self, text=self.name)
        self.label_name.grid(column=1, row=0)
        self.label_status = tk.Label(self, text=self.status)
        self.label_status.grid(column=2, row=0)


    def start_tracking(self):
        self.status = 'Started'
        self.label_status.config(text=self.status)

    def stop_tracking(self):
        self.status = 'Stopped'
        self.label_status.config(text=self.status)




def configure(parent, configuration=None):
    """Creates the frontend layout and primary components."""

    tracker_frame = tk.Frame(parent)
    button_new_tracker = tk.Button(parent, text = 'New Tracker', command=add_tracker(tracker_frame, tracker_created))
    button_new_tracker.pack()

    tracker_frame.pack()
    if configuration and 'Trackers' in configuration:
        for tracker in configuration['Trackers']:
            tracker_view = TrackerWidget(tracker_frame, tracker['Name'])
            tracker_view.pack()


def add_tracker(parent, callback):
    popup = tk.Toplevel()
    popup.title('Create new tracker')
    label_name = tk.Label(parent, "Tracker Name:")
    label_name.grid(column=0, row=0)
    input_name = tk.Entry(parent, )
    input_name.grid(column=1, row=0)
    button_ok = tk.Button(parent, text='Ok', command=callback(parent, input_name.get))

    button_cancel = tk.Button(parent, text='Cancel', command=popup.destroy)

def tracker_created(parent, get_name):
    name = get_name()
    tracker = 
    
    




def initialize_frontend(configuration=None):
    """Initializes the frontend application."""
    # Create application context
    window = tk.Tk()
    window.title("Time Tracker")
    window.geometry('350x200')

    configure(window, configuration)

    return window

def run_frontend(window):
    """Runs the given frontend window."""
    # Run main window
    window.mainloop()