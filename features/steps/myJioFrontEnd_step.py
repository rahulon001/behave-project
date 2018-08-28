from behave import *
from features.sourcecode import myJioFrontEnd

@when(u'I am logging in for access token')
def step_impl(context):
    myJioFrontEnd.set_access_token()

@when(u'Raise "{http_request_type}" request with parameters')
def step_impl(context, http_request_type):
    myJioFrontEnd.raise_request_with_parameters(http_request_type)

