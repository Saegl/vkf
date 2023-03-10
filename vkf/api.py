"""
Useful wrappers around api.vk.com/method
"""
from typing import Any, Iterator

import httpx

from vkf.models import Friend
from vkf.config import logger


VK_API_BASE_URL = "https://api.vk.com/method/"
VK_API_VERSION = "5.131"


class VKapiError(Exception):
    """Exception to represent errors received from vk api"""


class AccessTokenExpired(VKapiError):
    pass


VKresponse = dict[Any, Any]


def vk_method(
    method_name: str, params: dict[str, str], access_token: str
) -> VKresponse:
    """
    Request to vk methods listed on https://dev.vk.com/method

    Raises:
        VKapiError: error received from vk api
        AccessTokenExpired: user have to get new access token
    """
    response: VKresponse = httpx.post(
        VK_API_BASE_URL + method_name,
        headers={"Authorization": f"Bearer {access_token}"},
        params={"v": VK_API_VERSION} | params,
    ).json()

    check_error(response)
    return response


def check_error(response: VKresponse) -> None:
    """Check api response for errors"""
    if "error" in response:
        logger.debug(f"Error returned from vk api: {response['error']}")
        if response["error"]["error_code"] == 5:
            raise AccessTokenExpired("Access token expired, get new with `vkf auth`")
        else:
            raise VKapiError(response["error"].get("error_msg"))


def get_friends(access_token: str, user_id: int) -> Iterator[Friend]:
    """
    Load friends sorted by name
    https://dev.vk.com/method/friends.get
    """
    response = vk_method(
        "friends.get",
        {
            "user_id": str(user_id),
            "order": "name",
            "fields": "bdate,nickname,country,city,sex",
        },
        access_token,
    )

    for item in response["response"]["items"]:
        friend = Friend(
            first_name=item["first_name"],
            last_name=item["last_name"],
            country=item.get("country", {}).get("title"),
            city=item.get("city", {}).get("title"),
            bdate=item.get("bdate"),
            sex=item.get("sex"),
        )
        yield friend
