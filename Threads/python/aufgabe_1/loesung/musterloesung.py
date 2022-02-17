from threading import Thread
import time

my_list: list[int] = []


def add_to_list(number: int) -> None:
    time.sleep(1)
    my_list.append(number)


if __name__ == "__main__":

    for round in range(1, 11):
        thread = Thread(target=add_to_list, args=(round,))
        thread.start()

    time.sleep(10)
    print(my_list)
