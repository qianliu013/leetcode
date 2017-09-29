# coding=utf-8

"""4Sum II.

>>> solve = _solve
>>> solve([1,2], [-2,-1], [-1,2], [0,2])
2
"""

# import bisect
import collections


def _solve(A, B, C, D):
    def _sorted_two_sum(arr1, arr2):
        return sorted([num1 + num2 for num1 in arr1 for num2 in arr2])
    # arr1, arr2 = _sorted_two_sum(A, B), _sorted_two_sum(C, D)
    # return sum((bisect.bisect_right(arr2, -num1) - bisect.bisect_left(arr2, -num1) for num1 in arr1))
    arr1, arr2 = _sorted_two_sum(A, B), _sorted_two_sum(C, D)
    length = len(arr2)
    i, j, ans = 0, length - 1, 0
    count_i, count_j = 1, 1
    while i < length and j > -1:
        if count_i == 1:
            while count_i + i < length and arr1[i] == arr1[i + count_i]:
                count_i += 1
        if count_j == 1:
            while j - count_j > -1 and arr2[j] == arr2[j - count_j]:
                count_j += 1
        if arr1[i] + arr2[j] == 0:
            ans += count_i * count_j
            i += count_i
            j -= count_j
            count_i = 1
            count_j = 1
        elif arr1[i] + arr2[j] > 0:
            j -= count_j
            count_j = 1
        else:
            i += count_i
            count_i = 1
    return ans


def _solve1(A, B, C, D):
    two_sum_dict = collections.Counter(a + b for a in A for b in B)
    return sum(two_sum_dict[-c - d] for c in C for d in D)


# 因为代码细节不好，下面的代码会 Memory Limit Exceeded
def _solve2(A, B, C, D):
    def _dict_of_two_sum(arr1, arr2):
        result = collections.defaultdict(int)
        for num1 in arr1:
            for num2 in arr2:
                result[num1 + num2] += 1
        return result

    dict1, dict2 = _dict_of_two_sum(A, B), _dict_of_two_sum(C, D)
    ans = 0
    for key, value in dict1.items():
        ans += dict2[-key] * value
    return ans
