"""
Server Configuration
"""

# Libraries
import os
from dotenv import load_dotenv


# Load the process
load_dotenv(verbose=True)


configuration = {
    'host_server_vroom': os.getenv('HOST_VROOM_API'),
}
