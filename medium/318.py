# coding=utf-8

"""Maximum Product of Word Lengths.

>>> solve = _solve
>>> solve(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
4
>>> solve(["a", "aa", "aaa", "aaaa"])
0
"""


# bit 操作，简单而快速的写法，参考自
# https://discuss.leetcode.com/topic/46685/python-solution-beats-99-67
def _solve(words):
    res = {}
    for word in words:
        bit_int = 0
        for ch in word:
            bit_int |= (1 << (ord(ch) - 97))
        res[bit_int] = max(res.get(bit_int, 0), len(word))
    return max([res[a] * res[b] for a in res for b in res if not a & b] or [0])


# 除了 res 总是存储最大值的优化外，你还可以考虑计算 max 值的其他优化
# 在二重循环中提前 break，取避免无用计算，具体
# 可参考 https://discuss.leetcode.com/topic/31769/32ms-java-ac-solution
