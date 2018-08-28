#Created By Rahul Ranjan on 24/06/2018.
@test_all
Feature: API testing for Reliance Retail module of coupon
  Scenario Outline: Creating , updating and deleting a Reliance Retail promotion.
    Given I am verifying "<api_name>" api with url "<url>"
    When Set URL for "<url_endpoint>" for "<http_request_type>" request
    When Set body for "<body>"
    When set header for "<header>"
    When set parameters for "None"
    When Raise "<http_request_type>" request
    Then Valid HTTP response should be received
    Then Response http code should be "<response_code>"
    Then Response HEADER content type should be "<response_header_Type>"
    Then Response BODY should not be null or empty

    Examples:
      |url_endpoint             |http_request_type|body                       |header           |api_name              |url                                                      |response_code|response_header_Type   |
      |couponRetailPromoCreation|POST             |CreatePromoRelianceRetail  |applicationJson  |Promo_creation        |http://localhost:8082/v1/cms/coupons/promo/         |200          |application/json       |
      |couponRetailPromoCreation|PUT              |CreatePromoRelianceRetail  |applicationJson  |Promo_update          |http://localhost:8082/v1/cms/coupons/promo/         |200          |application/json       |
      |deletePromo              |DELETE           |None                       |None             |Coupon_delete         |http://localhost:8082/v1/cms/coupons/promo/{promoID}|200          |application/json       |
      |couponRetailPromoCreation|GET              |None                       |None             |Get_promo_creation    |http://localhost:8082/v1/cms/coupons/promo/         |404          |application/json       |
#  @test_coupon
  Scenario: Converting a promo to coupon.
    Given I am verifying "promo_to_coupon" api with url "http://localhost:8082/v1/cms/coupons/promo/"
    When Create 2 promo to be converted.
    When Set URL for "convertPromoToCoupon" for "POST" request
    When Set data "data_convertPromoToCoupon" and file "file_convertPromoToCoupon" for api
    When I am logging in to CMS
    When set header for "multipartFormDataWithAntiForgery"
    When Raise "POST" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response HEADER content type should be "application/json"

  Scenario: Getting Coupon ID of a converted promo ID.
    Given I am verifying " get Coupon ID from Promo ID" api with url "http://localhost:8082/v1/cms/coupons/promo"
    When I am logging in to CMS
    When Set URL for "GetAllCouponIDFromPromoID" for "GET" request
    When set parameters for "GetAllCouponIDFromPromoID"
    When set header for "secureJson"
    When Raise "GET" request for secure api
    Then Response http code should be "200"
    Then Promo ID should be assigned to coupon ID.

#  @test
  Scenario: Mapping the coupon codes to coupon ID.
    Given I am verifying "Mapping_coupon_code_to_couponID" api with url "http://localhost:8082/coupons/v1/coupons/coupon-codes"
    When Set URL for "couponCodeMapping" for "POST" request
    When set header for "multipartFormData"
    When Set data "None" and file "mapCouponCodeToPromo" for api
    And Raise "POST" HTTP request with file.
    Then Response http code should be "202"

#     @test
  Scenario: Create a campaign for the created coupon .
    Given I am verifying "campaign creation" api with url "http://localhost:8082/v1/cms/coupon-campaign/"
    When I am logging in to CMS
    When Set URL for "couponCampaignCreation" for "POST" request
    When set header for "secureJson"
    When Set data "couponCampaignCreation" and file "None" for api
    When Raise "POST" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response BODY should not be null or empty


#  @test
  Scenario: coupon code should be assigned to the coupons ID
    Given I am verifying "coupon code count" api with url "http://localhost:8082/v1/cms/merchant/23330/coupons/"
    When I am logging in to CMS
    When Set URL for "CouponCodeCount" for "GET" request
    When set header for "multipartFormDataWithAntiForgery"
    When Raise "GET" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response BODY should not be null or empty

#    @test
  Scenario Outline: Assigning coupons to phone numbers .
    Given I am verifying "Assigning Coupons to phone number" api with url "http://localhost:8082/v1/coupons/5988/redeem?version=v5"
    When Set URL for "couponCodeDistributionAPI" for "POST" request
    When Set header for "couponCodeDistributionAPI" linking to user "<num>" with phone number "<phone_num>".
    When Set parameters for "couponCodeDistributionAPI"
    When Set body for "couponCodeDistributionAPI"
    When Raise "POST" request with parameters
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response HEADER content type should be "application/json"
    Then Response BODY should not be null or empty
 #        When check that last created coupon codes for promo should be redeemed

    Examples:
      | num   |phone_num |
      |   1   |9945240312|
      |   2   |9945240313|
      |   3   |9945240314|
      |   4   |9945240315|
      |   5   |9945240316|
      |   6   |9945240317|
      |   7   |9945240318|
      |   8   |9945240319|
      |   9   |9945240320|
      |   10  |9945240311|

#    @test
  Scenario: redemption of the coupon codes after coupon codes are assigned.
    Given I am verifying "Coupon code redemption" api with url "http://localhost:8082/coupons/v1/coupons/redemptions"
    When Set URL for "couponCodeRedeeming" for "POST" request
    When set header for "multipartFormData"
    When Set data "None" and file "redeemCoupon" for api
    And Raise "POST" HTTP request with file.
    Then Response http code should be "202"

#    @test
  Scenario Outline: Create promo after removing mandatory fields one by one.
    Given I am verifying "Promo Creation" api with url "http://localhost:8082/v1/cms/coupons/promo/"
    When Set URL for "couponRetailPromoCreation" for "POST" request
    When set header for "applicationJson"
    When Set body for "CreatePromoRelianceRetail"
    And remove mandatory parameter "<parameters>" from promo body.
    When Raise "POST" request
    Then Valid HTTP response should be received
    Then Response http code should be "400"

    Examples:
      | parameters        |
      |REF_ID             |
      |PROMO_NAME         |
      |FORMAT             |
      |PROMO_STATUS       |
      |PROMO_CREATION_DATE|
      |START_DATE         |
      |END_DATE           |
      |PROMO_TYPE         |
      |TRIG_TYPE          |
      |TRIG_VAL           |
      |ARTICLE_STATUS     |
      |REWARD_TYPE        |
      |PROMO_DESC         |
      |TRANSACTION_LIMIT  |
      |COUPON_TYPE        |
      |COUPON_SERIES_NO   |

