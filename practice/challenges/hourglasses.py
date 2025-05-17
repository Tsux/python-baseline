'''
Given a 6x6 2D array 'arr', an hourglass is a subset of values with indices falling in the following pattern:
a b c
  d
e f g

There are 16 hourglasses in a 6x6 2D array. The 'hourglass sum' is the sum of the values in an hourglass.
Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.
'''
import pytest
from collections import Counter

test_samples = [
    ([
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0,  0, 8,  6, 6, 0],
        [0,  0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    # For above 2D array, expected max sum is 28
    ], 28),
    ([
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 9, 2, -4, -4, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    # For above 2D array, expected max sum is 13
    ], 13),
    ([
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    # For above 2D array, expected max sum is 19
    ], 19)
]
"fcrxzwscanmligyxyvym"
"jxwtrhvujlmrpdoqbisbwhmgpmeoke"
a = "rxwsmligxvm" "rxwsmligv"
b = "xwrvlmriswmgm" "xwrvlmisg"

def hourglass_sum(arr):
    """
    Receives a 2D square array and returns the hourglass with greater sum from matrix
    :param arr: entry matrix
    :return: hourglass with greater sum out of identified hourglasses in the entry matrix
    """
    n = len(arr)

    greater_sum = None
    for i in range(n-2):
        for j in range(n-2):
            cur_sum = 0
            cur_sum += arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            cur_sum += arr[i + 1][j + 1]
            cur_sum += arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]

            if greater_sum is None or cur_sum > greater_sum:
                greater_sum = cur_sum

    return greater_sum

@pytest.mark.parametrize(
    "arr,expected_max_sum", test_samples
)
def test_hourglass_sum(arr, expected_max_sum):
    assert hourglass_sum(arr) == expected_max_sum