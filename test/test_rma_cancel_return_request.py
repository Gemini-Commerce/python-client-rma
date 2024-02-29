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

from rma.models.rma_cancel_return_request import RmaCancelReturnRequest

class TestRmaCancelReturnRequest(unittest.TestCase):
    """RmaCancelReturnRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RmaCancelReturnRequest:
        """Test RmaCancelReturnRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RmaCancelReturnRequest`
        """
        model = RmaCancelReturnRequest()
        if include_optional:
            return RmaCancelReturnRequest(
                tenant_id = '',
                id = ''
            )
        else:
            return RmaCancelReturnRequest(
                tenant_id = '',
                id = '',
        )
        """

    def testRmaCancelReturnRequest(self):
        """Test RmaCancelReturnRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
