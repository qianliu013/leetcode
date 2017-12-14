# coding=utf-8

"""S.

>>> solve = _solve
>>> solve('abab')
3
>>> solve('bbbab')
4
"""


# 这道题使用 dp 可能会 TLE，有一些优化点需要注意
def _solve(s):
    # 加上这个简单的判断，代码运行时间大概会减少 800ms 左右，这个算是最重要的优化了
    if s == s[::-1]:
        return len(s)
    length = len(s)
    # 二维到一维的优化
    dp = [0] * length
    # 至于如何保存上一次迭代的结果，除了下面的写法外，还可以考虑的写法有
    # - 其他生成一个数组的方法，如 list(dp), dp[:] 等
    # - 最初直接生成两个数组，每次迭代轮换
    # - 每次内循环主动保存上一次迭代结果的一个值（dp[i+1]）
    # 测试可知，速度差距不大
    for j in xrange(length):
        tmp = [0] * length
        tmp[j] = 1
        for i in xrange(j - 1, -1, -1):
            # 下面的更新是一个要注意的地方，我最初写的是
            # tmp[i] = max(dp[i], tmp[i + 1], 2 * (s[i] == s[j]) + dp[i + 1])
            # 实际上上述语句比起下面的来说，是非常慢的
            if s[i] == s[j]:
                tmp[i] = dp[i + 1] + 2
            else:
                tmp[i] = max(tmp[i + 1], dp[i])
        dp = tmp
    return dp[0]
