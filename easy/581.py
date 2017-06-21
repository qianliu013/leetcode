# coding=utf-8

"""Shortest Unsorted Continuous Subarray."""

from __future__ import print_function
import test_tools


def _solve(nums):
    start, end = 0, len(nums) - 1
    while start < end:
        if nums[start] > nums[start + 1]:
            break
        start += 1
    if start + 1 > end:
        return 0
    while end - 1 > -1:
        if nums[end - 1] > nums[end]:
            break
        end -= 1
    min_mid, max_mid = min(nums[start:end + 1]), max(nums[start:end + 1])
    while start > -1:
        if nums[start] <= min_mid:
            break
        start -= 1
    while end < len(nums):
        if max_mid <= nums[end]:
            break
        end += 1
    return end - start - 1


def _solve1(nums):
    not_same_indexes = [i for i in xrange(len(nums)) if nums[i] != sorted(nums)[i]]
    return not_same_indexes[-1] - not_same_indexes[0] + 1 if not_same_indexes else 0


def _solve2(nums):
    length = len(nums) - 1
    left, right, left_stack, right_stack = length + 1, -1, [], []
    for i, num in enumerate(nums):
        while left_stack and nums[left_stack[-1]] > num:
            left = min(left_stack.pop(), left)
        left_stack.append(i)

        while right_stack and nums[right_stack[-1]] < nums[length - i]:
            right = max(right_stack.pop(), right)
        right_stack.append(length - i)
    return right - left + 1 if right > left else 0


# 寻找小于自己右面最小数大的最靠左的位置
# 寻找大于自己左面最大数大的最靠右的位置
def _solve3(nums):
    if len(nums) == 0:
        return 0
    left, right, length, min_num, max_num = -1, -2, len(nums), nums[-1], nums[0]
    for i in xrange(1, length):
        max_num = max(max_num, nums[i])
        min_num = min(min_num, nums[length - i - 1])
        if max_num > nums[i]:
            right = i
        if min_num < nums[length - i - 1]:
            left = length - i - 1
    return right - left + 1


if __name__ == '__main__':
    print (_solve3([]))
    print (_solve3(range(4)))
    print (_solve3([2, 6, 4, 8, 10, 9, 15]))
    for _ in range(27):
        NUMS = test_tools.generate_random_arr(5, 1, 9)
        if _solve(NUMS) != _solve1(NUMS):
            print (NUMS)
            break
