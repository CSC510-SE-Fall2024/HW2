import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import rand


def mergeSort(arr):
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

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))


def recombine(leftArr, rightArr):
    """
    Merge two sorted lists into one sorted list.

    Args:
        leftArr (list): The first sorted list.
        rightArr (list): The second sorted list.

    Returns:
        list: The merged and sorted list.
    """
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1

    while rightIndex < len(rightArr):
        mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
        rightIndex += 1

    while leftIndex < len(leftArr):
        mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        leftIndex += 1

    return mergeArr


arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)
