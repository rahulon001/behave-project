# Created By Rahul Ranjan on 26/08/2018.

from features.constants import helpercodes
from features.constants.apiBody import headerType

constants = {}


def modify_and_set_headers(header, phone_num=None):
    if header in ("multipartFormDataWithAntiForgery", "secureJson"):
        constants['api_request_Header'] = helpercodes.edit_header(headerType.get(header))
    elif header in "couponCodeDistributionAPI":
        constants['api_request_Header'] = (headerType.get(header))
        constants['api_request_Header']['x-loginid'] = phone_num
    elif header in ('Category', 'Favourite', 'AllCoupons'):
        constants['api_request_Header'] = (headerType.get(header))
        constants['api_request_Header']['Authorization'] = 'Bearer '+helpercodes.access_token()
    else:
        constants['api_request_Header'] = (headerType.get(header))
    helpercodes.set_header(constants['api_request_Header'])
