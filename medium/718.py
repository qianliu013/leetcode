# coding=utf-8
"""Maximum Length of Repeated Subarray.

>>> solve = _solve3
>>> solve([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
3
"""

import collections


# O(n ^ 2)
def _solve(A, B):
    len_a, len_b = len(A), len(B)
    dp = [[0] * (len_b + 1) for _ in xrange(len_a)]
    ans = 0
    for i, num_a in enumerate(A):
        for j, num_b in enumerate(B):
            if num_a == num_b:
                dp[i][j] = dp[i - 1][j - 1] + 1
                ans = max(dp[i][j], ans)
    return ans


# 此题另一种 O(n ^ 2) 方法是滑动数组；即想象一个数组不动，另一个数组在此数组滑动
# 最长的长度一定是某一位对齐情况下产生的，以此可解
# 代码参考自 https://discuss.leetcode.com/topic/108785/easy-o-n-2-time-o-1-space-solution-no-dp
def _solve1(A, B):
    len_a, len_b = len(A), len(B)
    ans = 0
    for offset in xrange(-len_a, len_b):
        count, i = 0, max(0, offset)
        while i - offset < len_a and i < len_b:
            if A[i - offset] == B[i]:
                count += 1
                ans = max(ans, count)
            else:
                count = 0
            i += 1
    return ans


# O(n ^ log(n))
# 此题的形式和数据特点其实很容易联想到字符串相关的算法，因此可以用 二分 + 判断子串 的算法
# 但是裸的暴力其复杂度是 O(n ^ 2)，因此需要优化为 O(n)
# set 优化
def _solve2(A, B):
    def _check(length):
        seen = {A[i:i + length] for i in xrange(len(A) - length + 1)}
        return any(B[j:j + length] in seen for j in xrange(len(B) - length + 1))

    A = ''.join(map(chr, A))
    B = ''.join(map(chr, B))

    left, right = 0, min(len(A), len(B)) + 1
    while left < right:
        mid = left + (right - left) / 2
        if _check(mid):
            left = mid + 1
        else:
            right = mid
    return left - 1


# Rabin-Karp algorithm，代码来自：
# https://leetcode.com/articles/maximum-length-of-repeated-subarray/
def _solve3(A, B):
    P, MOD = 113, 10**9 + 7
    Pinv = pow(P, MOD - 2, MOD)

    def check(guess):
        def _rolling(A, length):
            if length == 0:
                yield 0, 0
                return

            h, power = 0, 1
            for i, x in enumerate(A):
                h = (h + x * power) % MOD
                if i < length - 1:
                    power = (power * P) % MOD
                else:
                    yield h, i - (length - 1)
                    h = (h - A[i - (length - 1)]) * Pinv % MOD

        hashes = collections.defaultdict(list)
        for ha, start in _rolling(A, guess):
            hashes[ha].append(start)
        for ha, start in _rolling(B, guess):
            iarr = hashes.get(ha, [])
            if any(A[i:i + guess] == B[start:start + guess] for i in iarr):
                return True
        return False

    lo, hi = 0, min(len(A), len(B)) + 1
    while lo < hi:
        mi = (lo + hi) / 2
        if check(mi):
            lo = mi + 1
        else:
            hi = mi
    return lo - 1