# coding: utf-8

"""
    RMA Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from rma.models.rma_confirm_return_approve_items_request import RmaConfirmReturnApproveItemsRequest

class TestRmaConfirmReturnApproveItemsRequest(unittest.TestCase):
    """RmaConfirmReturnApproveItemsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RmaConfirmReturnApproveItemsRequest:
        """Test RmaConfirmReturnApproveItemsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RmaConfirmReturnApproveItemsRequest`
        """
        model = RmaConfirmReturnApproveItemsRequest()
        if include_optional:
            return RmaConfirmReturnApproveItemsRequest(
                tenant_id = '',
                id = '',
                items = [
                    rma.models.rma_confirm_return_approve_items_request_item.rmaConfirmReturnApproveItemsRequestItem(
                        grn = '', 
                        quantity = '', )
                    ]
            )
        else:
            return RmaConfirmReturnApproveItemsRequest(
                tenant_id = '',
                id = '',
                items = [
                    rma.models.rma_confirm_return_approve_items_request_item.rmaConfirmReturnApproveItemsRequestItem(
                        grn = '', 
                        quantity = '', )
                    ],
        )
        """

    def testRmaConfirmReturnApproveItemsRequest(self):
        """Test RmaConfirmReturnApproveItemsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()