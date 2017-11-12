# coding=utf-8

"""Repeated String Match.

>>> solve = _solve
>>> solve("abcd", "cdabcdab")
3
>>> solve("abcd", "abcd")
1
>>> solve("abababaaba", "aabaaba")
2
"""


# 两行解法，参考自 https://discuss.leetcode.com/topic/105618/intuitive-python-2-liner
# t = -(-len(B) // len(A)) # Equal to ceil(len(b) / len(a))
# return t * (B in A * t) or (t + 1) * (B in A * (t + 1)) or -1

def _solve(A, B):
    factor = len(B) / len(A) + 1
    if B in A * factor:
        return (factor - 1) if B in A * (factor - 1) else factor
    else:
        return 2 if B in A * 2 else -1

# 官方 Solution 有种 Rabin-Karp (Rolling Hash) 方法，较为复杂
# https://leetcode.com/articles/repeated-string-match/
