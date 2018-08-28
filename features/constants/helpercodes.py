# Created By Rahul Ranjan on 24/06/2018.
import random, os, json, string, math, csv, time
import requests
import pandas as pd
from requests import Session
from features.constants.urls import urlDict
from features.constants.apiBody import couponDetails, merchant_details

constants = {}
s = Session()
path3 = os.path.dirname(__file__)
# print("Path3 for helper is ", path3)


def set_url(api_post):
    # print(api_post)
    constants['api_post'] = api_post


def set_body(api_body):
    # print(api_body)
    constants['api_Body'] = api_body


def set_header(api_request_header):
    constants['api_request_Header'] = api_request_header


def set_parameter(set_parameters):
    constants['setParameters'] = set_parameters


def set_file_data(file, data):
    constants['api_file_multipart'] = file
    constants['api_data_multipart'] = data


def edit_header(header):
    if 'x-anti-forgery' in header:
        constants['api_request_Header_antiForge'] = header
        constants['api_request_Header_antiForge']['x-anti-forgery'] = constants['xAntiForgery']
        return constants['api_request_Header_antiForge']

###################


def raise_request(http_request_type):

    if 'GET' == http_request_type:
        response_full = requests.get(url=constants['api_post'],
                                     headers=constants['api_request_Header'],
                                     params=constants['setParameters'])
        constants['response_full'] = response_full
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()

    elif 'POST' == http_request_type:
        response_full = requests.post(url=constants['api_post'],
                                      data=constants['api_Body'],
                                      headers=constants['api_request_Header'])
        constants['response_full'] = response_full
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()

    elif 'PUT' == http_request_type:
        response_full = requests.put(url=constants['api_post'],
                                     data=constants['api_Body'],
                                     headers=constants['api_request_Header'])
        constants['response_full'] = response_full
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()

    elif 'DELETE' == http_request_type:
        response_full = requests.delete(url=constants['api_post'])
        constants['response_full'] = response_full
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()


def raise_request_with_parameters(http_request_type):

    if 'GET' == http_request_type:
        response_full = requests.get(url=constants['api_post'],
                                     headers=constants['api_request_Header'],
                                     params=constants['setParameters'])
        constants['response_full'] = response_full
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()

    elif 'POST' == http_request_type:
        response_full = requests.post(url=constants['api_post'],
                                      data=constants['api_Body'],
                                      headers=constants['api_request_Header'],
                                      params=constants['setParameters'])
        constants['response_full'] = response_full
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()


def raise_request_multipart_secure(http_request_type):
    # print(constants['api_post'])
    # print(constants['api_file_multipart'])
    # print(constants['api_data_multipart'])
    # print(constants['api_request_Header'])
    global s
    if "POST" == http_request_type:
        response_full = s.post(url=constants['api_post'],
                               files=constants['api_file_multipart'],
                               data=constants['api_data_multipart'],
                               headers=constants['api_request_Header'])
        constants['response_full'] = response_full
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()
    elif "GET" == http_request_type:
        response_full = s.get(url=constants['api_post'],
                              params=constants['setParameters'],
                              headers=constants['api_request_Header'])
        constants['response_full'] = response_full
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()


def raise_request_multipart_file_data(http_request_type):
    if "POST" == http_request_type:
        response_full = requests.post(constants['api_post'],
                                      files=constants['api_file_multipart'],
                                      data=constants['api_data_multipart'])
        constants['response_full'] = response_full
        return response_full.headers, response_full, response_full.text, response_full.elapsed.total_seconds()


# login to CMS


def login_to_cms():
    global s
    url = urlDict.get('cmsLogin')
    payload = "username=super5&password=f01d71e6e38fc7d8afec846de6c512ce310dd1bf6ab1003c9a2a93729795295d"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }
    resp = s.post(url, data=payload, headers=headers)
    constants['xAntiForgery'] = str(resp.headers['x-anti-forgery'])
    print(resp)


def access_token():
    url = urlDict.get('MyjioAccessToken')
    payload = {'username': "9945240311", 'password': "jiomoney@2", 'grant_type': "password"}
    headers = {
        'Authorization': "Basic bDd4eDNlODg3NDAzYjVlZDQwZTc4Y2E4ZWRlZjY1Yzg3NTg3OmM2NDU1NjhhOTI3NzQ1YTY5NmUwZTUyZTU4N"
                         "zFiZTgz",
        'Content-Type': "application/x-www-form-urlencoded"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return json.loads(response.text)["access_token"]


def verify_response(expected_response_code):
    constants['expected_response_code'] = expected_response_code
    actual_response_code = constants['response_full'].status_code
    if str(actual_response_code) != str(expected_response_code):
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)


def validate_responcee():
    if None in constants['response_full']:
        raise('Null response received')


def create_couponcode_redeem_file(lst):
    res = []
    data = lst[0]
    for j in range(10):
        res.append(random.randint(1982, 81882882))
    raw_data1 = {'PromotionId': data, 'CouponCode': res}
    raw_data2 = {'CouponCode': res}
    df1 = pd.DataFrame(raw_data1, columns=['PromotionId', 'CouponCode'])
    df2 = pd.DataFrame(raw_data2, columns=['CouponCode'])
    # print("Z"*100,filename)
    df1.to_csv(path3 + '/files/couponcode.csv', index=False)
    # print("G"*100, df1)
    df2.to_csv(path3 + '/files/redemptions.csv', index=False)


def assig_coupon_details():
    foo = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    return couponDetails.get(random.choice(foo))


def assig_merchant_details():
    foo = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    return merchant_details.get(random.choice(foo))


def assign_coupon_body():
    choice = {
            'A': ('data_add_coupon_pull_merchant_type_flat_discount_on_sku',
                  'file_add_coupon_pull_merchant_type_flat_discount_on_sku',
                  'add_coupon_pull_merchant_type'),        # add_coupon_pull_merchant_type_flat_discount_on_sku_or_type
            'B': ('data_add_coupon_pull_merchant_type_Free_SKUs_on_Bill',
                  'file_add_coupon_pull_merchant_type_Free_SKUs_on_Bill',
                  'add_coupon_pull_merchant_type'),        # add_coupon_pull_merchant_type_Free_SKUs_on_Bill__or_type
            'C': ('data_add_coupon_pull_merchant_type_Free_SKUs_on_SKUs',
                  'file_add_coupon_pull_merchant_type_Free_SKUs_on_SKUs',
                  'add_coupon_pull_merchant_type'),        # add_coupon_pull_merchant_type_Free_SKUs_on_SKUs__or_type
            'D': ('data_add_coupon_pull_merchant_type_flat_discount',
                  'file_add_coupon_pull_merchant_type_flat_discount',
                  'add_coupon_pull_merchant_type'),        # add_coupon_pull_merchant_type_flat_discount
            'E': ('data_add_coupon_pull_merchant_type_Percentage_discount_on_SKU',
                  'file_add_coupon_pull_merchant_type_Percentage_discount_on_SKU',
                  'add_coupon_pull_merchant_type'),  # add_coupon_pull_merchant_type_Percentage_discount_on_SKU_or_type
            'F': ('data_add_coupon_pull_merchant_type_Percentage_discount_on_Bill',
                  'file_add_coupon_pull_merchant_type_Percentage_discount_on_Bill',
                  'add_coupon_pull_merchant_type'),  # add_coupon_pull_merchant_type_Percentage_discount_on_Bill_or_type
            'G': ('data_add_coupon_pull_brand_type_flat_discount_on_sku',
                  'file_add_coupon_pull_brand_type_flat_discount_on_sku',
                  'add_coupon_pull_brand_type'),          # add_coupon_pull_brand_type_flat_discount_on_sku__or_type
            'H': ('data_add_coupon_pull_brand_type_Free_SKUs_on_Bill',
                  'file_add_coupon_pull_brand_type_Free_SKUs_on_Bill',
                  'add_coupon_pull_brand_type'),          # add_coupon_pull_brand_type_Free_SKUs_on_Bill__or_type
            'I': ('data_add_coupon_pull_brand_type_Free_SKUs_on_SKUs',
                  'file_add_coupon_pull_brand_type_Free_SKUs_on_SKUs',
                  'add_coupon_pull_brand_type'),          # add_coupon_pull_brand_type_Free_SKUs_on_SKUs__or_type
            'J': ('data_add_coupon_pull_brand_type_flat_discount',
                  'file_add_coupon_pull_brand_type_flat_discount',
                  'add_coupon_pull_brand_type'),          # add_coupon_pull_brand_type_flat_discount
            'K': ('data_add_coupon_pull_brand_type_Percentage_discount_on_SKU',
                  'file_add_coupon_pull_brand_type_Percentage_discount_on_SKU',
                  'add_coupon_pull_brand_type'),    # add_coupon_pull_brand_type_Percentage_discount_on_SKU__or_type
            'L': ('data_add_coupon_pull_brand_type_Percentage_discount_on_Bill',
                  'file_add_coupon_pull_brand_type_Percentage_discount_on_Bill',
                  'add_coupon_pull_brand_type'),    # add_coupon_pull_brand_type_Percentage_discount_on_Bill__or_type

            # 'M': ('', '', ''),          # add_coupon_pull_merchant_type_flat_discount_on_sku_and_type
            # 'N': ('', '', ''),          # add_coupon_pull_merchant_type_Free_SKUs_on_Bill__and_type
            # 'O': ('', '', ''),          # add_coupon_pull_merchant_type_Free_SKUs_on_SKUs__and_type
            # 'P': ('', '', ''),          # add_coupon_pull_merchant_type_Percentage_discount_on_SKU__and_type
            # 'Q': ('', '', ''),          # add_coupon_pull_merchant_type_Percentage_discount_on_Bill__and_type
            # 'R': ('', '', ''),          # add_coupon_pull_brand_type_flat_discount_on_sku__and_type
            # 'S': ('', '', ''),          # add_coupon_pull_brand_type_Free_SKUs_on_Bill__and_type
            # 'T': ('', '', ''),          # add_coupon_pull_brand_type_Free_SKUs_on_SKUs__and_type
            # 'W': ('', '', ''),          # add_coupon_pull_brand_type_Percentage_discount_on_SKU__and_type
            # 'X': ('', '', ''),          # add_coupon_pull_brand_type_Percentage_discount_on_Bill__and_type
        }
    foo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    select_coupon = random.choice(foo)
    (data, file, url) = choice.get(select_coupon)
    return data, file, url


def random_char_generator(rang):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(rang))


# This function will make branches_num per city
def coordinate_distributions(merchant_id, branches_num=3, radius_1=50):
    df_cities = pd.read_csv(path3+'/files/branch_coordinates.csv')  # file for city coordinates
    a_list, b_list, c_list, d_list, e_list, f_list, g_list, h_list, i_list = [], [], [], [], [], [], [], [], []
    for i in range(len(df_cities)):
        radius = random.randint(1, radius_1)                        # m - reasonably accurate for distances < 100km
        branches = random.randint(1, branches_num)                  # varying number of branches in different cities
        center_lat = df_cities['Latitude'][i]                       # latitude of circle center, decimal degrees
        center_lon = df_cities['Longitude'][i]                      # Longitude of circle center, decimal degrees
        zone_lst = ["north", "south", "east", "west"]
        # generate points
        for k in range(branches):
            # compute
            angle = math.pi*2*k/branches
            dx = radius*math.cos(angle)
            dy = radius*math.sin(angle)
            constants['lat'] = center_lat + (180/math.pi)*(dy/6378137)
            constants['lon'] = center_lon + (180/math.pi)*(dx/6378137)/math.cos(center_lat*math.pi/180)
            pin = random.randint(560001, 831012)
            zone = random.choice(zone_lst)
            a_list.append(merchant_id)                              # merchant
            b_list.append(zone)                                     # zone
            c_list.append("Karnataka")                              # state
            d_list.append(df_cities['City'][i])                     # city
            e_list.append(df_cities['City'][i])                     # address
            f_list.append(pin)                                      # pin
            g_list.append(format(float(constants['lat']), ".4f"))   # latitude
            h_list.append(format(float(constants['lon']), ".4f"))   # latitude
            i_list.append(pin)                                      # shop_number
    raw_data = {
            'merchant': a_list,
            'zone': b_list,
            'state': c_list,
            'city': d_list,
            'Address': e_list,
            'PIN': f_list,
            'lat': g_list,
            'lng': h_list,
            'shop-number': i_list}
    df = pd.DataFrame(raw_data)
    with open(path3+'/files/address_info.csv', 'w+') as address_info: # Creating CSV file
        df.to_csv(address_info, index=False)
    del a_list, b_list, c_list, d_list, e_list, f_list, g_list, h_list


def deleting_coupon_list():
    if os.path.exists(path3+'/files/coupon_list.csv'):
        os.remove(path3+'/files/coupon_list.csv')


def deleting_address_info():
    f = open(path3+"/files/address_info.csv", "w+")
    f.close()


# getters and setters
def set_promo_list(promo_list):
    constants["promo_list"] = promo_list


def get_promo_list():
    return constants["promo_list"]


def set_coupon_list(coupon_list):
    constants["coupon_list"] = coupon_list


def get_coupon_list():
    return constants["coupon_list"]


def set_random_num_generator(lower_lmt, upper_lmt):
    constants['random'] = random.randint(lower_lmt, upper_lmt)


def get_random_num_generator():
    return constants['random']


# def create_coupon_id_lst_csv(coupon_id_lst):
#     with open(path3+'/files/coupon_list.csv', "w") as file:
#         print("new file created")
#         out = csv.writer(file, delimiter=',')
#         out.writerows(map(lambda x: [x], coupon_id_lst))
#         create_coupon_id_lst()
#
#
# def create_coupon_id_lst():
#     lst = []
#     with open(path3+'/files/coupon_list.csv') as my_file:   # code for campaign creation
#         for row in my_file:
#             row = row.strip()
#             if row:
#                 lst.append(row)
#         return lst


# if __name__ == "__main__":
    # coordinate_distributions(merchant_id=23926, branches_num=1, radius_1=50)
