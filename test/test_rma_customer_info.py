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

from rma.models.rma_customer_info import RmaCustomerInfo

class TestRmaCustomerInfo(unittest.TestCase):
    """RmaCustomerInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RmaCustomerInfo:
        """Test RmaCustomerInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RmaCustomerInfo`
        """
        model = RmaCustomerInfo()
        if include_optional:
            return RmaCustomerInfo(
                firstname = '',
                lastname = '',
                email = '',
                phone = '',
                grn = ''
            )
        else:
            return RmaCustomerInfo(
        )
        """

    def testRmaCustomerInfo(self):
        """Test RmaCustomerInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
