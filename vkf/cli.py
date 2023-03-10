import sys

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


class ArgumentError(Exception):
    """Exception to represent wrong arguments to cli program"""


def get_serializer(format: str):
    if format not in serializers:
        raise ArgumentError(
            f"Format {format} is not supported, "
            f"supported formats: {list(serializers.keys())}"
        )
    return serializers[format]


class CliCommands:
    """
    export friends from vk.com
    """

    def __init__(self, trace: bool = False):
        """
        Flags for all commands.

        use flag --trace to show full stacktrace
        By defualt full stacktrace is disabled to
        make short human readable messages.
        """
        self.trace = trace
        if not trace:
            sys.tracebacklimit = 0

    def auth(
        self,
        client_id: str,
        host: str = "127.0.0.1",
        port: int = 3434,
    ):
        """
        Use vk.com implicit flow through default web browser
        to get access token.
        It opens small localhost server to catch returned token.
        Ensure host is added to vk app developer dashboard (Settings -> Open API),
        and port is not currently in use
        """
        vkf.auth.web_auth(client_id, host, port)

    def load_friends(
        self,
        access_token: str,
        user_id: int,
        format: str = "csv",
        output: str = "",
    ):
        """Load friends and save them in report"""
        friends = vkf.api.get_friends(access_token, user_id)
        serializer = get_serializer(format)

        filename = output if output else "report." + format

        with open(filename, "w", encoding="utf8", newline="") as f:
            serializer.save(friends, f)
