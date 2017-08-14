# coding=utf-8

"""Teemo Attacking.

>>> solve = _solve2
>>> solve([1, 3], 2)
4
>>> solve([1, 2], 2)
3
"""


def _solve(timeSeries, duration):
    start, end, ans = -1, -1, 0
    for time in timeSeries:
        if start == -1:
            start = time
            end = start + duration
        elif time >= end:
            ans += end - start
            start = time
            end = start + duration
        elif time < end:
            end = time + duration
    return ans + end - start


def _solve1(timeSeries, duration):
    ans = duration * len(timeSeries)
    for i in xrange(1, len(timeSeries)):
        ans -= max(0, duration - (timeSeries[i] - timeSeries[i - 1]))
    return ans


def _solve2(timeSeries, duration):
    if timeSeries:
        ans, begin = duration, timeSeries[0]
        for time in timeSeries[1:]:
            ans += (time - begin) if time < begin + duration else duration
            begin = time
        return ans
    else:
        return 0
