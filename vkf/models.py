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

    # Birth date can be in 3 possible formats
    # None if bdate is hidden
    # DD.MM if year is hidden
    # DD.MM.YYYY otherwise
    bdate: str | None

    # 1 female
    # 2 male
    sex: int
