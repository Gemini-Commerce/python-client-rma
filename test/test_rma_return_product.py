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

from rma.models.rma_return_product import RmaReturnProduct

class TestRmaReturnProduct(unittest.TestCase):
    """RmaReturnProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RmaReturnProduct:
        """Test RmaReturnProduct
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RmaReturnProduct`
        """
        model = RmaReturnProduct()
        if include_optional:
            return RmaReturnProduct(
                grn = '',
                reason = '',
                requested = rma.models.rma_return_product_property.rmaReturnProductProperty(
                    quantity = '', 
                    note = '', ),
                approved = rma.models.rma_return_product_property.rmaReturnProductProperty(
                    quantity = '', 
                    note = '', ),
                verified = rma.models.rma_return_product_property.rmaReturnProductProperty(
                    quantity = '', 
                    note = '', ),
                refunded = rma.models.rma_return_product_property.rmaReturnProductProperty(
                    quantity = '', 
                    note = '', )
            )
        else:
            return RmaReturnProduct(
        )
        """

    def testRmaReturnProduct(self):
        """Test RmaReturnProduct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()