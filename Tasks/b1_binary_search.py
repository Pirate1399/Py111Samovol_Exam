from typing import Sequence, Optional

import time


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    min_index = 0
    max_index = len(arr) - 1
    while max_index >= min_index:
        middle_index = (max_index + min_index)//2
        if elem == arr[middle_index]:
            return middle_index

        elif elem < arr[middle_index]:
            max_index = middle_index - 1

        elif elem > arr[middle_index]:
            min_index = middle_index + 1

    return None


arr = [i for i in range(30000000)]

t_1 = time.time()
for i in range(5):
    print(binary_search(4509821, arr))

print((time.time() - t_1)/5)
