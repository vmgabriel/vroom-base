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
