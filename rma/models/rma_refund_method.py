# coding: utf-8

"""
    RMA Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class RmaRefundMethod(str, Enum):
    """
    RmaRefundMethod
    """

    """
    allowed enum values
    """
    REFUND_METHOD_UNKNOWN = 'REFUND_METHOD_UNKNOWN'
    REFUND_METHOD_OFFLINE = 'REFUND_METHOD_OFFLINE'
    REFUND_METHOD_COUPON = 'REFUND_METHOD_COUPON'
    REFUND_METHOD_SAME_AS_PAYMENT = 'REFUND_METHOD_SAME_AS_PAYMENT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RmaRefundMethod from a JSON string"""
        return cls(json.loads(json_str))


