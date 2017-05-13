# coding=utf-8

"""Best Time to Buy and Sell Stock II."""

from __future__ import print_function


def _solve(prices):
    ans = 0
    for index in range(1, len(prices)):
        if prices[index] > prices[index - 1]:
            ans += prices[index] - prices[index - 1]
    return ans


if __name__ == '__main__':
    print (_solve([5, 10, 8, 1, 7]))
