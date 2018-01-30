# coding=utf-8

"""Insert Delete GetRandom O(1)."""

import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__dict = {}
        self.__arr = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.__dict:
            return False
        self.__dict[val] = len(self.__arr)
        self.__arr.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.__dict:
            index = self.__dict[val]
            self.__arr[index], self.__arr[-1] = self.__arr[-1], self.__arr[index]
            self.__dict[self.__arr[index]] = index
            self.__arr.pop()
            del self.__dict[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.__arr)
