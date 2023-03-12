# Notes for developers

## Add new output format

0. Create new file in `vkf/serializers/<format>.py`
1. Inherit from Abstract Class, like [here](../vkf/serializers/csv.py)
2. Register your new class [at](../vkf/cli.py) :: serializers

```python
serializers: dict[str, Serializer] = {
    "csv": CsvSerializer(),
    ...,
    "<new_format>": NewFormatSerializer(),
}
```

3. Update [readme](../README.md)
