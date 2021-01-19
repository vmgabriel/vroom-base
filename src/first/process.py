"""
Process for message use
"""

# Modules
import json
from src.config import configuration as config
from src.utils import jsonfile_to_dict, api_request

# Constants
file_path_in = 'src/first/in.json'


def run():
    """Run process"""
    url = config['server']['host_server_vroom']

    data = jsonfile_to_dict(file_path_in)
    response = api_request(url, data=data, method='post')

    print('data - ', json.dumps(response, indent=2))
