# coding=utf-8

"""Sentence Similarity.

>>> solve = _solve
>>> solve(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "fine"], ["drama", "acting"], ["skills", "talent"]])
True
"""


def _solve(words1, words2, pairs):
    if len(words1) != len(words2):
        return False
    if not words1:
        return True
    res = set(map(tuple, pairs))
    for two_word in zip(words1, words2):
        if two_word not in res and (two_word[1], two_word[0]) not in res and two_word[0] != two_word[1]:
            return False
    return True
