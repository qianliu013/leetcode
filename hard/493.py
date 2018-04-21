# coding=utf-8
"""Reverse Pairs.

>>> solve = _solve
>>> solve([1, 3, 2, 3, 1])
2
>>> solve([2, 4, 3, 5, 1])
3
"""

# 此题的其他解法包括
# - BST：手动维护一颗二叉搜索树，虽然不做优化最坏情况复杂度为 O(n^2)，但是此题可过
# - BIT：树状数组，利用其 O(log(n)) 时间复杂度内修改单个元素并且维护区间信息的性质可作
# 具体可参考此题的 solution


def _solve(nums):
    def _merge(low, mid, high):
        l_i, r_i = low, mid + 1
        total = 0
        while l_i <= mid and r_i <= high:
            if nums[l_i] > 2 * nums[r_i]:
                total += mid + 1 - l_i
                r_i += 1
            else:
                l_i += 1

        aux[low:high + 1] = nums[low:high + 1]
        l_i, r_i = low, mid + 1
        for i in xrange(low, high + 1):
            if l_i > mid:
                nums[i] = aux[r_i]
                r_i += 1
            elif r_i > high:
                nums[i] = aux[l_i]
                l_i += 1
            elif aux[r_i] < aux[l_i]:
                nums[i] = aux[r_i]
                r_i += 1
            else:
                nums[i] = aux[l_i]
                l_i += 1
        return total

    def _sort(low, high):
        if low < high:
            mid = low + (high - low) / 2
            total = _sort(low, mid) + _sort(mid + 1, high)
            return total + _merge(low, mid, high)
        return 0

    aux = [0] * len(nums)
    return _sort(0, len(nums) - 1)
