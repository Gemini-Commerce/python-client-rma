# # RmaOrderData


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at**| **datetime** |   | [optional]
**updated_at**| **datetime** |   | [optional]
**grn**| **str** |   | [optional]
**number**| **str** |   | [optional]
**status**| **str** |   | [optional]
**channel**| **str** |   | [optional]
**market**| **str** |   | [optional]
**items**| [**List[RmaOrderDataItem]**](RmaOrderDataItem.md) |   | [optional]
**currency**| [**RmaCurrency**](RmaCurrency.md) |  for more information please, see Model/RmaCurrency.php  | [optional]
**subtotals**| [**Dict[str, OrderDataSubtotal]**](OrderDataSubtotal.md) |   | [optional]
**totals**| [**Dict[str, OrderDataTotal]**](OrderDataTotal.md) |   | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

