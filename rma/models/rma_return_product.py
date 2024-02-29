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
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from rma.models.rma_return_product_property import RmaReturnProductProperty
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RmaReturnProduct(BaseModel):
    """
    RmaReturnProduct
    """ # noqa: E501
    grn: Optional[StrictStr] = None
    reason: Optional[StrictStr] = None
    requested: Optional[RmaReturnProductProperty] = None
    approved: Optional[RmaReturnProductProperty] = None
    verified: Optional[RmaReturnProductProperty] = None
    refunded: Optional[RmaReturnProductProperty] = None
    __properties: ClassVar[List[str]] = ["grn", "reason", "requested", "approved", "verified", "refunded"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RmaReturnProduct from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of requested
        if self.requested:
            _dict['requested'] = self.requested.to_dict()
        # override the default output from pydantic by calling `to_dict()` of approved
        if self.approved:
            _dict['approved'] = self.approved.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verified
        if self.verified:
            _dict['verified'] = self.verified.to_dict()
        # override the default output from pydantic by calling `to_dict()` of refunded
        if self.refunded:
            _dict['refunded'] = self.refunded.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RmaReturnProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "grn": obj.get("grn"),
            "reason": obj.get("reason"),
            "requested": RmaReturnProductProperty.from_dict(obj.get("requested")) if obj.get("requested") is not None else None,
            "approved": RmaReturnProductProperty.from_dict(obj.get("approved")) if obj.get("approved") is not None else None,
            "verified": RmaReturnProductProperty.from_dict(obj.get("verified")) if obj.get("verified") is not None else None,
            "refunded": RmaReturnProductProperty.from_dict(obj.get("refunded")) if obj.get("refunded") is not None else None
        })
        return _obj

