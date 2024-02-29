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

from rma.api.rma_api import RmaApi


class TestRmaApi(unittest.TestCase):
    """RmaApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RmaApi()

    def tearDown(self) -> None:
        pass

    def test_add_note(self) -> None:
        """Test case for add_note

        Add a note to an RMA
        """
        pass

    def test_approve_return(self) -> None:
        """Test case for approve_return

        Approve a return
        """
        pass

    def test_cancel_return(self) -> None:
        """Test case for cancel_return

        Cancel a return
        """
        pass

    def test_confirm_return_approve_items(self) -> None:
        """Test case for confirm_return_approve_items

        Confirm return approve items
        """
        pass

    def test_create_return(self) -> None:
        """Test case for create_return

        Create a return
        """
        pass

    def test_delete_note(self) -> None:
        """Test case for delete_note

        Delete a note from an RMA
        """
        pass

    def test_edit_note(self) -> None:
        """Test case for edit_note

        Edit a note on an RMA
        """
        pass

    def test_get_return(self) -> None:
        """Test case for get_return

        Get a return
        """
        pass

    def test_list_notes_by_return_id(self) -> None:
        """Test case for list_notes_by_return_id

        List notes by return id
        """
        pass

    def test_list_returns(self) -> None:
        """Test case for list_returns

        List returns
        """
        pass

    def test_refund_return(self) -> None:
        """Test case for refund_return

        Refund a return
        """
        pass

    def test_reject_return(self) -> None:
        """Test case for reject_return

        Reject a return
        """
        pass

    def test_set_received_items(self) -> None:
        """Test case for set_received_items

        Set received items
        """
        pass

    def test_skip_return_status(self) -> None:
        """Test case for skip_return_status

        Skip a return status
        """
        pass


if __name__ == '__main__':
    unittest.main()
