# coding=utf-8

"""Best Time to Buy and Sell Stock."""

from __future__ import print_function


def _solve(prices):
    min_prices = 0x7fffffff
    ans = 0
    for price in prices:
        min_prices = min(price, min_prices)
        ans = max(price - min_prices, ans)
    return ans


if __name__ == '__main__':
    print (_solve([]))
    print (_solve([1, 13, 9, 17, 2, 3, 15, 18]))
