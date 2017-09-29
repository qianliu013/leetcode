# coding=utf-8

"""Implement Magic Dictionary."""


# 暴力使用 hashmap 存储、计算所有可能性的方法，如：
# https://discuss.leetcode.com/topic/103033/python-without-26-factor-in-complexity
# https://discuss.leetcode.com/topic/102992/easy-14-lines-java-solution-hashmap


class MagicDictionary(object):

    def __init__(self):
        """Initialize your data structure here."""
        self.__trie = [None] * 27

    def buildDict(self, dict):
        """Build a dictionary through a list of words.

        :type dict: List[str]
        :rtype: void
        """
        for string in dict:
            self.__build(string)

    def search(self, word):
        """Return if there is any word in the trie that equals to the given word after modifying exactly one character.

        :type word: str
        :rtype: bool
        """
        return self.__find(word, 0, self.__trie, False)

    def __build(self, string):
        arr = self.__trie
        for char in string:
            if not arr[ord(char) - 97]:
                arr[ord(char) - 97] = [None] * 27
            arr = arr[ord(char) - 97]
        arr[26] = True

    def __find(self, string, cur_index, arr, modified):
        if cur_index == len(string):
            return bool(arr[26] and modified)
        res = False
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if arr[ord(char) - 97]:
                if char == string[cur_index]:
                    res = res or self.__find(string, cur_index + 1, arr[ord(char) - 97], modified)
                elif not modified:
                    res = res or self.__find(string, cur_index + 1, arr[ord(char) - 97], not modified)
        return res
