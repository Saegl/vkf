import io

from vkf.models import Friend
from vkf.serializers.json import JsonSerializer
from vkf.serializers.csv import CsvSerializer
from vkf.serializers.tsv import TsvSerializer


friends = [
    Friend(
        first_name="john",
        last_name="doe",
        country=None,
        city=None,
        bdate=None,
        sex=1,
    ),
    Friend(
        first_name="example",
        last_name="example2",
        country="Kazakhstan",
        city="Almaty",
        bdate="13.06.2001",
        sex=1,
    ),
]


def test_save_json():
    serializer = JsonSerializer()
    output = io.StringIO()
    serializer.save(friends, output)


def test_save_csv():
    serializer = CsvSerializer()
    output = io.StringIO()
    serializer.save(friends, output)


def test_save_tsv():
    serializer = TsvSerializer()
    output = io.StringIO()
    serializer.save(friends, output)
