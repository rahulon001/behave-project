# Created By Rahul Ranjan on 26/08/2018.

baseURL_ = ""

baseURL_1 = "http://localhost:8082"

baseURL_app_ = "https://api-sit.jio.com"


urlDict = \
    {
        'cmsLogin':
            baseURL_+"/v1/cms/login",
        'couponRetailPromoCreation':
            baseURL_+"/v1/cms/coupons/promo/",
        'deletePromo':
            baseURL_+"/v1/cms/coupons/promo/",
        'convertPromoToCoupon':
            baseURL_+"/v1/cms/coupons/promo/convert",
        'couponCodeRedeeming':
            baseURL_+"/coupons/v1/coupons/redemptions",
        'couponCodeMapping':
            baseURL_+"/coupons/v1/coupons/coupon-codes",
        'GetAllCouponIDFromPromoID':
            baseURL_+"/v1/cms/coupons/promo",
        'couponCampaignCreation':
            baseURL_+"/v1/cms/coupon-campaign/",
        'CouponCodeCount':
            baseURL_+"/v1/cms/merchant/23330/coupons/",
        'couponCodeDistributionAPI':
            baseURL_+"/v1/coupons/",
        'creatCouponsPullType':
            baseURL_+"/v1/cms/merchant/23331/coupon",
        'add_merchant':
            baseURL_+"/v1/cms/admin/merchants",
        'add_merchant_branch':
            baseURL_+"/v1/cms/merchant/address/csv",
        "add_coupon_pull_merchant_type":
            baseURL_+"/v1/cms/merchant/6110/coupon",
        "add_coupon_pull_brand_type":
            baseURL_+"/v1/cms/merchant/721/coupon",
        "create_merchant_group":
            baseURL_+"/v1/cms/merchant-group/",
        'redeemApiClientSide':
            baseURL_app_+"/cr/v2/coupons/redeem/",
        'getCouponMyjio':
            baseURL_app_+"/cr/v2/coupons?categoryId=202&start=0&end=1000&version=v4",
        'MyjioAccessToken':
            baseURL_app_+"/jm/auth/oauth/v2/token",
        'MyjioCategory':
            baseURL_app_+"/cr/v2/coupons/category?client=myjio&version=v5",
        'MyjioFavourite':
            baseURL_app_+"/cr/v2/coupons/favorites?version=v5",
        'MyjioAllCoupons':
            baseURL_app_+"/cr/v2/coupons?"
                         "categoryId=1&reductionType=2&lat=12.9716658&"
                         "lng=77.6056825&source=all&version=v5&format=group&start=0&end=10",

    }
