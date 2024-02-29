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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from rma.models.order_data_subtotal import OrderDataSubtotal
from rma.models.order_data_total import OrderDataTotal
from rma.models.rma_currency import RmaCurrency
from rma.models.rma_order_data_item import RmaOrderDataItem
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RmaOrderData(BaseModel):
    """
    RmaOrderData
    """ # noqa: E501
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    grn: Optional[StrictStr] = None
    number: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    channel: Optional[StrictStr] = None
    market: Optional[StrictStr] = None
    items: Optional[List[RmaOrderDataItem]] = None
    currency: Optional[RmaCurrency] = None
    subtotals: Optional[Dict[str, OrderDataSubtotal]] = None
    totals: Optional[Dict[str, OrderDataTotal]] = None
    __properties: ClassVar[List[str]] = ["createdAt", "updatedAt", "grn", "number", "status", "channel", "market", "items", "currency", "subtotals", "totals"]

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
        """Create an instance of RmaOrderData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in subtotals (dict)
        _field_dict = {}
        if self.subtotals:
            for _key in self.subtotals:
                if self.subtotals[_key]:
                    _field_dict[_key] = self.subtotals[_key].to_dict()
            _dict['subtotals'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in totals (dict)
        _field_dict = {}
        if self.totals:
            for _key in self.totals:
                if self.totals[_key]:
                    _field_dict[_key] = self.totals[_key].to_dict()
            _dict['totals'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RmaOrderData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "grn": obj.get("grn"),
            "number": obj.get("number"),
            "status": obj.get("status"),
            "channel": obj.get("channel"),
            "market": obj.get("market"),
            "items": [RmaOrderDataItem.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "currency": obj.get("currency"),
            "subtotals": dict(
                (_k, OrderDataSubtotal.from_dict(_v))
                for _k, _v in obj.get("subtotals").items()
            )
            if obj.get("subtotals") is not None
            else None,
            "totals": dict(
                (_k, OrderDataTotal.from_dict(_v))
                for _k, _v in obj.get("totals").items()
            )
            if obj.get("totals") is not None
            else None
        })
        return _obj

