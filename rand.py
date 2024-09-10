import subprocess

def random_array(arr):
    """
    Populate the given list with random integers between 1 and 20.

    Args:
        arr (list): A list to be filled with random integers.

    Returns:
        list: The input list with each element replaced by a random integer between 1 and 20.
    """
    for i in range(len(arr)):
        result = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, text=True, check=True
        )
        arr[i] = int(result.stdout.strip())
    return arr