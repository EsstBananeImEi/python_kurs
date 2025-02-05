import os
import random
import time


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def console_text_decorator(border_char: str = "#"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_border_char = border_char

            textzeilen = func(*args, **kwargs)
            max_textzeile = len(max(textzeilen, key=len)) + 1

            border = current_border_char.center(
                max_textzeile + len(current_border_char) * 4 + 1,
                current_border_char,
            )

            print(border)
            for textzeile in textzeilen:
                print(
                    current_border_char,
                    textzeile.center(max_textzeile + len(current_border_char)),
                    current_border_char,
                )
            print(border)

            current_border_char = current_border_char[::-1]

            time.sleep(1)

        return wrapper

    return decorator


@console_text_decorator(border_char="!")
def get_error_message(*textzeilen):
    return textzeilen


get_error_message(
    "This is an",
    "Error",
    "please contact",
    "your Administrator",
    f"Code: 000xa{random.randint(100000, 999999)}",
)


@console_text_decorator(border_char="$")
def get_money_message(*textzeilen):
    return textzeilen


get_money_message("You are the WINNER", "of the", "2.000.000 $", "Jackpot")
