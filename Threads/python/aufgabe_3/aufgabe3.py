from threading import Thread
import time

my_list: list[int] = [1]
my_threads: list[Thread] = []


def add_to_list(number: int) -> None:
    global my_list

    local_list = my_list
    time.sleep(0.2)
    local_list.append(local_list[-1] + number)

    my_list = local_list


if __name__ == "__main__":

    for round in range(1, 11):
        my_threads.append(Thread(target=add_to_list, args=(round,)))

    for thread in my_threads:
        thread.start()

    for thread in my_threads:
        thread.join()

    print(my_list)
