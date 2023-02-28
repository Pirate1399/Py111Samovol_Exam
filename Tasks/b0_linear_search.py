"""
This module implements some functions based on linear search algo
"""
from typing import Sequence
import random
import time


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """

    min_ = arr[0]
    min_index = 0
    for index, elem in enumerate(arr):
        if elem < min_:
            min_ = elem
            min_index = index

    return min_index

t_1 = time.time()


print(min_search([random.randint(-10000, 10000) for _ in range(30000)]))
print(time.time() - t_1)
