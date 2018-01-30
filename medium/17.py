# coding=utf-8
"""Letter Combinations of a Phone Number.

>>> solve = _solve
>>> solve('23')
['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
"""


def _solve(digits):
    if not len(digits):
        return []
    maps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    return reduce(lambda acc, digit: [each + nxt for nxt in maps[digit] for each in acc], digits, [''])
