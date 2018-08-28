# Created By Rahul Ranjan on 26/08/2018.

from features.constants.urls import urlDict
from features.constants import helpercodes

constants = {}


def modify_and_set_url(url_endpoint, http_request_type, *args):
    constants['http_request_type'] = http_request_type
    constants['url_endpoint'] = url_endpoint
    if url_endpoint == "deletePromo":
        constants['api_post'] = (urlDict.get(url_endpoint)+str(helpercodes.get_random_num_generator()))
    elif url_endpoint == "CouponCodeCount":
        constants['api_post'] = (urlDict.get(url_endpoint))+str(helpercodes.get_coupon_list()[0])+"/codes/count"
    elif url_endpoint == "redeemApiClientSide":
        constants['api_post'] = (urlDict.get(url_endpoint))+str(helpercodes.get_coupon_list()[0])
    elif url_endpoint == 'couponCodeDistributionAPI':
        constants['api_post'] = (urlDict.get(url_endpoint))+str(helpercodes.get_coupon_list()[0])+'/redeem'
    else:
        constants['api_post'] = (urlDict.get(url_endpoint))
    helpercodes.set_url(constants['api_post'])
