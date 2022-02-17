from threading import Thread
import time

my_list: list[int] = []
my_threads: list[Thread] = []


def add_to_list(number: int) -> None:
    time.sleep(1)
    my_list.append(number)


if __name__ == "__main__":

    for round in range(1, 11):
        my_threads.append(Thread(target=add_to_list, args=(round,)))

    for thread in my_threads:
        thread.start()
        thread.join()

    print(my_list)
