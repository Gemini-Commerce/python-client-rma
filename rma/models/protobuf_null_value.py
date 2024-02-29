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


class ProtobufNullValue(str, Enum):
    """
    `NullValue` is a singleton enumeration to represent the null value for the `Value` type union.   The JSON representation for `NullValue` is JSON `null`.   - NULL_VALUE: Null value.
    """

    """
    allowed enum values
    """
    NULL_VALUE = 'NULL_VALUE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProtobufNullValue from a JSON string"""
        return cls(json.loads(json_str))


