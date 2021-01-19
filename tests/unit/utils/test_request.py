"""
Test Utils of request
"""

# Libraries
from unittest.mock import Mock

# Modules
from src.utils import api_request

requests = Mock()


def test_request(mocker):
    """Test request to send petition"""
    expected = {
        'status': 200,
        'encoding': 'utf-8',
        'response': {
            'data': 'ok'
        }
    }

    def log_request(url, *args, **kwargs):
        print('url - ', url)
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.encoding = 'utf-8'
        response_mock.json.return_value = {
            'data': 'ok',
        }
        return response_mock

    mocker.patch(
        'requests.post',
        log_request
    )
    url = 'http://localhost:1000/routes'
    data = {
        'data': 'ok'
    }
    response = api_request(
        url,
        data=data,
        method='post'
    )
    assert expected == response
