# Created By Rahul Ranjan on 24/06/2018.
from features.constants.api_parameters import Set_url
from features.constants.api_parameters import Set_body
from features.constants.api_parameters import Set_headers
from features.constants.api_parameters import set_parameters
from features.constants.api_parameters import Set_request
from features.constants import helpercodes
from features.constants.apiBody import apiBodyDict
import json
from datetime import datetime


now = datetime.now()
constants = {}


# json data
def set_url(url_endpoint, http_request_type):
    constants['http_request_type'] = http_request_type
    Set_url.modify_and_set_url(url_endpoint, http_request_type)


# api_body
def modify_set_simple_body(data):
    Set_body.modify_and_set_simple_body(data, constants['http_request_type'])


# Secure_api_body
def set_body_data_file(data, file):
    Set_body.modify_and_set_data_files(data, file)


# header
def set_header(header, phone_num=None):
    Set_headers.modify_and_set_headers(header, phone_num)


# parameters
def set_parameter(params):
    set_parameters.modify_and_set_parameters(params)

# ================================================================================ #


def request_raise(http_request_type):
    constants['response_header'], constants['response_full'], constants['response_text'], constants['latency'] = \
        Set_request.request_raise(http_request_type)


def raise_request_multipart_secure(http_request_type):
    constants['response_header'], constants['response_full'], constants['response_text'], constants['latency'] = \
        Set_request.raise_request_multipart_secure(http_request_type)
    # print("#5"*50, constants['response_text'])


def raise_request_multipart_file_only(http_request_type):
    constants['response_header'], constants['response_full'], constants['response_text'], constants['latency'] = \
        Set_request.raise_request_multipart_file_only(http_request_type)

# ================================================================================ #


def create_promo(num):
    promo_lst = []
    for i in range(num):
        Set_url.modify_and_set_url('couponRetailPromoCreation', 'POST')
        # print(constants['api_post'])
        Set_headers.modify_and_set_headers('applicationJson')
        # print(constants['api_request_Header'])
        Set_body.modify_and_set_simple_body('CreatePromoRelianceRetail', 'POST')
        # print(constants['api_Body'])
        request_raise('POST')
        # print(constants['response_full'])
        promo_lst.append(helpercodes.get_random_num_generator())
        helpercodes.set_promo_list(promo_lst)


def promo_id_to_coupon_id():
    coupon_lst = []
    json_data = json.loads(constants['response_text'])
    for x in helpercodes.get_promo_list():
        for elements in json_data:
            # print(elements['REF_ID'])
            if elements['REF_ID'] == str(x):
                c = elements["COUPON"]
            else:
                continue
            coupon_lst.append(c)
        # constants['coupon_lst'] = couponLst
        constants['coupon_lst'] = [6026, 6953]
        helpercodes.set_coupon_list(constants['coupon_lst'])


def change_mandatory_params(parameters):
    Set_body.change_mandatory_parameters(parameters)


def validate_response():
    helpercodes.validate_responcee()


def expected_response(expected_response_code):
    helpercodes.verify_response(expected_response_code)


def expected_header_content_type(expected_response_content_type):
    actual_response_content_type = constants['response_header']['Content-Type']
    # print(actual_response_content_type)
    if expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + \
                      actual_response_content_type


def check_response_body():
    if None in constants['response_full']:
        assert False, '***ERROR:  Null or none response body received'


def coupon_code_redemption(redeem_coupon):
    constants['api_file_multipart'] = apiBodyDict.get(redeem_coupon)
    # print("F"*100,http_request_body['api_file_multipart'])


def login_to_cms():
    helpercodes.login_to_cms()


# if __name__ == "__main__":
#     modifysetBODY('CreatePromoRelianceRetail')
