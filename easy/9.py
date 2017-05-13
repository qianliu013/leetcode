# coding=utf-8

"""Palindrome Number."""


# 如果直接翻转可能会溢出 int
# 当然 Python 不会溢出
def _solve(x):
    if x == 0:
        return True
    if x < 0 or x % 10 == 0:
        return False
    left, right = x, 0
    while left > right:
        right = right * 10 + left % 10
        left /= 10
    return left == right or left == right / 10


if __name__ == '__main__':
    for i in range(1000):
        if _solve(i) != (i == int(str(i)[::-1])):
            print i
