import fire

import vkf.auth
import vkf.api
from vkf.serializers.base import Serializer
from vkf.serializers.json import JsonSerializer
from vkf.serializers.csv import CsvSerializer
from vkf.serializers.tsv import TsvSerializer


serializers: dict[str, Serializer] = {
    "json": JsonSerializer(),
    "csv": CsvSerializer(),
    "tsv": TsvSerializer(),
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

    with open("report." + format, "w", encoding="utf8", newline="") as f:
        serializer.save(friends, f)


def _main():
    """
    This function needed to conf `poetry scripts entry point`
    It starts from underscore to prevent showing it in fire cmd
    """
    fire.Fire(name="vkf")


if __name__ == "__main__":
    _main()
