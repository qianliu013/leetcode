# coding=utf-8

"""Factorial Trailing Zeroes."""


def _solve(n):
    ans = 0
    while n > 0:
        ans += n / 5
        n /= 5
    return ans


if __name__ == '__main__':
    fact = 1
    test = 0
    for i in range(1, 1000):
        fact *= i
        while fact % 10 == 0:
            test += 1
            fact /= 10
        if _solve(i) != test:
            print i, test, fact
