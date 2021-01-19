"""
JSon Util
"""

# Libraries
import json


def load_file(name_file: str) -> dict:
    """
    Load a File JSON extension
    name_file: route of file
    return dict -> json
    """
    with open(name_file) as json_file:
        return json.load(json_file)


def to_file(name_file: str, data: dict):
    """
    Send and save file

    name_file: required file to save
    data: required data to save
    """
    print('save - ', name_file)
    with open(name_file, 'w') as out_file:
        json.dump(data, out_file, indent=2)
