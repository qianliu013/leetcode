# coding=utf-8

"""Number of Boomerangs."""

from __future__ import print_function


def _solve(points):
    ans = 0
    total = len(points)
    boomerangs = {}
    for i in xrange(total):
        for j in xrange(0, total):
            distance = (points[i][0] - points[j][0]) ** 2 + \
                (points[i][1] - points[j][1]) ** 2
            boomerangs[distance] = boomerangs.get(distance, 0) + 1
        ans += sum([boomerangs[dis] * (boomerangs[dis] - 1)
                    for dis in boomerangs])
        boomerangs.clear()
    return ans


if __name__ == '__main__':
    print (_solve([[0, 0], [1, 0], [2, 0], [3, 0]]))
    print (_solve([[0, 0], [1, 0], [2, 0]]))
    print (_solve([[0, 0], [1, 0]]))
    print (_solve([[0, 0]]))
    print (_solve([]))
