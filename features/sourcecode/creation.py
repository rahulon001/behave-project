from features.constants import helpercodes
import os, json, csv
import time
from features.constants.api_parameters import Set_url
from features.constants.api_parameters import Set_body
from features.constants.api_parameters import Set_headers
from features.constants.api_parameters import Set_request

from datetime import datetime
constants = {}
now = datetime.now()
path = os.path.dirname(__file__)


def deleting_address_info():
    helpercodes.deleting_address_info()


def create_multiple_merchants(merchants_num, branches_num, radius_branch):
    constants['merchant_list'] = []
    for _ in range(merchants_num):
        helpercodes.login_to_cms()
        time.sleep(1)
        # Creating merchants
        Set_body.modify_and_set_data_files('data_add_merchants', 'file_add_merchants')
        Set_url.modify_and_set_url('add_merchant', 'POST')
        Set_headers.modify_and_set_headers('multipartFormDataWithAntiForgery')
        constants['response_header'], constants['response_full'], constants['response_text'], constants['latency'] = \
            Set_request.raise_request_multipart_secure('POST')
        constants['merchant_list'].append(constants['response_text'])

        helpercodes.coordinate_distributions(constants['response_text'], branches_num, radius_branch)
        # creating branches for the merchants
        Set_body.modify_and_set_data_files('data_add_branches', 'file_add_branches')
        Set_url.modify_and_set_url('add_merchant_branch', 'POST')
        Set_headers.modify_and_set_headers('multipartFormDataWithAntiForgery')
        Set_request.raise_request_multipart_secure('POST')
    # print(constants['merchant_list'])


def create_merchant_group():
    helpercodes.login_to_cms()
    Set_body.modify_and_set_data_files('create_merchant_group', None, constants['merchant_list'])
    Set_url.modify_and_set_url('create_merchant_group', 'POST')
    Set_headers.modify_and_set_headers('secureJson')
    Set_request.raise_request_multipart_secure('POST')


def create_multiple_coupons(coupon_num):
    coupon_id_lst = []
    for _ in range(coupon_num):
        helpercodes.login_to_cms()
        Set_headers.modify_and_set_headers("multipartFormDataWithAntiForgery")
        data, file, url = helpercodes.assign_coupon_body()
        Set_url.modify_and_set_url(url, 'POST')
        Set_body.modify_and_set_data_files(data, file)
        constants['response_header'], constants['response_full'], constants['response_text'], constants['latency'] \
            = Set_request.raise_request_multipart_secure('POST')
        coupon_id = (json.loads(constants['response_text']))['id']
        coupon_id_lst.append(coupon_id)
    # print(coupon_id_lst)
    constants['coupon_id_lst'] = coupon_id_lst
        # helpercodes.create_coupon_id_lst_csv(coupon_id_lst)


# def deleting_coupon_list():
#     helpercodes.deleting_coupon_list()


def create_campaigns():
    helpercodes.login_to_cms()
    helpercodes.set_coupon_list(constants['coupon_id_lst'])
    Set_body.modify_and_set_data_files('couponCampaignCreation', None, constants['coupon_id_lst'])
    Set_url.modify_and_set_url('couponCampaignCreation', 'POST')
    Set_headers.modify_and_set_headers('secureJson')
    Set_request.raise_request_multipart_secure('POST')

#helpercodes.set_coupon_list(constants['coupon_lst'])