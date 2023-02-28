import random

import time

from Tasks.g2_quick_sort import quick_sort

from Tasks.g1_merge_sort import merge_sort

arr = [random.randint(13, 25) for _ in range(1000000)]

if __name__ == '__main__':
    arr = [random.randint(13, 25) for _ in range(1000000)]
    t_1 = time.time()
    for i in range(5):
        quick_sort(arr)

    print(f"Время выполнения быстрой сортировки составляет {round((time.time() - t_1)/5, 2)}")

    t_2 = time.time()
    for i in range(5):
        merge_sort(arr)

    print(f"Время выполнения сортировки слиянием составляет {round((time.time() - t_1)/5, 2)}")


