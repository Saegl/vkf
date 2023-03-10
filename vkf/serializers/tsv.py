import csv
from io import TextIOWrapper
from typing import Iterator
from vkf.serializers.base import Serializer
from vkf.models import Friend


class TsvSerializer(Serializer):
    def save(self, friends: Iterator[Friend], f: TextIOWrapper):
        fieldnames = list(Friend.schema()["properties"].keys())

        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()

        for friend in friends:
            writer.writerow(friend.dict())
