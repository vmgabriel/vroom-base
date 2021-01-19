"""
Test Module for json
"""

# Libraries
from os import path
from datetime import datetime

# Modules
from src.utils import (
    jsonfile_to_dict,
    dict_to_file,
)

# Constants
test_data = {
        "load": "process",
        "x": 1,
        "y": 2.1,
        "z": [
            1,
            2,
            3
        ],
        "a": True,
        "b": {
            "foo": "baz"
        }
    }

def test_load_file_json():
    """
    Verify load of json
    """
    path_route = 'tests/unit/utils/in.json'
    data = jsonfile_to_dict(path_route)
    assert isinstance(data, dict)
    assert data == test_data


def test_save_to_file():
    """Save a file"""
    output_file = 'tests/unit/utils/'
    output_file += datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    output_file += '-test.json'
    dict_to_file(output_file, test_data)
    assert path.isfile(output_file)
