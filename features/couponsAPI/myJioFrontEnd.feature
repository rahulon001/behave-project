@test_all
Feature: Finding the latency of the APIs.
  Scenario Outline: Latency for MyJio frontend App
    Given I am verifying "<api_name>" api with url "<url>"
    When I am logging in for access token
    When Set URL for "<url_endpoint>" for "<http_request_type>" request
    When set header for "<header>"
    When set parameters for "<parameters>"
    When Raise "<http_request_type>" request with parameters
    Then Valid HTTP response should be received
    Then Response http code should be "200"
    Examples:
      |url_endpoint          |http_request_type|header         |parameters    |api_name   |url|
      |MyjioCategory         |GET              |Category       |Category      |Category   |http://localhost:8082/cr/v2/coupons/category?|
      |MyjioFavourite        |GET              |Favourite      |Favourite     |Favourite  |http://localhost:8082/cr/v2/coupons/favorites?|
      |MyjioAllCoupons       |GET              |AllCoupons     |AllCoupons    |AllCoupons |http://localhost:8082/cr/v2/coupons?|


    #######################

#    When Latency for category change to shopping
#    When Latency for category change to Entertainment
#    When Latency for category change to dining

