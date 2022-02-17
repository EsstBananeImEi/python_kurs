from threading import Thread, Lock
import time

saldo = 0
lock = Lock()


def deposit(amount: int):
    global saldo

    lock.acquire()
    local_balance = saldo
    local_balance += amount

    time.sleep(0.2)

    saldo = local_balance
    print(f'Einzahlung={amount}')
    lock.release()


t1 = Thread(target=deposit, args=(10,))
t2 = Thread(target=deposit, args=(20,))

t1.start()
t2.start()


t1.join()
t2.join()


print(f'Dein Endgültiger Saldo ist {saldo}')
