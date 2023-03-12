"""
Validated models received from vk api
Used as input to serializers
"""
from pydantic import BaseModel


class Friend(BaseModel):
    first_name: str
    last_name: str
    country: str | None
    city: str | None
    bdate: str | None
    sex: int
