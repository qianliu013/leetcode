# coding=utf-8

"""Third Maximum Number."""

from __future__ import print_function
import heapq
import test_tools


def _solve(nums):
    max_nums = [nums[0], nums[0], nums[0]]

    def _sort():
        if max_nums[0] > max_nums[2]:
            max_nums[0], max_nums[2] = max_nums[2], max_nums[0]
        if max_nums[0] > max_nums[1]:
            max_nums[0], max_nums[1] = max_nums[1], max_nums[0]

    length = 1
    for num in nums[1:]:
        if num in max_nums:
            continue
        if length == 1:
            if max_nums[2] < num:
                max_nums[2] = num
            if max_nums[2] > num:
                max_nums[1] = num
            length = 2
            continue

        if length == 2:
            length = 3
            max_nums[0] = num
            _sort()
            continue

        if max_nums[0] < num:
            max_nums[0] = num
            _sort()

    return max_nums[0] if length == 3 else max_nums[2]


def _solve1(nums):
    set_nums = set()
    heapq_nums = []
    for num in nums:
        if num not in set_nums:
            set_nums.add(num)
            heapq.heappush(heapq_nums, num)
            if len(heapq_nums) > 3:
                set_nums.remove(heapq.heappop(heapq_nums))
    if len(heapq_nums) < 3:
        while len(heapq_nums) > 1:
            heapq.heappop(heapq_nums)
    return heapq_nums[0]


if __name__ == '__main__':
    print (_solve1([1]))
    print (_solve1([1, 2]))
    print (_solve1([1, 2, 3]))
    print (_solve1([2, 2, 3, 1]))
    print (_solve1([1, 2, 1, 2, 1]))
    for _ in range(5):
        TEST_DATA = test_tools.generate_random_arr(7, 1, 5)
        print (TEST_DATA, _solve1(TEST_DATA))
