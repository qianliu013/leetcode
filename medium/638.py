# coding=utf-8

"""Shopping Offers.

>>> solve = _solve
>>> solve([0, 0, 0], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 1, 1])
0
>>> solve([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2])
14
>>> solve([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1])
11
"""


def _solve(price, special, needs):
    length, max_value = len(needs), float('inf')
    res, ans = {(0,) * length: 0}, max_value
    for offer in special:
        for key, value in res.items():
            for i in xrange(1, 7):
                tmp = tuple(a + i * b for a, b in zip(key, offer[:-1]))
                if all(a <= b for a, b in zip(tmp, needs)):
                    res[tmp] = min(res.get(tmp, max_value), value + offer[-1] * i)
                else:
                    break
    for key, value in res.items():
        ans = min(ans, value + sum([(b - a) * price[i] for i, (a, b) in enumerate(zip(key, needs))]))
    return ans


def _solve1(price, special, needs):
    cache, total_range = {}, range(len(needs))

    def _dfs(cur):
        res = sum(cur[i] * price[i] for i in total_range)
        for offer in special:
            tmp = tuple(cur[i] - offer[i] for i in total_range)
            if min(tmp) >= 0:
                res = min(res, cache.get(tmp, _dfs(tmp)) + offer[-1])
        cache[tuple(cur)] = res
        return res
    return _dfs(needs)
