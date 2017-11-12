# coding=utf-8

"""Longest Word in Dictionary.

>>> solve = _solve1
>>> solve(["a", "banana", "app", "appl", "ap", "apply", "apple"])
'apple'
>>> solve(["rac", "rs", "ra", "on", "r", "otif", "o", "onpdu", "rsf", "rs", "ot", "oti", "racy", "onpd"])
'otif'
"""


def _solve(words):
    ans, root = '', {}
    for word in sorted(words):
        cur_len, cur_node = 0, root
        while cur_len < len(word) and word[cur_len] in cur_node:
            cur_node = cur_node[word[cur_len]]
            cur_len += 1
        if len(word) == cur_len + 1:
            cur_node[word[-1]] = {}
            ans = word if len(word) > len(ans) else ans
    return ans


def _solve1(words):
    ans, res = '', {''}
    for word in sorted(words):
        if word[:-1] in res:
            res.add(word)
            ans = max(ans, word, key=len)
    return ans
