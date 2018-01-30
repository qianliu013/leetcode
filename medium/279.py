# coding=utf-8

"""Perfect Squares.

>>> solve = _solve
"""


# 此题不太好的一点是没给数据范围，假设数据很大的话，dp 就是不可行的
# 因此，我最初的想法是 深搜 + 减枝，即根据是否已得到的结果来减去不可能优于此的结果
# 以下代码是很快的，59ms(97.87%)，十分接近于纯数学解法
def _solve(n):
    ans = [n]

    def _dfs(cur, max_n, acc):
        max_n = min(max_n, int(cur ** 0.5))
        for i in xrange(max_n, 0, -1):
            square = i * i
            if cur > (ans[0] - acc - 1) * square:
                return
            remaining = cur - square
            if remaining == 0:
                ans[0] = min(ans[0], acc + 1)
            else:
                _dfs(remaining, i, acc + 1)

    _dfs(n, n, 0)
    return ans[0]


# 另一种思路是 bfs，即先得到为 1 个数平方和的结果集，在由此得到两个数的，以此扩展
# 如果未知 four-square_theorem，此方法的时间复杂度也可能会很高
# 而且如前所述，如果不知道数据范围，也许会超内存限制（？）
# 实现代码可见：https://discuss.leetcode.com/topic/26262/short-python-solution-using-bfs

# 虽然 dp 是 trivial，但是可以看下下面 discuss 的链接，如何跨测试保存数据
# https://discuss.leetcode.com/topic/23812/static-dp-c-12-ms-python-172-ms-ruby-384-ms

# 最后是数学解法，Wiki：https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
def _solve1(n):
    while n % 4 == 0:
        n /= 4
    if n % 8 == 7:
        return 4
    for i in xrange(n + 1):
        temp = i * i
        if temp <= n:
            if int((n - temp) ** 0.5) ** 2 + temp == n:
                return 1 + (0 if temp == 0 else 1)
        else:
            break
    return 3
