# coding=utf-8

"""Generate Parentheses.

>>> solve = _solve1
>>> solve(3)
['((()))', '(()())', '(())()', '()(())', '()()()']
"""


def _solve(n):
    cache = {1: ['()']}

    # 下面的函数其实可以简化
    def _dfs(left, right):
        if (right - left) in cache:
            return cache[right - left]
        res = []
        for mid in xrange(right, left, -2):
            in_arr = _dfs(left + 1, mid - 1) if mid - 1 > left + 1 else ['']
            out_arr = _dfs(mid + 1, right) if right > mid else ['']
            for in_str in in_arr:
                tmp = '(' + in_str + ')'
                for out_str in out_arr:
                    res.append(tmp + out_str)
        cache[right - left] = res
        return res

    _dfs(0, n * 2 - 1)
    return cache[n * 2 - 1]


# 与上述思路相同的迭代做法
def _solve1(n):
    dp = [[] for i in range(n + 1)]
    dp[0].append('')
    for i in range(n + 1):
        for j in range(i):
            dp[i] += ['(' + in_str + ')' + out_str for in_str in dp[j] for out_str in dp[i - j - 1]]
    return dp[n]


# 另一种比较容易想到的做法
def _solve1(n):
    ans = []

    def _dfs(cur_str, left, right):
        if left == right == n:
            ans.append(cur_str)
            return None
        if left < n:
            _dfs(cur_str + '(', left + 1, right)
        if right < left:
            _dfs(cur_str + ')', left, right + 1)

    _dfs('', 0, 0)
    return ans
