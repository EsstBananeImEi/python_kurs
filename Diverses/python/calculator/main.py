from argparse import ArgumentParser
from functools import reduce
from calculator import Calculator

from factory import Factory

# if __name__ == "__main__":
#     parser = ArgumentParser()
#     parser.add_argument('--value1', type=float, default=0,
#                         help='gib die erste zahl an')
#     parser.add_argument('--value2', type=float, default=0,
#                         help='gib die zweite zahl an ')
#     parser.add_argument('--operator', type=str, default="+",
#                         help='gib die Operation an')
#     arguments = parser.parse_args()

#     calculator = Factory.operator_factory(arguments.operator)
#     if isinstance(calculator, str):
#         print(calculator)
#     else:
#         print(calculator(arguments.value1, arguments.value2))

# Optionale Aufgabe mit n zahlen
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--values', nargs="+", default=0,
                        help='gib die zweite zahl an ')
    parser.add_argument('--operator', type=str,
                        default="+", help='gib den operator an')
    arguments = parser.parse_args()

    calculator = Factory.operator_factory(arguments.operator)
    if isinstance(calculator, str):
        print(calculator)
    else:
        print(reduce(calculator, map(float, arguments.values)))
