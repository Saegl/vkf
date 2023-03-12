# Notes for developers

This project uses [poetry](https://python-poetry.org/)  
If you install package by using pip, you cannot test it / run linters and formatters  
So install by using poetry, install poetry itself and then:

```bash
poetry shell
poetry install
```

## Run tests

```bash
pytest --cov=vkf --cov-report=html
```

## Run formatter / linters

```bash
pre-commit run -a # all files
pre-commit run # staged files
```

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
