# coding=utf-8
"""Rotated Digits.

>>> solve = _solve
>>> solve(10000)
2320
"""


# 此题的偏数学解法可以参考
# https://leetcode.com/problems/rotated-digits/discuss/116530/Easy-Understood-Solution-and-O(logN)
# 思路即：固定某一位，所有低位的可能性都可以很快地算出来
def _solve(N):
    not_valid_set, diff_set = set('347'), set('2569')
    ans = 0
    for num in xrange(1, N + 1):
        set_n = set(str(num))
        ans += bool(not (not_valid_set & set_n) and diff_set & set_n)
    return ans
