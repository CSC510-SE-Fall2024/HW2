import subprocess


def random_array(arr):
    """
    Populate the given array with random integers between 1 and 20.

    Args:
        arr (list): A list to be filled with random integers.

    Returns:
        list: The input list with each element replaced by a random integer between 1 and 20.
    """
    shuffled_num = None
    for i in range(len(arr)):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True)
        arr[i] = int(shuffled_num.stdout)
    return arr

