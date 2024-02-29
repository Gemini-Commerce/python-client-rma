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

from rma.models.rma_postal_address import RmaPostalAddress

class TestRmaPostalAddress(unittest.TestCase):
    """RmaPostalAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RmaPostalAddress:
        """Test RmaPostalAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RmaPostalAddress`
        """
        model = RmaPostalAddress()
        if include_optional:
            return RmaPostalAddress(
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
                additional_info = rma.models.additional_info.additionalInfo()
            )
        else:
            return RmaPostalAddress(
        )
        """

    def testRmaPostalAddress(self):
        """Test RmaPostalAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()