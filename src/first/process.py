"""
Process for message use
"""

# Modules
from src.utils import jsonfile_to_dict

# Constants
file_path_in = 'src/first/in.json'


def run():
    """Run process"""
    data = jsonfile_to_dict(file_path_in)
