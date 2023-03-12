"""
Abstract classes for models -> text_file serializers
"""

import abc
from io import TextIOWrapper

from typing import Iterator

from vkf.models import Friend


class Serializer(abc.ABC):
    """
    Abstract class for friends -> text_file serializer
    """

    def save(self, friends: Iterator[Friend], f: TextIOWrapper):
        pass
