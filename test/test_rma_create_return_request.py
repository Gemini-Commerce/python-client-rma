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

from rma.models.rma_create_return_request import RmaCreateReturnRequest

class TestRmaCreateReturnRequest(unittest.TestCase):
    """RmaCreateReturnRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RmaCreateReturnRequest:
        """Test RmaCreateReturnRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RmaCreateReturnRequest`
        """
        model = RmaCreateReturnRequest()
        if include_optional:
            return RmaCreateReturnRequest(
                tenant_id = '',
                order_grn = '',
                products = [
                    rma.models.create_return_request_product.CreateReturnRequestProduct(
                        grn = '', 
                        quantity = '', 
                        reason = '', 
                        note = '', )
                    ],
                preferred_refund_method = 'REFUND_METHOD_UNKNOWN',
                refund_shipping_cost = True,
                refund_payment_cost = True,
                customer_info = rma.models.rma_customer_info.rmaCustomerInfo(
                    firstname = '', 
                    lastname = '', 
                    email = '', 
                    phone = '', 
                    grn = '', ),
                return_address = rma.models.rma_postal_address.rmaPostalAddress(
                    revision = 56, 
                    region_code = '', 
                    language_code = '', 
                    postal_code = '', 
                    sorting_code = '', 
                    administrative_area = '', 
                    locality = '', 
                    sublocality = '', 
                    address_lines = [
                        ''
                        ], 
                    recipients = [
                        ''
                        ], 
                    organization = '', 
                    phone_number = '', 
                    additional_info = rma.models.additional_info.additionalInfo(), ),
                note = ''
            )
        else:
            return RmaCreateReturnRequest(
                tenant_id = '',
                order_grn = '',
                products = [
                    rma.models.create_return_request_product.CreateReturnRequestProduct(
                        grn = '', 
                        quantity = '', 
                        reason = '', 
                        note = '', )
                    ],
                preferred_refund_method = 'REFUND_METHOD_UNKNOWN',
        )
        """

    def testRmaCreateReturnRequest(self):
        """Test RmaCreateReturnRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()