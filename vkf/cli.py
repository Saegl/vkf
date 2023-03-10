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

    def auth(self):
        """
        Use vk.com implicit flow through default web browser
        to get access token
        """
        vkf.auth.web_auth()

    def load_friends(
        self,
        access_token: str,
        user_id: int,
        format: str = "csv",
        output: str = "",
    ):
        """Load friends and save them in report"""
        friends = vkf.api.get_friends(access_token, user_id)
        serializer = serializers[format]

        with open("report." + format, "w", encoding="utf8", newline="") as f:
            serializer.save(friends, f)
