import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, name: str = "app", level=logging.INFO):
        # Create the logs directory if it doesn't exist
        os.makedirs("logs", exist_ok=True)

        # Define the log file name based on the current date
        log_filename = f"logs/{name}_{datetime.now().strftime('%Y-%m-%d')}.log"

        # Configure the logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.propagate = False

        # Avoid duplicate handlers if the logger already exists
        if not self.logger.handlers:
            # File handler
            file_handler = logging.FileHandler(log_filename, encoding="utf-8")
            file_handler.setLevel(level)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # Define the log format
            formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Attach handlers to the logger
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger