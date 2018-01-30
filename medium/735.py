# coding=utf-8

"""Asteroid Collision.

>>> solve = _solve
>>> solve([5, 10, -5])
[5, 10]
>>> solve([8, -8])
[]
>>> solve([10, 2, -5])
[10]
>>> solve([-2, -1, 1, 2])
[-2, -1, 1, 2]
"""


def _solve(asteroids):
    ans = [-1]
    for asteroid in asteroids:
        while asteroid < 0 < ans[-1]:
            if -asteroid < ans[-1] or -asteroid == ans.pop():
                break
        else:
            ans.append(asteroid)
    return ans[1:]
