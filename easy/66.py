# coding=utf-8

"""Plus One."""


# 这道题明显的信息量不足
# 如果数组数字大于 9 呢？这导致我刚开始很困扰
# 看 solution，很多题解都没考虑到，而且题目也没说
def _solve(digits):
    num = reduce(lambda sum, index: sum + digits[index] * 10 ** (len(digits) - 1 - index),
                 range(len(digits)), 0)
    return [int(digit) for digit in str(num + 1)]


if __name__ == '__main__':
    print (_solve([15, 9, 8, 10, 12]))
