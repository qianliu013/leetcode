# coding=utf-8

"""Sort Colors.

>>> solve = _solve
"""

import collections


def _solve(nums):
    counter = collections.Counter(nums)
    i = [0]

    def _process(target):
        for _ in xrange(counter[target]):
            nums[i[0]] = target
            i[0] += 1
    map(_process, [0, 1, 2])


# 这种思路的双 index 写法其具体实现其实很多变，可以有各种各样的写法，但是由于 python 没有 `++` `--`，
# 所以最后的代码看起来也许没那么简洁，具体实现可参考 discuss 的代码
# https://discuss.leetcode.com/topic/5422/share-my-at-most-two-pass-constant-space-10-line-solution
# https://discuss.leetcode.com/topic/6968/four-different-solutions
def _solve1(nums):
    i, end0, start2 = 0, 0, len(nums) - 1
    while i <= start2:
        if nums[i] == 0 and i > end0:
            nums[end0], nums[i] = 0, nums[end0]
            end0 += 1
        elif nums[i] == 2 and i < start2:
            nums[start2], nums[i] = 2, nums[start2]
            start2 -= 1
        else:
            i += 1


# 思路较为清晰的三 index 写法， 代码参考自
# https://discuss.leetcode.com/topic/26181/ac-python-in-place-one-pass-solution-o-n-time-o-1-space-no-swap-no-count
def _solve2(nums):
    i0 = i1 = 0
    for i2, num in enumerate(nums):
        nums[i2] = 2
        if num < 2:
            nums[i1] = 1
            i1 += 1
        if num == 0:
            nums[i0] = 0
            i0 += 1
