# coding=utf-8

"""Shuffle an Array."""

import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.__nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # 可以使用 timeit 测试，数组复制使用  list(arr) 的速度快于 arr[:]
        ans = list(self.__nums)
        for i in xrange(len(self.__nums)):
            rand_int = random.randrange(i + 1)
            ans[i], ans[rand_int] = ans[rand_int], self.__nums[i]
        return ans
