"""
Process for message use
"""

# Modules
import json
from src.config import configuration as config
from src.utils import jsonfile_to_dict, api_request, dict_to_file

# Constants
file_path_in = 'src/second/in.json'
out_file = 'src/second/out.json'


def run():
    """Run process"""
    url = config['server']['host_server_vroom']

    data = jsonfile_to_dict(file_path_in)
    response = api_request(url, data=data, method='post')
    dict_to_file(out_file, response)

    #print(json.dumps(response, indent=2))
