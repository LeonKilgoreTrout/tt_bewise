from loguru import logger
import sys
from typing import Any
from time import time

config = {
    "handlers": [
        {
            "sink": sys.stdout,
            "format": "{message}"
        },
        {
            "sink": "./logs/logs.log",
            "format": "{message}",
            "rotation": "5 MB"
        }
    ]
}


logger.remove()
logger.configure(**config)


def log(message: str, **kwargs: Any) -> None:
    data = {
        "message": message,
        "info": str(kwargs),
        "timestamp": time()
    }
    logger.info(data)
