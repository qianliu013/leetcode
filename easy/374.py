# coding=utf-8

"""Guess Number Higher or Lower."""


def guess(number):
    if global_number == number:
        return 0
    if global_number < number:
        return -1
    if global_number > number:
        return 1


def _solve(n):
    left, right = 1, n
    while left <= right:
        mid = left + (right - left) / 2
        flag = guess(mid)
        if flag == 0:
            return mid
        if flag == 1:
            left = mid + 1
        if flag == -1:
            right = mid - 1


def _solve1(n):
    left, right = 1, n
    while left <= right:
        mid1, mid2 = left + (right - left) / 3, right - (right - left) / 3
        flag1, flag2 = guess(mid1), guess(mid2)
        if flag1 == 0:
            return mid1
        if flag2 == 0:
            return mid2
        if flag1 == -1:
            right = mid1 - 1
        if flag1 == 1 and flag2 == -1:
            left, right = mid1 + 1, mid2 - 1
        if flag2 == 1:
            left = mid2 + 1


if __name__ == '__main__':
    for global_number in range(1, 11):
        print _solve1(10)
