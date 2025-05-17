


def array_manipulation(n, queries):
    """
        This implementation updates each element in the specified range for every query,
        leading to a time complexity of approximately O(n * m)
        where m is the number of queries—inefficient for large inputs
        :param n: vector size
        :param queries: updates to vector
        :return: max value after all updates to vector
    """
    # initializes the 0s vector
    vector = [0] * n
    max_val = -1
    for q in queries:
        vector = [x + q[2] if q[0] - 1 <= ind < q[1] else x for ind, x in enumerate(vector)]

    for value in vector:
        if value > max_val:
            max_val = value

    return max_val


def array_manipulation_prefix_sum(n, queries):
    """
    Difference array technique perform range updates in O(1) time per query,
    and then compute the prefix sum at the end. This reduces overall complexity to O(n + m)

    How this give the correct maximum?

        :param n:
        :param queries:
        :return: max value after all updates to vector
    """
    # Initialize difference array
    diff_vector = [0] * (n)

    # Apply all range updates in O(1) per query
    for start, end, val in queries:
        diff_vector[start - 1] += val
        if end < n:
            diff_vector[end] -= val

    # After all queries, the diff array contains the incremental changes at each index. Uncomment below line for demo:
    # print(diff_vector)
    max_val = -1
    current_sum = 0

    # To reconstruct the actual values of the original array after all updates, compute the prefix sum of diff array
    # -> prefix sums to get final array values
    for i in range(n):
        current_sum += diff_vector[i]
        if current_sum > max_val:
            max_val = current_sum

    return max_val

n = 10
queries = [
    [1, 5, 3],
    [4, 8, 7],
    [6, 9, 1],
]
[3, 3, 3, 3, 3, 0, 0, 0, 0, 0]
[3, 3, 3, 3, 10, 7, 7, 7, 0, 0]
[3, 3, 3, 3, 10, 7, 8, 8, 1, 0]
print(array_manipulation_prefix_sum(n, queries))