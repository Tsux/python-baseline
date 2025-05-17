import pytest


def diagonal_difference(arr):
    # Write your code here
    diag_a = 0
    diag_b = 0
    n = len(arr)
    for i in range(n):
        diag_a += arr[i][i]
        diag_b += arr[i][n - 1 - i]


    diff = diag_a - diag_b

    return diff if diff >= 0 else diff * -1


@pytest.mark.parametrize(
    "matrix, expected", [
        (
            [
                [11, 2, 4],
                [4, 5, 6],
                [10, 8, -12],
            ], 15
        ),
        (
            [
                [100, -73, 28, 71, -35, -94, 11],
                [11, 7, -5, 31, 57, -4, -35],
                [-33, 86, 71, 84, 81, 6, 26],
                [-85, 99, -48, -77, 58, 77, 64],
                [34, 37, -72, -47, -94, 60, 12],
                [-23, 81, 63, 52, -76, 23, 62],
                [11, 17, -98, -96, 66, 18, -52]
            ], 53
        )
    ]
)
def test_diagonal_difference(matrix, expected):
    assert diagonal_difference(matrix) == expected
