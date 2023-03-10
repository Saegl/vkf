import abc
from io import TextIOWrapper

from typing import Iterator

from vkf.models import Friend


class Serializer(abc.ABC):
    def save(self, friends: Iterator[Friend], f: TextIOWrapper):
        pass
