import threading as th

class TimeTracker():
    def __init__(self, configuration):
        self.configuration = configuration
        self.id = configuration['Id']
        self.name = configuration['Name']

    def name(self):
        return self.name
    
    def start_tracking(self):
        active = True

class TrackerProcess(th.Thread):
    """Primary process for the time tracking backend."""
    def __init__(self, configuration):
        super().__init__(self, target=execute)
        self.trackers = {}
        for tracker_config in configuration['Trackers']:
            tracker = TimeTracker(tracker_config)
            self.trackers[tracker.name] = tracker

    def register_input_pipe(self, input_pipe):


    def execute(self):
        while not self.stopped:
