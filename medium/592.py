# coding=utf-8

"""Fraction Addition and Subtraction.

>>> solve = _solve3
>>> solve("-1/2+1/2")
'0/1'
>>> solve("-1/2+1/2+1/3")
'1/3'
>>> solve("1/3-1/2")
'-1/6'
>>> solve("5/3+1/3")
'2/1'
"""

import collections
from fractions import Fraction
import re


def _solve(expression):
    def _gcd(a, b):
        return _gcd(b, a % b) if a % b else b

    denominators = collections.defaultdict(int)
    pattern = re.compile(r'([+-]?\d+)/(\d+)')
    for numerator, denominator in pattern.findall(expression):
        denominators[int(denominator)] += int(numerator)
    all_denominator, all_numerator = 1, 0
    for i in denominators:
        all_denominator *= i
    for key, val in denominators.items():
        all_numerator += all_denominator / key * val
    gcd = _gcd(abs(all_numerator), abs(all_denominator))
    return str(all_numerator / gcd) + '/' + str(all_denominator / gcd)


# 参考自 https://discuss.leetcode.com/topic/90061/small-simple-c-java-python
def _solve1(expression):
    def _gcd(a, b):
        return _gcd(b, a % b) if a % b else b

    all_numerator, all_denominator = 0, 1
    for numerator, denominator in re.findall('([+-]?\d+)/(\d+)', expression):
        numerator, denominator = int(numerator), int(denominator)
        all_numerator = all_numerator * denominator + numerator * all_denominator
        all_denominator *= denominator
        gcd = _gcd(all_numerator, all_denominator)
        all_numerator /= gcd
        all_denominator /= gcd
    return '{0}/{1}'.format(all_numerator, all_denominator)


# 使用 Fraction 两个 python 2line
# 来自 https://discuss.leetcode.com/topic/90019/use-python-fractions-and-regex-module/2
def _solve2(expression):
    ans = sum(map(Fraction, re.findall('.+?/\d+', expression)))
    return str(ans) + "/1" * (ans.denominator == 1)


# 来自 https://discuss.leetcode.com/topic/90251/python-easy-understand-2-line-solution
def _solve3(expression):
    res = sum(map(Fraction, expression.replace('+', ' +').replace('-', ' -').split()))
    return str(res.numerator) + '/' + str(res.denominator)
