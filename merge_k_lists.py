from typing import List


def merge_two_lists(left: List[int], right: List[int]) -> List[int]:
    merged = []
    left_idx = right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx += 1

    return merged


def merge_k_lists(arr: List[List[int]]) -> List[int]:
    n = len(arr)

    if not arr:
        return []

    if n == 1:
        return arr[0]

    mid = n // 2
    left = merge_k_lists(arr[:mid])
    right = merge_k_lists(arr[mid:])

    return merge_two_lists(left, right)


nested_list = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(nested_list)

print("Sorted list:", merged_list)
