import json


def get_data_from_json(name):
    """Function to retrieve data from a json file."""
    with open(name, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_executed_operations():
    """Function to retrieve executed operations from operations.json file."""
    executed = []
    count = 0
    data = get_data_from_json('operations.json')
    while len(executed) < 5:
        count -= 1
        if data[count]['state'] == "EXECUTED":
            executed.append(data[count])
    # Returns a list of 5 completed operations sorted by recency
    return executed
