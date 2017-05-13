# coding=utf-8

"""Pascal's Triangle."""


def _solve(numRows):
    if numRows < 1:
        return []
    ans = [[1]]
    for row in xrange(1, numRows):
        ans.append([1])
        for col in xrange(1, len(ans[row - 1])):
            ans[row].append(ans[row - 1][col - 1] + ans[row - 1][col])
        ans[row].append(1)
    return ans


def _solve1(numRows):
    res = [[1]]
    for _ in range(1, numRows):
        res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
    return res[:numRows]


if __name__ == '__main__':
    print _solve1(-1)
    print _solve1(1)
    print _solve1(5)
