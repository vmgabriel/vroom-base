"""
Test Module for json
"""

# Modules
from src.utils import jsonfile_to_dict


def test_load_file_json():
    """
    Verify load of json
    """
    path_route = 'tests/unit/utils/in.json'
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
    data = jsonfile_to_dict(path_route)
    assert isinstance(data, dict)
    assert data == test_data
