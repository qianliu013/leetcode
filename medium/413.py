# coding=utf-8

"""Arithmetic Slices.
>>> solve = _solve1
>>> solve([1,2,3,4])
3
>>> solve([1,2,4])
0
>>> solve([1,2,3,4,5,6,7])
15
>>> solve([1, 1, 1, 2, 3, 5, 7, 9])
5
"""


def _solve(A):
    if not A or len(A) < 3:
        return 0

    result = []
    diff, count = A[1] - A[0], 2
    for i, num in enumerate(A):
        if i < 2:
            continue
        if diff == num - A[i - 1]:
            count += 1
        else:
            if count > 2:
                result.append(count - 2)
            count = 2
            diff = num - A[i - 1]
    if count > 2:
        result.append(count - 2)
    return sum([(x * (x + 1) / 2) for x in result])


def _solve1(A):
    if not A or len(A) < 3:
        return 0

    ans, diff, count = 0, A[1] - A[0], 0
    for i, num in enumerate(A):
        if i < 2:
            continue
        if diff == num - A[i - 1]:
            count += 1
            ans += count
        else:
            count = 0
            diff = num - A[i - 1]
    return ans
