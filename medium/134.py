# coding=utf-8
"""Gas Station.

>>> solve = _solve
>>> solve([2, 4], [3, 4])
-1
>>> solve([5], [4])
0
>>> solve([1, 2], [2, 1])
1
>>> solve([2, 0, 1, 2, 3, 4, 0], [0, 1, 0, 0, 0, 0, 11])
0
"""


# 两种解法核心是一样的，关键在于想清楚为什么可以这样做
def _solve(gas, cost):
    start, end = len(gas) - 1, 0
    cur = gas[start] - cost[start]
    while start > end:
        if cur >= 0 and gas[end] + cur >= cost[end]:
            cur += gas[end] - cost[end]
            end += 1
        else:
            start -= 1
            cur += gas[start] - cost[start]
    return start if cur >= 0 else -1


def _solve1(gas, cost):
    sum_gas = sum_cost = tank = start = 0
    for i, (g, c) in enumerate(zip(gas, cost)):
        sum_cost += c
        sum_gas += g
        tank += g - c
        if tank < 0:
            tank = 0
            start = i + 1
    return start if sum_gas >= sum_cost else -1
