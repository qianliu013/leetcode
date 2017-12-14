# coding=utf-8

"""Elimination Game.

>>> solve = _solve
>>> solve(13)
6
"""


# 此题的一种思路是模拟
# 迭代最后一个留下来的数
def _solve(n):
    step, start, flag = 1, 1, 1
    while True:
        next_start = start + step * flag
        if 1 <= next_start <= n:
            step *= 2
            if flag > 0:
                start = next_start + (n - next_start) / step * step * flag
            else:
                start = next_start + (next_start - 1) / step * step * flag
            flag = -flag
        else:
            return start


# 一种更加简洁的写法，来自 discuss 最高票
# https://discuss.leetcode.com/topic/59293/java-easiest-solution-o-logn-with-explanation
def _solve1(n):
    left, remaining, step, head = 1, n, 1, 1
    while remaining > 1:
        if left or remaining & 1:
            head += step
        remaining >>= 1
        step *= 2
        left ^= 1
    return head


# 另一种思路是求递推式
# 一种比较容易理解的 two-pass 方法，来自
# https://discuss.leetcode.com/topic/59992/c-29ms-with-complexity-of-log4-n-and-explanation
def _solve2(n):
    def _dfs(n):
        if n == 1:
            return 1
        if n <= 4:
            return 2
        if n % 2 != 0:
            n -= 1
        if n % 4 != 0:
            return 4 * _dfs(n / 4)
        return 4 * _dfs(n / 4) - 2
    return _dfs(n)


# 需要细心考虑的递推式：f(n)=2(1+n/2-f(n/2))，可参考
# https://discuss.leetcode.com/topic/61875/one-line-java-solution-based-on-josephus-problem
def _solve3(n):
    def _dfs(n):
        return 1 if n == 1 else (2 * (1 + n / 2 - _dfs(n / 2)))
    return _dfs(n)


# 来自上个链接的另一种解法
def _solve4(n):
    return ((n | 0x55555555555555) & ((1 << (n.bit_length() - 1)) - 1)) + 1
