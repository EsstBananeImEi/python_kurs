def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fiblist(n: int) -> list[int]:
    fib = [0, 1]
    for _ in range(1, n):
        fib += [fib[-1] + fib[-2]]
    return fib
