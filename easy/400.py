# coding=utf-8

"""Nth Digit."""


def _solve(n):
    left, right = 1, 10
    digit = 1
    result = [0]
    while result[-1] < (1 << 32):
        result.append((right - left) * digit + result[-1])
        left, right = left * 10, right * 10
        digit += 1
    for digit, sum_digit in enumerate(result):
        if n <= sum_digit:
            tmp = n - result[digit - 1] - 1
            num = (10 ** (digit - 1)) + tmp / digit
            return int(str(num)[tmp % digit])


# 简化版
def _solve1(n):
    digits, start, count = 1, 1, 9
    n -= 1
    while True:
        total = digits * count
        if n >= total:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10
        else:
            return int(str(start + n / digits)[n % digits])


if __name__ == '__main__':
    ans = ''
    for i in range(1, 1000):
        ans += str(i)
    for index, char in enumerate(ans):
        if int(char) != _solve1(index + 1):
            print index, char
            break
