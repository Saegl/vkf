import httpx

BASE_API = "https://api.vk.com/method/"


def vk_method(method_name, params, access_token: str) -> httpx.Response:
    return httpx.post(
        BASE_API + method_name,
        headers={"Authorization": f"Bearer {access_token}"},
        params={"v": "5.131"} | params,
    )


def get_friends(access_token, user_id: int):
    response = vk_method(
        "friends.get",
        {
            "user_id": user_id,
            "fields": "bdate,nickname,country,city,sex",
        },
        access_token,
    )
    # print(response.json())
    json = response.json()

    for item in json["response"]["items"]:
        print(item)
