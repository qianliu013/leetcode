# coding=utf-8

"""Range Sum Query - Immutable."""

from __future__ import print_function


class NumArray(object):
    """Sum."""

    def __init__(self, nums):
        """
        Init.

        :type nums: List[int]
        """
        self.__nums = nums
        self.__sums = []
        for num in nums:
            self.__sums.append(num + (self.__sums[-1] if self.__sums else 0))

    def sumRange(self, i, j):
        """
        Sum.

        :type i: int
        :type j: int
        :rtype: int
        """
        return self.__sums[j] - self.__sums[i] + self.__nums[i]


if __name__ == '__main__':
    arr = NumArray([-2, 0, 3, -5, 2, -1])
    print (arr.sumRange(0, 2))
    print (arr.sumRange(2, 5))
    print (arr.sumRange(0, 5))
