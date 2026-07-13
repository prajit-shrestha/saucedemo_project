import logging
from logging.handlers import RotatingFileHandler


def get_logger():

    logger = logging.getLogger(__name__)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler = RotatingFileHandler(
            "logs/automation.log",
            maxBytes=5 * 1024 * 1024,  # 5 MB
            backupCount=3
        )
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(filename)s | %(funcName)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger