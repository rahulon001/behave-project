# Created By Rahul Ranjan on 26/08/2018.
from features.constants import helpercodes
constants = {}


def request_raise(http_request_type):
    constants['response_header'], constants['response_full'], constants['response_text'], constants['latency'] = \
        helpercodes.raise_request(http_request_type)
    print("Latency for the API is:", constants['latency'])
    print("Response is ", constants['response_full'])
    return constants['response_header'], constants['response_full'], constants['response_text'], constants['latency']


def raise_request_multipart_secure(http_request_type):
    constants['response_header'], constants['response_full'], constants['response_text'], constants['latency'] = \
        helpercodes.raise_request_multipart_secure(http_request_type)
    print("Latency for the API is:", constants['latency'])
    print("Response is ", constants['response_full'])
    # print("#1"*50,constants['response_text'])
    return constants['response_header'], constants['response_full'], constants['response_text'], constants['latency']


def raise_request_multipart_file_only(http_request_type):
    constants['response_header'], constants['response_full'], constants['response_text'], constants['latency'] = \
        helpercodes.raise_request_multipart_file_data(http_request_type)
    print("Latency for the API is:", constants['latency'])
    print("Response is ", constants['response_full'])
    return constants['response_header'], constants['response_full'], constants['response_text'], constants['latency']


def raise_request_with_parameters(http_request_type):
    constants['response_header'], constants['response_full'], constants['response_text'], constants['latency'] = \
        helpercodes.raise_request_with_parameters(http_request_type)
    print("Latency for the API is:", constants['latency'])
    print("Response is ", constants['response_full'])
    return constants['response_header'], constants['response_full'], constants['response_text'], constants['latency']


