# coding=utf-8

"""Valid Palindrome II.

>>> solve = _solve1
>>> solve('aba')
True
>>> solve('abca')
True
"""


def _solve(s):
    def _compute_left_right(left, right):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        if left >= right:
            return None
        else:
            return left, right
    res = _compute_left_right(0, len(s) - 1)
    if not res:
        return True
    return not _compute_left_right(res[0] + 1, res[1]) or not _compute_left_right(res[0], res[1] - 1)


# 极简写法，参考了 https://discuss.leetcode.com/topic/103982/python-easy-and-concise-solution
def _solve1(s):
    i = 0
    while i < len(s) / 2 and s[i] == s[~i]:
        i += 1
    s = s[i:len(s) - i]
    return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]
