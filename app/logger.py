from loguru import logger
import sys
from typing import Any
from time import time
from app.settings import Settings


DEBUG = Settings().app_description.debug
config = {
    "handlers": [
        {
            "sink": "../logs/logs.log",
            "format": "{message}",
            "rotation": "5 MB"
        }
    ]
}

if DEBUG:
    config["handlers"].append(dict({"sink": sys.stdout,
                                    "format": "{message}"}))

logger.remove()
logger.configure(**config)


def log(message: str, **kwargs: Any) -> None:
    data = {
        "message": message,
        "info": str(kwargs),
        "timestamp": time()
    }
    logger.info(data)
