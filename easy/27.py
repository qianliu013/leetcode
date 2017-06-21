# coding=utf-8

"""Remove Element."""

from __future__ import print_function


# 我刚开始多想了点
# 下面的方法可以保证原数组内的元素不变
# 其余的都是覆盖了
def _solve(nums, val):
    front = 0
    end = -1
    length = len(nums)
    while front - end <= length:
        if nums[front] == val and nums[end] != val:
            nums[front], nums[end] = nums[end], nums[front]
        if nums[front] != val:
            front += 1
        if nums[end] == val:
            end -= 1
    return front



def _solve1(nums, val):
    new_len = 0
    for num in nums:
        if num != val:
            nums[new_len] = num
            new_len += 1
    return new_len


def _solve2(nums, val):
    length = len(nums)
    for index in xrange(length):
        while(nums[index] == val and index < length):
            length -= 1
            nums[index] = nums[length]
    return length


if __name__ == '__main__':
    print (_solve1([], 3))
    print (_solve1([2], 3))
    print (_solve1([3], 3))
    print (_solve1([2, 2, 2], 3))
    print (_solve1([3, 3, 3, 2], 3))
    print (_solve1([2, 2, 3, 3, 3], 3))
    print (_solve1([3, 3, 2, 2, 3], 3))
