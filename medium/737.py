# coding=utf-8

"""Sentence Similarity II.

>>> solve = _solve
>>> solve(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "good"], ["fine", "good"], ["drama", "acting"], ["skills", "talent"]])
True
"""


# 可以认为是并查集（Union-Find）
# 正规、完整的并查集实现可参考 547.py
def _solve(words1, words2, pairs):
    if len(words1) != len(words2):
        return False
    if not words1:
        return True
    res = {}

    def _find(word):
        if word not in res:
            res[word] = word
        elif word != res[word]:
            res[word] = _find(res[word])
        return res[word]

    for word1, word2 in pairs:
        root1, root2 = _find(word1), _find(word2)
        if root1 != root2:
            res[root1] = root2

    for word1, word2 in zip(words1, words2):
        if _find(word1) != _find(word2):
            return False
    return True
