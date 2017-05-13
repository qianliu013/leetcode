# coding=utf-8

"""Add Strings."""

from __future__ import print_function


def _solve(num1, num2):
    len1 = len(num1)
    len2 = len(num2)
    str1 = num1[::-1]
    str2 = num2[::-1]
    ans = ''
    carry = 0
    for i in xrange(max(len1, len2)):
        digit1 = int(str1[i]) if i < len1 else 0
        digit2 = int(str2[i]) if i < len2 else 0
        sum_i = digit1 + digit2 + carry
        carry = sum_i // 10
        ans = str(sum_i % 10) + ans
    if carry:
        ans = str(carry) + ans
    return ans


if __name__ == '__main__':
    for i in range(0, 100):
        for j in range(0, 100):
            if _solve(str(i), str(j)) != str(i + j):
                print (i, j, _solve(str(i), str(j)))
