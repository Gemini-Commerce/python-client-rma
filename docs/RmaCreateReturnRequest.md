# # RmaCreateReturnRequest


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id**| **str** |   |
**order_grn**| **str** |   |
**products**| [**List[CreateReturnRequestProduct]**](CreateReturnRequestProduct.md) |   |
**preferred_refund_method**| [**RmaRefundMethod**](RmaRefundMethod.md) |  for more information please, see Model/RmaRefundMethod.php  | [default to RmaRefundMethod.UNKNOWN]
**refund_shipping_cost**| **bool** |   | [optional]
**refund_payment_cost**| **bool** |   | [optional]
**customer_info**| [**RmaCustomerInfo**](RmaCustomerInfo.md) |   | [optional]
**return_address**| [**RmaPostalAddress**](RmaPostalAddress.md) |   | [optional]
**note**| **str** |   | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

