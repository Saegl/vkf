import sys
import httpx

from vkf.models import Friend


BASE_API = "https://api.vk.com/method/"


class AccessTokenExpired(Exception):
    pass


def vk_method(method_name, params, access_token: str) -> dict:
    response = httpx.post(
        BASE_API + method_name,
        headers={"Authorization": f"Bearer {access_token}"},
        params={"v": "5.131"} | params,
    ).json()

    check_error(response)
    return response


def check_error(response: dict):
    if "error" in response:
        if response["error"]["error_code"] == 5:
            sys.tracebacklimit = 0
            raise AccessTokenExpired("Access token expired, get new with `vkf auth`")


def get_friends(access_token, user_id: int):
    response = vk_method(
        "friends.get",
        {
            "user_id": user_id,
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
