# #Created By Rahul Ranjan on 24/06/2018.
from behave import *
from features.sourcecode import reliance_retail

@given(u'I am verifying "{api_name}" api with url "{url}"')
def step_impl(context, api_name, url):
    pass


@when(u'Set URL for "{url_endpoint}" for "{http_request_type}" request')
def step_impl(context, url_endpoint, http_request_type):
    reliance_retail.set_url(url_endpoint, http_request_type)


@when(u'Set body for "{body}"')
def step_impl(context, body):
    reliance_retail.modify_set_simple_body(body)


@when(u'set header for "{header}"')
def step_impl(context, header):
    reliance_retail.set_header(header)


@when(u'Raise "{http_request_type}" request')
def step_impl(context, http_request_type):
    reliance_retail.request_raise(http_request_type)


@when(u'Set file for "{redeem_coupon}"')
def step_impl(context, redeem_coupon):
    reliance_retail.coupon_code_redemption(redeem_coupon)


@when(u'remove mandatory parameter "{parameters}" from promo body.')
def step_impl(context,parameters):
    reliance_retail.change_mandatory_params(parameters)


@then(u'Valid HTTP response should be received')
def step_impl(context):
    reliance_retail.validate_response()



@then(u'Response http code should be "{response_code}"')
def step_impl(context, response_code):
    reliance_retail.expected_response(response_code)


@then(u'Response HEADER content type should be "{response_header_Type}"')
def step_impl(context, response_header_Type):
    reliance_retail.expected_header_content_type(response_header_Type)


@then(u'Response BODY should not be null or empty')
def step_impl(context):
    reliance_retail.check_response_body()


@when(u'Create {num:d} promo to be converted.')
def step_impl(context, num):
    reliance_retail.create_promo(num)


@when(u'I am logging in to CMS')
def step_impl(context):
    reliance_retail.login_to_cms()


@when(u'set parameters for "{parameters}"')
def step_impl(context, parameters):
    reliance_retail.set_parameter(parameters)


@when(u'Set data "{data}" and file "{file}" for api')
def step_impl(context, data, file):
    reliance_retail.set_body_data_file(data, file)


@when(u'Raise "{http_request_type}" request for secure api')
def step_impl(context, http_request_type):
    reliance_retail.raise_request_multipart_secure(http_request_type)


@Then(u'Promo ID should be assigned to coupon ID.')
def step_impl(context):
    reliance_retail.promo_id_to_coupon_id()


@when(u'Raise "{http_request_type}" HTTP request with files and data.')
def step_impl(context, http_request_type):
    reliance_retail.raise_request_multipart_secure(http_request_type)


@when(u'Raise "{http_request_type}" HTTP request with file.')
def step_impl(context, http_request_type):
    reliance_retail.raise_request_multipart_file_only(http_request_type)


@when(u'Set header for "{header}" linking to user "{num}" with phone number "{phone_num}".')
def step_impl(context,header,num,phone_num):
    reliance_retail.set_header(header,phone_num)