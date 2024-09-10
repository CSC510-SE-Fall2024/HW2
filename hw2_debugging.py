import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import rand


def merge_sort(arr):
    """
    Perform a merge sort on the input array.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list of elements.
    """
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merge two sorted lists into one sorted list.

    Args:
        left_arr (list): The first sorted list.
        right_arr (list): The second sorted list.

    Returns:
        list: The merged and sorted list.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    while right_index < len(right_arr):
        merge_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1

    while left_index < len(left_arr):
        merge_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1

    return merge_arr


if __name__ == "__main__":
    arr = rand.random_array([None] * 20)
    arr_out = merge_sort(arr)
    print(arr_out)
