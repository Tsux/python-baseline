"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
Each person wears a sticker indicating their initial position in the queue from 1 to n.
Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker.
One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order.
Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
"""
import pytest


def minimum_bribes(q):
    bribes = 0
    next, prox = 1, 2
    for i in range(len(q)-1):
        way = i + 3
        if q[i] > way:
            print("Too chaotic")
            return "Too chaotic"

        if q[i] == way:
            bribes += 2
        elif q[i] == prox:
            bribes += 1
            prox = way
        elif q[i] == next:
            next = prox
            prox = way

    print(bribes)
    return bribes


@pytest.mark.parametrize(
    "queue, expected_bribes", [
        ([2, 1, 5, 3, 4], 3),
        ([2, 5, 1, 3, 4], "Too chaotic"),
        ([1, 2, 5, 3, 7, 8, 6, 4], 7),
        ([1, 2, 5, 3, 4, 7, 8, 6], 4)
    ]
)
def test_minimum_bribes(queue, expected_bribes):
    assert minimum_bribes(queue) == expected_bribes
