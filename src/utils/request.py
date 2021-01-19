"""
Request configuration
"""

# Libraries
import json
import requests


def valid_type(_type: str) -> dict:
    """Convert to valid type"""
    if _type == 'json':
        return {
            'Content-Type': 'application/json'
        }
    return {}


def send_request(
        url: str,
        data: dict = None,
        params: dict = None,
        method: str = 'get',
        content: str = 'json'
) -> dict:
    """
    Request configuration to send
    url: [required] - url to send
    data: { default: None } - data to send
    method: { default: 'get' } - method to send
    params: { default: None } - params to send
    content: { default: 'json' } - content to send

    return {
      'status': int -> status code,
      'encoding': str -> encoding output,
      'response': dict -> output of request,
    }
    """
    headers = {}
    headers = {
        **headers,
        **valid_type(content)
    }
    _r = None
    try:
        if method == 'get':
            _r = requests.get(
                url,
                params=params,
                headers=headers,
            )
        if method == 'post':
            _r = requests.post(
                url,
                data=data if content != 'json' else json.dumps(data),
                params=params,
                headers=headers,
            )
        if _r is None:
            raise Exception('Not Method Valid')
        return {
            'status': _r.status_code,
            'encoding': _r.encoding,
            'response': _r.json(),
        }
    except Exception as exc:
        raise exc
