"""
    Logger verwenden mit getLogger
        Mit der Funktion getLogger kannst du einen Logger aufrufen oder erstellen.
        Meist wird für die Erstellung eines neuen Loggers die Variable __name__ verwendet.
        Diese enthält den Namen des Moduls, in dem sie verwendet wird.
"""
import logging


def my_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", "%d.%m.%Y %H:%M:%S")
    file_handler = logging.FileHandler(f"{name}.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


class Calculator:
    def __init__(self):
        self.logger = my_logger(__class__.__name__)

    def divide(self, divident, divisor):
        try:
            self.logger.info(f"divide {divident} / {divisor}")
            quotient = divident / divisor
            self.logger.info(f"{divident} / {divisor} = {quotient}")
            return quotient
        except ZeroDivisionError as ex:
            self.logger.error(f"beim teilen von ({divident} / {divisor}) ist ein fehler aufgetreten:", exc_info=True)


calc = Calculator()
calc.divide(200, 200)
