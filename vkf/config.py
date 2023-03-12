import logging

logger = logging.Logger(name="APP", level=logging.DEBUG)

formatter = logging.Formatter("%(name)s:%(levelname)s: %(message)s")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.CRITICAL)
console_handler.setFormatter(formatter)


file_handler = logging.FileHandler("vkf.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


logger.addHandler(console_handler)
logger.addHandler(file_handler)
