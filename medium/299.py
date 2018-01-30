# coding=utf-8
"""Bulls and Cows.

>>> solve = _solve1
>>> solve('1807', '7810')
'1A3B'
>>> solve('1123', '0111')
'1A1B'
"""

import collections
import operator


# 3 line：代码来自：https://discuss.leetcode.com/topic/28457/3-lines-in-python
def _solve(secret, guess):
    bulls = sum(map(operator.eq, secret, guess))
    both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')
    return '{}A{}B'.format(bulls, both - bulls)


# one pass：思路来自：https://discuss.leetcode.com/topic/28463/one-pass-java-solution
def _solve1(secret, guess):
    bulls = cows = 0
    numbers = collections.Counter()
    for i in xrange(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        else:
            if numbers[secret[i]] < 0:
                cows += 1
            if numbers[guess[i]] > 0:
                cows += 1
            numbers[secret[i]] += 1
            numbers[guess[i]] -= 1
    return '{}A{}B'.format(bulls, cows)
