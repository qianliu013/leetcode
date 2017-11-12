# coding=utf-8

"""Random Pick Index."""

import bisect
import random


class Solution(object):
    def __init__(self, nums):
        """Init.

        :type nums: List[int]
        :type numsSize: int
        """
        self.__num_indexes = [(num, i) for i, num in enumerate(nums)]
        self.__num_indexes.sort()

    def pick(self, target):
        """Pick.

        :type target: int
        :rtype: int
        """
        left = bisect.bisect_left(self.__num_indexes, (target,))
        right = bisect.bisect_left(self.__num_indexes, (target + 1,))
        return self.__num_indexes[random.randrange(left, right)][1]


# Reservoir Sampling
class Solution1(object):
    def __init__(self, nums):
        """Init.

        :type nums: List[int]
        :type numsSize: int
        """
        self.__nums = nums

    def pick(self, target):
        """Pick.

        :type target: int
        :rtype: int
        """
        result, count = -1, 0
        for i, num in enumerate(self.__nums):
            if num == target:
                count += 1
                if random.randrange(count) == 0:
                    result = i
        return result
