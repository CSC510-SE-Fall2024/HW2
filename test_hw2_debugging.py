import hw2_debugging

def test_empty_array():
    assert hw2_debugging.mergeSort([]) == []


def test_sorted_array():
    assert hw2_debugging.mergeSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_random_array():
    arr = [10, 2, 14, 3, 7]
    sorted_arr = [2, 3, 7, 10, 14]
    assert hw2_debugging.mergeSort(arr) == sorted_arr
