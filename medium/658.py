# coding=utf-8
"""Find K Closest Elements.

>>> solve = _solve2
>>> solve(range(1, 6), 4, -1)
[1, 2, 3, 4]
>>> solve(range(1, 6), 4, 6)
[2, 3, 4, 5]
>>> solve(range(1, 6), 4, 3)
[1, 2, 3, 4]
>>> solve(range(1, 6), 1, 3)
[3]
"""

import bisect


# sorted is stable.
def _solve(arr, k, x):
    return sorted(sorted(arr, key=lambda val: abs(val - x))[:k])


# 这道题的双指针法要注意的就是 bisect.bisect_left 返回的是什么与边界条件判断
def _solve1(arr, k, x):
    left = right = bisect.bisect_left(arr, x)
    while right - left < k:
        if left == 0:
            return arr[:k]
        if right == len(arr):
            return arr[-k:]
        if x - arr[left - 1] <= arr[right] - x:
            left -= 1
        else:
            right += 1
    return arr[left:right]


# 此题可以使用二分：其思路是子数组 arr[start:start+k) 与 x 差值的绝对值的 sum 先递减后递增
# 因此我们要获得非递减的第一项即可；因为相邻两个子数组差值仅与首末项有关，所以无需计算 sum
def _solve2(arr, k, x):
    low, high = 0, len(arr) - k
    while low < high:
        mid = (low + high) / 2
        # if abs(arr[mid] - x) > abs(arr[mid + k] - x):
        # 绝对值不等式可以转换为非绝对值不等式
        if x - arr[mid] > arr[mid + k] - x:
            low = mid + 1
        else:
            high = mid
    return arr[low:low + k]
