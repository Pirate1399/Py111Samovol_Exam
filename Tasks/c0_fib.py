import time


def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError(f"Is there a {n} number of Fibonacci sequence? I think here should be an exception...")
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError(f"Is there a {n} number of Fibonacci sequence? I think here should be and exception...")

    if n == 1 or n == 2:
        return 1

    elif n > 2:
        num_1 = 1
        num_2 = 1
        for _ in range(3, n+1):
            num_1, num_2 = num_2, num_1 + num_2

        return num_1


def fib_gen(n: int):
    if n < 0:
        raise ValueError(f"Is there a {n} number of Fibonacci sequence? I think here should be and exception...")

    num_1, num_2 = 0, 1
    for _ in range(0, n+1):
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


if __name__ == '__main__':
    t_1 = time.perf_counter_ns()

    for i in range(10):
        print(fib_recursive(33))
        # print(fib_iterative(301))

    print(((time.perf_counter_ns() - t_1) / 10) / 1000 / 1000 / 1000)

    f_gen = fib_gen(9)
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
