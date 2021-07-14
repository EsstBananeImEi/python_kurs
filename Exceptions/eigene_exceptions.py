"""
    Es ist möglich eigene Exeptions zu erstellen
"""

# class CustomError(Exception):
#     pass
#
# raise CustomError("An error occurred")

print("\n######################################")

# class BaseException(Exception):
#     pass
#
# class TempretureTooHigh(BaseException):
#     pass
#
# class TempretureTooLow(BaseException):
#     pass
#
# best_temperature = 10
#
# while True:
#     try:
#         temp = int(input("Enter Temperatur: "))
#         if temp < best_temperature:
#             raise TempretureTooLow
#         elif temp > best_temperature:
#             raise TempretureTooHigh
#         break
#     except TempretureTooLow:
#         print("This Temperature is too low, try again!")
#         print()
#     except TempretureTooHigh:
#         print("This Temperature is too high, try again!")
#         print()
#
# print("Congratulations! You has found the best Temperature.")

print("\n######################################")


class SaleryNotInRangeError(Exception):
    """
        Diese Exception ist für den Zahlungs eingang

        Attributes:
            salery: zahlung die den error verursacht
            message: erläuterung des errors
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.salary} -> {self.message}'


salery = 2
if not 5000 < salery < 15000:
    raise SaleryNotInRangeError(salery)
