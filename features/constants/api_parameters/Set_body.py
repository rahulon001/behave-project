# Created By Rahul Ranjan on 26/08/2018.

import json
import random,csv
from datetime import datetime
from features.constants import helpercodes
from features.constants.apiBody import apiBodyDict
from dateutil.relativedelta import relativedelta

now = datetime.now()
constants = {}


def modify_and_set_simple_body(data, request_type):
    constants['coupon_details'] = helpercodes.assig_coupon_details()
    if data == 'CreatePromoRelianceRetail':
        json_body = apiBodyDict.get(data)
        json_data = json_body['promotions'][0]
        for key, value in json_data.items():
            if key == "REF_ID" and request_type == 'POST':
                helpercodes.set_random_num_generator(689, 77896677)
                json_data["REF_ID"] = str(helpercodes.get_random_num_generator())
                json_data["PROMO_NAME"] = constants['coupon_details']['name']
                json_data["PROMO_CREATION_DATE"] = now.strftime("%Y-%m-%d %H:%M:%S")
                json_data["START_DATE"] = now.strftime("%Y-%m-%d %H:%M:%S")
                json_data["END_DATE"] = (now + relativedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S")
                json_data["ENTITY"][0]['NAME'] = constants['coupon_details']['name1']
                json_data["ENTITY"][0]['CATEGORIES'] = constants['coupon_details']['category']
                json_data["STORE_ID"] = constants['coupon_details']['Merchant']
            elif key == "REF_ID" and request_type == 'PUT':
                break
        constants['api_Body'] = json.dumps(json_body, ensure_ascii=False)
    else:
        body = apiBodyDict.get(data)
        constants['api_Body'] = body

    helpercodes.set_body(constants['api_Body'])


def modify_and_set_data_files(data, file, *args):
    if data == "data_convertPromoToCoupon" and file == "file_convertPromoToCoupon":
        constants['api_file_multipart'] = constants['coupon_details']['image']
        constants['api_data_multipart'] = apiBodyDict.get(data)
        constants['api_data_multipart'] = helpercodes.get_promo_list()
        constants['api_data_multipart1'] = {'promoList[]': constants['api_data_multipart'], 'clientList[]': ['2']}
        helpercodes.set_file_data(constants['api_file_multipart'], constants['api_data_multipart1'])
    elif file == "mapCouponCodeToPromo":
        helpercodes.create_couponcode_redeem_file(helpercodes.get_promo_list())
        constants['api_file_multipart'] = apiBodyDict.get(file)
        helpercodes.set_file_data(constants['api_file_multipart'], None)
    elif file == "redeemCoupon":
        constants['api_file_multipart'] = apiBodyDict.get(file)
        helpercodes.set_file_data(constants['api_file_multipart'], None)
    elif data == 'couponCampaignCreation':
        json_data = apiBodyDict.get(data)
        for _ in json_data.items():
            json_data["name"] = "Automation_Campaign"+now.strftime("%Y-%m-%d %H:%M:%S")
            json_data["startTime"] = now.strftime("%Y-%m-%d %H:%M:%S")
            json_data["endTime"] = (now + relativedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S")
            json_data['lineItems'][0]['coupons'] = helpercodes.get_coupon_list()
        constants['api_data_multipart1'] = json.dumps(json_data, ensure_ascii=False)
        helpercodes.set_file_data(None, constants['api_data_multipart1'])
    elif data == "data_add_merchants" and file == "file_add_merchants":
        constants['merchant_details'] = helpercodes.assig_merchant_details()
        json_data = apiBodyDict.get(data)
        constants['api_file_multipart'] = constants['merchant_details']['image']
        constants['random1'] = helpercodes.random_char_generator(14)
        for _ in json_data.items():
            json_data['masId'] = str(constants['random1'])
            json_data['name'] = str("Auto_merchant_"+constants['random1'])
        constants['api_data_multipart1'] = json_data
        helpercodes.set_file_data(constants['api_file_multipart'], constants['api_data_multipart1'])
    elif(
            data == "data_add_coupon_pull_merchant_type_flat_discount_on_sku" and
            file == "file_add_coupon_pull_merchant_type_flat_discount_on_sku") or \
        (
            data == "data_add_coupon_pull_merchant_type_Free_SKUs_on_Bill" and
            file == "file_add_coupon_pull_merchant_type_Free_SKUs_on_Bill") or \
        (
            data == "data_add_coupon_pull_merchant_type_Free_SKUs_on_SKUs" and
            file == "file_add_coupon_pull_brand_type_Free_SKUs_on_SKUs") or \
        (
            data == "data_add_coupon_pull_merchant_type_flat_discount" and
            file == "file_add_coupon_pull_merchant_type_flat_discount") or \
        (
            data == "data_add_coupon_pull_merchant_type_Percentage_discount_on_SKU" and
            file == "file_add_coupon_pull_merchant_type_Percentage_discount_on_SKU") or \
        (
            data == "data_add_coupon_pull_merchant_type_Percentage_discount_on_Bill" and
            file == "file_add_coupon_pull_merchant_type_Percentage_discount_on_Bill"):

        json_data = apiBodyDict.get(data)
        constants['coupon_details'] = helpercodes.assig_coupon_details()
        constants['api_file_multipart'] = constants['coupon_details']['image']
        for _ in json_data.items():
            json_data['couponStartTime'] = datetime.utcnow().isoformat()
            json_data['couponEndTime'] = datetime.utcnow().isoformat()
            json_data['title'] = constants['coupon_details']['name']
            json_data['source'] = random.choice(['discover', 'prime'])
            json_data['startDate'] = now.strftime("%Y/%m/%d")
            json_data['endDate'] = (now + relativedelta(days=10)).strftime("%Y/%m/%d")
            json_data["validFrom"] = now.strftime("%Y/%m/%d %H:%M:%S")
            json_data["validTo"] = (now + relativedelta(days=10)).strftime("%Y/%m/%d %H:%M:%S")
        constants['api_data_multipart1'] = json_data
        helpercodes.set_file_data(constants['api_file_multipart'], constants['api_data_multipart1'])
    elif(
            data == "data_add_coupon_pull_brand_type_flat_discount_on_sku" and
            file == "file_add_coupon_pull_brand_type_flat_discount_on_sku") or\
        (
            data == "data_add_coupon_pull_brand_type_Free_SKUs_on_SKUs" and
            file == "file_add_coupon_pull_brand_type_Free_SKUs_on_SKUs") or \
        (
            data == "data_add_coupon_pull_brand_type_Free_SKUs_on_Bill" and
            file == "file_add_coupon_pull_brand_type_Free_SKUs_on_Bill") or \
        (
            data == "data_add_coupon_pull_brand_type_flat_discount" and
            file == "file_add_coupon_pull_brand_type_flat_discount") or \
        (
            data == "data_add_coupon_pull_brand_type_Percentage_discount_on_SKU" and
            file == "file_add_coupon_pull_brand_type_Percentage_discount_on_SKU") or \
        (
            data == "data_add_coupon_pull_brand_type_Percentage_discount_on_Bill" and
            file == "file_add_coupon_pull_brand_type_Percentage_discount_on_Bill"):

        json_data = apiBodyDict.get(data)
        constants['coupon_details'] = helpercodes.assig_coupon_details()
        constants['api_file_multipart'] = constants['coupon_details']['image']
        for _ in json_data.items():
            json_data['couponStartTime'] = datetime.utcnow().isoformat()
            json_data['couponEndTime'] = datetime.utcnow().isoformat()
            json_data['title'] = constants['coupon_details']['name']
            json_data['source'] = random.choice(['discover', 'prime'])
            json_data['startDate'] = now.strftime("%Y/%m/%d")
            json_data['endDate'] = (now + relativedelta(days=10)).strftime("%Y/%m/%d")
            json_data["validFrom"] = now.strftime("%Y/%m/%d %H:%M:%S")
            json_data["validTo"] = (now + relativedelta(days=10)).strftime("%Y/%m/%d %H:%M:%S")
        constants['api_data_multipart1'] = json_data
        helpercodes.set_file_data(constants['api_file_multipart'], constants['api_data_multipart1'])
    elif data == 'create_merchant_group':
        merchant_list = args[0]
        json_data = apiBodyDict.get(data)
        json_data['idList'] = merchant_list
        constants['api_data_multipart1'] = json.dumps(json_data)
        helpercodes.set_file_data(None, constants['api_data_multipart1'])
    else:
        constants['api_data_multipart1'] = apiBodyDict.get(data)
        constants['api_file_multipart'] = apiBodyDict.get(file)
        helpercodes.set_file_data(constants['api_file_multipart'], constants['api_data_multipart1'])


def change_mandatory_parameters(parameters):
    data1 = (json.loads(constants['api_Body']))
    if parameters in data1['promotions'][0]:
        data1['promotions'][0].pop(parameters, None)
    constants['api_Body'] = json.dumps(data1, ensure_ascii=False)
    helpercodes.set_body(constants['api_Body'])
