# coding=utf-8

"""Minimum Time Difference."""


def _solve(timePoints):
    res = []
    for time_points in timePoints:
        hour, minute = time_points.split(':')
        res.append(60 * int(hour) + int(minute))
    res.sort()
    res.append(res[0] + 60 * 24)
    ans = 60 * 24
    for i in xrange(len(res) - 1):
        ans = min(ans, res[i + 1] - res[i])
    return ans
