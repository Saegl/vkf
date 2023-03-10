import fire

import vkf.auth
import vkf.api
from vkf.serializers.json import JsonSerializer


serializers = {
    "json": JsonSerializer(),
}


def auth():
    vkf.auth.web_auth()


def load_friends(
    access_token: str,
    user_id: int,
    format: str = "csv",
    output: str = "",
):
    friends = vkf.api.get_friends(access_token, user_id)
    serializer = serializers[format]

    with open("report." + format, "w", encoding="utf8") as f:
        serializer.save(friends, f)


def _main():
    """
    This function needed to conf `poetry scripts entry point`
    It starts from underscore to prevent showing it in fire cmd
    """
    fire.Fire(name="vkf")


if __name__ == "__main__":
    _main()
