import json
from typing import Iterator
from io import TextIOWrapper


from vkf.serializers.base import Serializer
from vkf.models import Friend


class JsonSerializer(Serializer):
    def save(self, friends: Iterator[Friend], f: TextIOWrapper) -> None:
        data = [friend.dict() for friend in friends]
        json.dump(data, f, ensure_ascii=False)
