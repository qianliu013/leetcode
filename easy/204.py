# coding=utf-8

"""Count Primes."""

from __future__ import print_function
import test_tools


# O(nloglogn) TLE
@test_tools.log_execution_time('origin')
def _solve(n):
    is_prime = [True for _ in range(n)]
    primes = []
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
        for j in range(i + i, n, i):
            is_prime[j] = False
    return len(primes)


# Sieve of Eratosthenes
# 这个答案参考自 https://discuss.leetcode.com/topic/14036/fast-python-solution
# 一些关键优化
# 最重要： if is_prime[]
# 其次： int(n ** 0.5) + 1
# 一些不重要的优化
# 赋值： for -> is_prime[i * i: n: i] = [False] * len(is_prime[i * i: n: i])
# [True for _ in range(n)] -> [True] * n
# range -> xrange
# 另外，对原始的 TLE 的代码的补充说明：
# 虽然存在多次的 primes.append() ，但对性能几乎无影响
# 如果将 primes 换用一个数字统计或者干脆在最后 sum(is_prime)，没有多大差距
@test_tools.log_execution_time('fast')
def _solve1(n):
    if n < 3:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in xrange(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i: n:i] = [False] * len(is_prime[i * i: n: i])
    return sum(is_prime)


# 欧拉筛法 O(n)
@test_tools.log_execution_time('O(n)')
def _solve2(n):
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in xrange(2, n):
        if is_prime[i]:
            primes.append(i)
        for prime in primes:
            if i * prime >= n:
                break
            is_prime[i * prime] = False
            if i % prime == 0:
                break
    return len(primes)


# 初始 n/2 是表示不包括偶数，step 为 2 * i 是为了不计算偶数
# 因为内循环一定是奇数，j = i * i + n * i，n 是偶数，j 才不是偶数
@test_tools.log_execution_time('faster')
def _solve3(n):
    if n < 3:
        return 0
    is_prime = [True] * n
    is_prime[0:2] = [False, False]
    count = n / 2
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if is_prime[i]:
            for j in xrange(i * i, n, 2 * i):
                if is_prime[j]:
                    count -= 1
                    is_prime[j] = False
    return count


# 参考自：https://discuss.leetcode.com/topic/27679/12ms-c-solution
# 是上面的优化版，数组表示 i * 2 + 1 的奇数是否为质数
# 内循环的初始条件即： ((i * 2 + 1) * (i * 2 + 1) - 1) / 2 = (i + 1) * 2 * i
@test_tools.log_execution_time('fastest')
def _solve4(n):
    if n < 3:
        return 0
    count = mid = n / 2
    is_prime = [True] * mid
    for i in xrange(1, int(n ** 0.5) / 2 + 1):
        if is_prime[i]:
            for j in xrange((i + 1) * 2 * i, mid, i * 2 + 1):
                if is_prime[j]:
                    count -= 1
                    is_prime[j] = False
    return count


if __name__ == '__main__':
    # print (_solve(1500000))
    print (_solve1(1500000))
    print (_solve2(1500000))
    print (_solve3(1500000))
    print (_solve4(1500000))
    print (_solve3(10))
    print (_solve4(10))
