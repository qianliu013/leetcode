# coding=utf-8

"""Rotate Array."""

from __future__ import print_function
import collections


def _solve(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[0:-k]


def _solve1(nums, k):
    def GCD(a, b):
        return GCD(b, a % b) if a % b else b

    length = len(nums)
    k %= length
    if k == 0:
        return
    end = GCD(length, k)
    for i in xrange(end):
        prev, nums[i], index = nums[i], nums[i - k], (i + k) % length
        while index != i:
            prev, nums[index], index = nums[index], prev, (index + k) % length


def _solve2(nums, k):
    k %= len(nums)
    nums_que = collections.deque(nums)
    while k:
        nums_que.appendleft(nums_que.pop())
        k -= 1
    for i, num in enumerate(nums_que):
        nums[i] = num


def _solve3(nums, k):
    def _reverse(start, end):
        while start < end:
            nums[start], nums[end - 1], start, end = nums[end - 1], nums[start], start + 1, end - 1

    k %= len(nums)
    _reverse(0, len(nums))
    _reverse(0, k)
    _reverse(k, len(nums))


# 参考自 https://discuss.leetcode.com/topic/9801/summary-of-c-solutions
# 当 n > 2k 时，很容易理解；当 n < 2k 时，会导致最后的 n - k 个数顺序不对
# 此时需要交换的数量则变为 n - k，k 则 k 变为 k % (n - k)
# 然后继续此过程，直至 k 为 0
def _solve4(nums, k):
    length = len(nums)
    start = 0
    while k:
        print (nums, k, length)
        k %= length
        for i in xrange(k):
            nums[start + i], nums[-k + i] = nums[-k + i], nums[start + i]
        start += k
        length -= k
    print (nums, k, length)


if __name__ == '__main__':
    NUMS = range(13)
    _solve4(NUMS, 5)
    exit(0)
    NUMS = [1, 2, 3, 4, 5, 6]
    _solve3(NUMS, 6)
    print (NUMS)
    NUMS = [1, 2, 3, 4, 5, 6]
    _solve(NUMS, 6)
    print (NUMS)
