"""
Utils package
"""

# Modules
from src.utils import (
    json,
    request,
)


jsonfile_to_dict = json.load_file
dict_to_file = json.to_file
api_request = request.send_request
