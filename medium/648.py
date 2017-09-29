# coding=utf-8

"""Replace Words.

>>> solve = _solve
>>> solve(["cat", "bat", "rat"], "the cattle was rattled by the battery")
'the cat was rat by the bat'
"""

import collections
import re


def _solve(dict, sentence):
    sorted_dict = sorted(dict, key=len)

    def _replace(res):
        word = res.group(0)
        for root in sorted_dict:
            if word.startswith(root):
                return root
        return word

    return re.sub('(\w+)', _replace, sentence)


# 比较传统的 Trie 写法
def _solve1(dict, sentence):
    class TrieNode(object):
        def __init__(self, val):
            self.val = val
            self.children = [None] * 26
            self.is_word = False

    def _build_trie(words):
        root = TrieNode('')
        for word in words:
            tmp = root
            for ch in word:
                diff = ord(ch) - ord('a')
                if not tmp.children[diff]:
                    tmp.children[diff] = TrieNode(ch)
                tmp = tmp.children[diff]
            tmp.is_word = True
        return root

    root = _build_trie(dict)

    def _get_shortest_path(word):
        length, node = 0, root
        for ch in word:
            length += 1
            diff = ord(ch) - ord('a')
            if node.children[diff]:
                if node.children[diff].is_word:
                    return word[:length]
                node = node.children[diff]
            else:
                return word
        return word

    return ' '.join(map(_get_shortest_path, sentence.split()))


# 使用 defaultdict 的做法
# 参考自 https://discuss.leetcode.com/topic/96826/python-straightforward-with-explanation-prefix-hash-trie-solutions
def _solve2(dict, sentence):
    def _trie():
        return collections.defaultdict(_trie)

    trie = _trie()
    IS_WORD = True
    for root in dict:
        cur = trie
        for letter in root:
            cur = cur[letter]
        cur[IS_WORD] = root

    def _replace(word):
        cur = trie
        for letter in word:
            if letter not in cur:
                break
            cur = cur[letter]
            if IS_WORD in cur:
                return cur[IS_WORD]
        return word

    return " ".join(map(_replace, sentence.split()))
