# coding=utf-8

"""Map Sum Pairs."""

# 使用 map 的暴力法和前缀字符串 map 就不写了


class MapSum(object):

    def __init__(self):
        """Initialize your data structure here."""
        self.__root = {}

    # 可以使用一个额外的 map 用于查找已存在的字符串，我在这里为了避免使用它而做了稍微麻烦的处理
    def insert(self, key, val):
        """Insert.

        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.__root
        for char in key:
            if char not in node:
                node[char] = {'sum': 0}
            node = node[char]
        if 'origin' in node:
            origin_value = -node['origin']
        else:
            origin_value, node['origin'] = 0, val
        node = self.__root
        for char in key:
            node = node[char]
            node['sum'] += origin_value + val

    def sum(self, prefix):
        """Sum.

        :type prefix: str
        :rtype: int
        """
        node = self.__root
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return 0
        return node['sum']
