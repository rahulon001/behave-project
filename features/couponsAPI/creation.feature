@test_all
Feature: Test for creating different entities like merchants , coupons etc.
#  @test_coupon
  Scenario: Creating a merchant
    Given I am verifying "add_Merchant" api with url "http://localhost:8082/v1/cms/admin/merchants"
    When Set URL for "add_merchant" for "POST" request
    When Set data "data_add_merchants" and file "file_add_merchants" for api
    When I am logging in to CMS
    When set header for "multipartFormDataWithAntiForgery"
    When Raise "POST" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Then Response HEADER content type should be "application/json"

#  @bulk
  Scenario: creating multiple merchants; assigning multiple branches via bulk upload and assigning those merchants to a group
    Given I am verifying "add_Multiple_Merchant_with_branches" api with url "http://localhost:8082/v1/cms/merchant/address/csv"
    Given I am verifying "merchant_group" api with url "http://localhost:8082/v1/cms/merchant-group/"
    When refreshing the address_info.csv file
    When create 1 merchants each with 1 branches within 50 km radius
    Then create the merchant group with the merchant list.

#  @test_coupon
  Scenario Outline: Creating a merchant pull type coupon
    Given I am verifying "<api_name>" api with url "<url>"
    When Set URL for "<api>" for "<request_type>" request
    When Set data "<data>" and file "<file>" for api
    When I am logging in to CMS
    When set header for "<header>"
    When Raise "<request_type>" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "<response>"
    Then Response HEADER content type should be "<response_header>"

    Examples:
      |url                                           |api_name                                                 |api                          |request_type|file                                                          |data                                                           |header                          |response|response_header  |
      |http://localhost:8082/v1/cms/merchant/<merchant_id>/coupon|add_coupon_pull_merchant_type_flat_discount_on_sku       |add_coupon_pull_merchant_type|POST        |file_add_coupon_pull_merchant_type_flat_discount_on_sku       |data_add_coupon_pull_merchant_type_flat_discount_on_sku        |multipartFormDataWithAntiForgery|200     |application/json |
      |http://localhost:8082/v1/cms/merchant/<merchant_id>/coupon|add_coupon_pull_merchant_type_Free_SKUs_on_Bill          |add_coupon_pull_merchant_type|POST        |file_add_coupon_pull_merchant_type_Free_SKUs_on_Bill          |data_add_coupon_pull_merchant_type_Free_SKUs_on_Bill           |multipartFormDataWithAntiForgery|200     |application/json |
      |http://localhost:8082/v1/cms/merchant/<merchant_id>/coupon|add_coupon_pull_merchant_type_Free_SKUs_on_SKUs          |add_coupon_pull_merchant_type|POST        |file_add_coupon_pull_merchant_type_Free_SKUs_on_SKUs          |data_add_coupon_pull_merchant_type_Free_SKUs_on_SKUs           |multipartFormDataWithAntiForgery|200     |application/json |
      |http://localhost:8082/v1/cms/merchant/<merchant_id>/coupon|add_coupon_pull_merchant_type_flat_discount              |add_coupon_pull_merchant_type|POST        |file_add_coupon_pull_merchant_type_flat_discount              |data_add_coupon_pull_merchant_type_flat_discount               |multipartFormDataWithAntiForgery|200     |application/json |
      |http://localhost:8082/v1/cms/merchant/<merchant_id>/coupon|add_coupon_pull_merchant_type_Percentage_discount_on_SKU |add_coupon_pull_merchant_type|POST        |file_add_coupon_pull_merchant_type_Percentage_discount_on_SKU |data_add_coupon_pull_merchant_type_Percentage_discount_on_SKU  |multipartFormDataWithAntiForgery|200     |application/json |
      |http://localhost:8082/v1/cms/merchant/<merchant_id>/coupon|add_coupon_pull_merchant_type_Percentage_discount_on_Bill|add_coupon_pull_merchant_type|POST        |file_add_coupon_pull_merchant_type_Percentage_discount_on_Bill|data_add_coupon_pull_merchant_type_Percentage_discount_on_Bill |multipartFormDataWithAntiForgery|200     |application/json |

#   @test_coupon
  Scenario Outline: Creating a brand pull type coupon
    Given I am verifying "<api_name>" api with url "<url>"
    When Set URL for "<api>" for "<request_type>" request
    When Set data "<data>" and file "<file>" for api
    When I am logging in to CMS
    When set header for "<header>"
    When Raise "<request_type>" request for secure api
    Then Valid HTTP response should be received
    Then Response http code should be "<response>"
    Then Response HEADER content type should be "<response_header>"
    Examples:
      |url                                               |api_name                                              |api                       |request_type|file                                                       |data                                                       |header                          |response|response_header  |
      |http://localhost:8082/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_pull_brand_type_flat_discount_on_sku       |add_coupon_pull_brand_type|POST        |file_add_coupon_pull_brand_type_flat_discount_on_sku       |data_add_coupon_pull_brand_type_flat_discount_on_sku       |multipartFormDataWithAntiForgery|200     |application/json |
      |http://localhost:8082/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_pull_brand_type_Free_SKUs_on_SKUs          |add_coupon_pull_brand_type|POST        |file_add_coupon_pull_brand_type_Free_SKUs_on_SKUs          |data_add_coupon_pull_brand_type_Free_SKUs_on_SKUs          |multipartFormDataWithAntiForgery|200     |application/json |
      |http://localhost:8082/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_pull_brand_type_Free_SKUs_on_Bill          |add_coupon_pull_brand_type|POST        |file_add_coupon_pull_brand_type_Free_SKUs_on_Bill          |data_add_coupon_pull_brand_type_Free_SKUs_on_Bill          |multipartFormDataWithAntiForgery|200     |application/json |
      |http://localhost:8082/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_pull_brand_type_flat_discount              |add_coupon_pull_brand_type|POST        |file_add_coupon_pull_brand_type_flat_discount              |data_add_coupon_pull_brand_type_flat_discount              |multipartFormDataWithAntiForgery|200     |application/json |
      |http://localhost:8082/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_pull_brand_type_Percentage_discount_on_SKU |add_coupon_pull_brand_type|POST        |file_add_coupon_pull_brand_type_Percentage_discount_on_SKU |data_add_coupon_pull_brand_type_Percentage_discount_on_SKU |multipartFormDataWithAntiForgery|200     |application/json |
      |http://localhost:8082/v1/cms/merchant/<merchant_grp_id>/coupon|add_coupon_pull_brand_type_Percentage_discount_on_Bill|add_coupon_pull_brand_type|POST        |file_add_coupon_pull_brand_type_Percentage_discount_on_Bill|data_add_coupon_pull_brand_type_Percentage_discount_on_Bill|multipartFormDataWithAntiForgery|200     |application/json |


  @bulk @test_coupon
  Scenario: creating multiple coupons
    Given I am verifying "campaign creation" api with url "<base_url>/v1/cms/coupon-campaign/"
    When create 1 coupons from all types
    Then creating campaigns with all the created coupon IDs