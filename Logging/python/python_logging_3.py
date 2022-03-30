"""
    Logger verwenden mit getLogger
        Mit der Funktion getLogger kannst du einen Logger aufrufen oder erstellen.
        Meist wird für die Erstellung eines neuen Loggers die Variable __name__ verwendet.
        Diese enthält den Namen des Moduls, in dem sie verwendet wird.
"""
import logging
import os
from logging.handlers import RotatingFileHandler


class Logger:
    def __init__(self, name, log_file, max_size=10 * 1024 * 1024, backup_count=5):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(
            log_file, maxBytes=max_size, backupCount=backup_count
        )
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg, exc_info=False):
        self.logger.error(msg, exc_info=exc_info)

    def critical(self, msg):
        self.logger.critical(msg)

    def remove_handler(self):
        print(f"Removing handler {self.logger.name}")
        self.logger.removeHandler(self.logger.handlers[0])

    def __repr__(self):
        return f"Logger({self.logger.name})"


class Calculator:
    def __init__(self):
        logging_path = os.sep.join(
            [os.path.dirname(os.path.abspath(__file__)), "calculator.log"]
        )
        self.logger = Logger("Calculator", logging_path)

    def divide(self, divident, divisor) -> float | None:
        try:
            self.logger.info(f"divide {divident} / {divisor}")
            quotient: float = divident / divisor
            self.logger.info(f"{divident} / {divisor} = {quotient}")
            return quotient
        except ZeroDivisionError as ex:
            self.logger.error(
                f"beim teilen von ({divident} / {divisor}) ist ein fehler aufgetreten:",
                exc_info=True,
            )


calc = Calculator()
result = calc.divide(10, 0)
print(result)
