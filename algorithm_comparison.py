from timeit import timeit
import random
from typing import Callable


def measure_execution_time(func: Callable, arguments, input_size):
    execution_time = timeit(lambda: func(arguments), number=1)

    print(
        f"Execution time of {func.__name__} with input size {input_size}: ",
        execution_time,
    )


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left_arr, right_arr):
    merged = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] < right_arr[right_idx]:
            merged.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged.append(right_arr[right_idx])
            right_idx += 1

    while left_idx < len(left_arr):
        merged.append(left_arr[left_idx])
        left_idx += 1

    while right_idx < len(right_arr):
        merged.append(right_arr[right_idx])
        right_idx += 1

    return merged


N = 10000
sorted_numbers_asc = list(range(N))
sorted_numbers_desc = list(range(N - 1, -1, -1))
shuffled_numbers = random.sample(range(N), k=N)

# measure_execution_time(merge_sort, sorted_numbers_asc, N)
# measure_execution_time(merge_sort, sorted_numbers_desc, N)
# measure_execution_time(merge_sort, shuffled_numbers, N)

# measure_execution_time(insertion_sort, sorted_numbers_asc, N)
# measure_execution_time(insertion_sort, sorted_numbers_desc, N)
# measure_execution_time(insertion_sort, shuffled_numbers, N)

measure_execution_time(sorted, sorted_numbers_asc, N)
measure_execution_time(sorted, sorted_numbers_desc, N)
measure_execution_time(sorted, shuffled_numbers, N)
