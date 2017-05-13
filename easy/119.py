# coding=utf-8

"""Pascal's Triangle II."""


def _solve(rowIndex):
    if rowIndex < 1:
        return [1]
    ans = [1 for _ in range(rowIndex + 1)]
    for row in xrange(1, rowIndex + 1):
        prev = 1
        for col in xrange(1, row):
            cur = ans[col]
            ans[col] = prev + cur
            prev = cur
    return ans


def _solve1(rowIndex):
    if rowIndex < 1:
        return [1]
    ans = [1 for _ in range(rowIndex + 1)]
    for row in xrange(1, rowIndex + 1):
        for col in xrange(row - 1, 0, -1):
            ans[col] += ans[col - 1]
    return ans


def _solve2(rowIndex):
    if rowIndex < 1:
        return [1]
    ans = [1 for _ in range(rowIndex + 1)]
    combination = 1
    small = 1
    for lager in xrange(rowIndex, rowIndex / 2, -1):
        combination *= lager
        combination /= small
        small += 1
        ans[lager - 1] = ans[small - 1] = combination
    return ans


if __name__ == '__main__':
    for index in range(0, 7):
        print _solve2(index)
