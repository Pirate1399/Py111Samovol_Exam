import time

import math

from functools import lru_cache


@lru_cache()
def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError("ValueError should be here...")

    if n in (0, 1):
        return 1

    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError

    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


def factorial_generator(n: int):
    if n < 0:
        raise ValueError

    result = 1
    while n > 0:
        yield result
        result *= n
        n -= 1


if __name__ == '__main__':

    t_1 = time.perf_counter_ns()

    for i in range(10):
        # print(factorial_recursive(200))  # 200 - 39980 нс без lru | 19820 нс с lru
        # print(factorial_iterative(200))  # 200 - 21380 нс через while  | 17010 нс через for
        print(math.factorial(200))  # 200 - 6940 нс

    print(((time.perf_counter_ns() - t_1) / 10))

    fact_gen = factorial_generator(5)
    print(next(fact_gen))
    print(next(fact_gen))
    print(next(fact_gen))
    print(next(fact_gen))
    print(next(fact_gen))
