from features.constants import helpercodes
from features.constants.api_parameters import Set_request

constants = {}


def raise_request_with_parameters(http_request_type):
    constants['response_header'], constants['response_full'], constants['response_text'], constants['latency'] = \
        Set_request.raise_request_with_parameters(http_request_type)


def set_access_token():
    helpercodes.access_token()
