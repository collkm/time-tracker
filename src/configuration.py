import json as json
import jsonpickle as jsonp
import os as os
import uuid as uuid


def configure():
    """Loads the application configuration or creates a new configuration directory if none exists."""

    config_path = os.path.join(os.getenv('APPDATA'), 'time-tracker', 'configuration.json')
    # Load or create configuration
    if os.path.exists(config_path):
        return load_configuration(config_path)
    else:
        return create_configuration(config_path)


def load_configuration(config_path):
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config


def create_configuration(config_path):
    """Creates a new default configuration file."""
    configuration = {
        'ReportPath': os.path.join(os.path.dirname(config_path), 'reports'),
        'Trackers': [ TrackerConfiguration('Test Tracker', 'For testing purposes only') ],
    }
    config_json = json.dumps(configuration, indent=4, default=vars)

    if not os.path.exists(os.path.dirname(config_path)):
        os.makedirs(os.path.dirname(config_path))
    with open(config_path, 'w+') as config_file:
        config_file.write(config_json)

    return configuration


class TrackerConfiguration(dict):
    def __init__(self, name, description, **kwargs):
        id = kwargs['id'] if 'id' in kwargs else str(uuid.uuid4())
        dict.__init__(self, Id=id, Name=name, Description=description)