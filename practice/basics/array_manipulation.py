import random

# Dimensions
rows = 3
cols = 4

# Generate two 2D arrays with random integers between 0 and 100
array1 = [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]
array2 = [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]

print("Array 1:")
for row in array1:
    print(row, end=',' if row != len(array1)-1 else '')

print("\nArray 2:")
for row in array2:
    print(row, end=',' if row != len(array2)-1 else '')

array1 = [
    [84, 35, 100, 97],
    [29, 54, 3, 16],
    [56, 61, 46, 51],
    [2, 30, 1, 3]
]

array2 = [
    [30, 89, 64, 69],
    [14, 13, 61, 35],
    [83, 41, 48, 60],
    [21, 33, 10, 5]
]

def rotate_matrix(array):
    result= []
    for l in range(len(array)):
        for i in range(len(array[l])):
            if l == 0:
                result.append([])
            result[i].append(array[l][i])

    for l in result:
        l.reverse()

    return result

print("============================================")
print("[")
for l in rotate_matrix(array1):
    print("\t[", end='')
    for i in l:
        print(f"{i}", end=", ")
    print("],")
print("]")


def add_number_to_list(num:int, a:list[int]=[]):
    new_array = a
    new_array.append(num)
    return new_array

print("\n")
array = add_number_to_list(1, [1, 2, 3])
array2 = add_number_to_list(2)

print(array)
print(array2)