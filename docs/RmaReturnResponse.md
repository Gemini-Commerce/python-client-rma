# # RmaReturnResponse


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id**| **str** |   | [optional]
**grn**| **str** |   | [optional]
**order_grn**| **str** |   | [optional]
**status**| **str** |   | [optional]
**products**| [**List[RmaReturnProduct]**](RmaReturnProduct.md) |   | [optional]
**preferred_refund_method**| [**RmaRefundMethod**](RmaRefundMethod.md) |  for more information please, see Model/RmaRefundMethod.php  | [optional]
**refund_shipping_cost**| **bool** |   | [optional]
**refund_payment_cost**| **bool** |   | [optional]
**customer_info**| [**RmaCustomerInfo**](RmaCustomerInfo.md) |   | [optional]
**return_address**| [**RmaPostalAddress**](RmaPostalAddress.md) |   | [optional]
**note**| **str** |   | [optional]
**history**| [**List[RmaReturnHistory]**](RmaReturnHistory.md) |   | [optional]
**created_at**| **datetime** |   | [optional]
**updated_at**| **datetime** |   | [optional]
**order_data**| [**RmaOrderData**](RmaOrderData.md) |   | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

