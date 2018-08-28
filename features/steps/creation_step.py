from behave import *
from features.sourcecode import creation


@when(u'refreshing the address_info.csv file')
def step_impl(context):
    creation.deleting_address_info()


@when(u'create {merchants_num:d} merchants each with {branches_num:d} branches within {radius_branch:d} km radius')
def step_impl(context,merchants_num, branches_num, radius_branch):
    creation.create_multiple_merchants(merchants_num, branches_num, radius_branch)


@when(u'create {coupon_num:d} coupons from all types')
def step_impl(context, coupon_num):
    creation.create_multiple_coupons(coupon_num)


@then(u'create the merchant group with the merchant list.')
def step_impl(context):
    creation.create_merchant_group()


@then(u'creating campaigns with all the created coupon IDs')
def step_impl(context):
    creation.create_campaigns()

