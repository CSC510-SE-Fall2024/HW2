import sys
import os

# Adding the directory of this file to the system path to allow imports from 'hw2_debugging'
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import hw2_debugging

def test_empty_array():
    """
    Test case for an empty array.

    Asserts that calling mergeSort on an empty list returns an empty list.
    """
    assert hw2_debugging.mergeSort([]) == []

def test_sorted_array():
    """
    Test case for an already sorted array.

    Asserts that calling mergeSort on a list that is already sorted returns the same list.
    """
    assert hw2_debugging.mergeSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_random_array():
    """
    Test case for a random unsorted array.

    Asserts that calling mergeSort on a randomly ordered list returns a correctly sorted list.
    """
    arr = [10, 2, 14, 3, 7]
    sorted_arr = [2, 3, 7, 10, 14]
    assert hw2_debugging.mergeSort(arr) == sorted_arr
