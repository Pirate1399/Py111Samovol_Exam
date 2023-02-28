from Tasks.g1_merge_sort import merge_sort

# Оценить асимптотическую сложность приведенного ниже алгоритма:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = int(len(arr) - 1)  # O(n)
out = []
while a > 0:  # O(log(n)) по основанию 1,7
    out.append(arr[a])  # O(1)
    a = int(a // 1.7)
    print(a)

merge_sort(out) # O(n log(n))

print("ассимптотическая сложность O(n log(n))")