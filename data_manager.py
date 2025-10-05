import json
from datetime import datetime

DATA_FILE = 'donations.json'

def load_data():
    """
    Loads donation data from the JSON file.
    Initializes a new data structure if the file doesn't exist.
    Returns:
        dict: The loaded data dictionary with 'donations' and 'inventory' keys.
    """
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Create a new, empty data structure if file is not found or is invalid
        data = {
            'donations': [],
            'inventory': {},
            'distributions': []
        }
    return data

def save_data(data):
    """
    Saves the provided data dictionary to the JSON file.
    """
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)