# coding=utf-8

"""Kth Smallest Element in a Sorted Matrix.

>>> solve = _solve
>>> [solve([[1,  5,  9], [10, 11, 13], [12, 13, 15]], i) for i in range(1, 10)]
[1, 5, 9, 10, 11, 12, 13, 13, 15]
"""

import heapq


def _solve(matrix, k):
    return sorted(reduce(lambda x, y: x + y, matrix, [None]))[k]


def _solve1(matrix, k):
    heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
    heapq.heapify(heap)
    val = 0
    for _ in range(k):
        val, i, j = heapq.heappop(heap)
        if j + 1 < len(matrix[0]):
            heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
    return val


# 注释的为二分写法另一种写法（只有小改动）
# 在 height 内层的循环中，易于想到的方法是使用二分查找，但是复杂度为 O(n * log(n))
# 利用矩阵行列均排好序的性质可以得到 O(n) 的做法
def _solve2(matrix, k):
    height, width = len(matrix), len(matrix[0])
    left, right = matrix[0][0], matrix[-1][-1]
    # while left <= right:
    while left < right:
        mid = (left + right) / 2
        count, upper = 0, width - 1
        for i in xrange(height):
            while upper >= 0 and matrix[i][upper] > mid:
                upper -= 1
            count += upper + 1
        if count < k:
            left = mid + 1
        else:
            right = mid
        # if count < k:
        #     left = mid + 1
        # else:
        #     right = mid - 1
    return left


# 此题的 O(n)（O(#rows)） 复杂度的解法（来自 paper(Selection in X + Y and matrices with sorted rows and columns)）
# 请参考 https://discuss.leetcode.com/topic/53126/o-n-from-paper-yes-o-rows
