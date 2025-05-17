"""
A left rotation operation on an array shifts each of the array's elements 1 unit to the left.
For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2]
Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

The function is expected to return an INTEGER_ARRAY. The function accepts following parameters:
1. INTEGER_ARRAY a
2. INTEGER d
"""

def rotate_left(a, d):
    for i in range(d):
        item = a.pop(0)
        a.append(item)

    return a

def rotate_right(a, d):
    for i in range(len(a)-d+1):
        item = a.pop(len(a)-1)
        a.insert(0, item)

    return a

def rotate_left_mod(a, d):
    rotate = d % len(a)
    return a[rotate:] + a[:rotate]


print(rotate_left([1, 2, 3, 4, 5], 4))
print(rotate_left_mod([1, 2, 3, 4, 5], 4))
print(rotate_right([1, 2, 3, 4, 5], 3))