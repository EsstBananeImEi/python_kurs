"""
    Python logging in Klassen:
        Logging kann in Klassen genauso verwendet werden wie wir es in Lektion logging 1 gemacht haben.

        Im Folgendem Code sehen wir ein Beispiel für das logging in einer Klasse.
"""

import logging

logging.basicConfig(level=logging.DEBUG, filename="logging_2.log")


class Calculator:

    def divide(self, divident, divisor):
        try:
            logging.info(f"divide {divident} / {divisor}")
            quotient = divident / divisor
            logging.info(f"{divident} / {divisor} = {quotient}")
            return quotient
        except ZeroDivisionError as ex:
            logging.error(f"beim teilen von ({divident} / {divisor}) ist ein fehler aufgetreten:", exc_info=True)


calc = Calculator()
calc.divide(200, 0)

"""
    Der Parameter exc_info, sorgte in unserem Beispiel noch dazu, dass wir den ZeroDevisionError mit in das Logfile
    geschrieben haben.
"""
