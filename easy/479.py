# coding=utf-8

"""Largest Palindrome Product."""

# 这道题用 python 做，不用 trick 是不可能过的

import test_tools


# 超时
@test_tools.log_execution_time('solve')
def _solve(n):
    left_num = int('9' * (n - 1) + '0')
    half = n / 2
    if n == 1:
        right_num = 0
    elif n < 6:
        right_num = int('9' + '0' * (n - 1))
    else:
        right_num = int('9' * half + '0' * (n - half))
    single_units = {9: 1, 3: 3, 7: 7}
    ans = 0
    for last1, last2 in single_units.items():
        start = left_num + last1
        for i in xrange(start, right_num, -10):
            end = left_num + last2
            if start * end < ans:
                break
            for j in xrange(end, right_num, -10):
                product = i * j
                if product <= ans:
                    break
                if str(product) == str(product)[::-1]:
                    ans = product
    return ans % 1337


# 超时
@test_tools.log_execution_time('solve1')
def _solve1(n):
    if n == 1:
        return 9
    max_num = (10 ** n) - 1
    for num in xrange(max_num, max_num / 10, -1):
        ans = int(str(num) + str(num)[::-1])
        test = max_num
        while test * test >= ans:
            if ans % test == 0:
                return ans % 1337
            test -= 1
    return 0


print _solve(7)
print _solve(8)
print _solve1(7)
print _solve1(8)

RESULT = [[1, 9, 9],
          [91, 99, 9009],
          [913, 993, 906609],
          [9901, 9999, 99000099],
          [99979, 99681, 9966006699],
          [999999, 999001, 999000000999],
          [9997647, 9998017, 99956644665999],
          [99999999, 99990001, 9999000000009999]]
TRICKS = [arr[2] % 1337 for arr in RESULT]
print TRICKS
