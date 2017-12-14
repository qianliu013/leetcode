# coding=utf-8

"""Best Time to Buy and Sell Stock with Transaction Fee.

>>> solve = _solve
>>> _solve([1, 3, 2, 8, 4, 9], 2)
8
"""


# 此题可以认为是 309 Best Time to Buy and Sell Stock with Cooldown 的简化版本
# 参考那道题的方式，可以直接写出状态方程得到答案
def _solve(prices, fee):
    if len(prices) < 2:
        return 0
    buy, sell = -prices[0], 0
    for price in prices:
        buy, sell = max(buy, sell - price), max(sell, buy + price - fee)
    return sell


# 但是此题不用 dp 的方式也可以解决，毕竟状态比较简单，只需要细致地考虑贪心即可；思路是
# 考虑上升 price 曲线，从最低到最高，只减去一次 fee
# 如果碰到下降曲线，只要考虑处于下降的 price 是否值得去替换即可
# 写法也很多，下面给出一种较为简洁的版本
def _solve1(prices, fee):
    if len(prices) < 2:
        return 0
    res, cur = 0, prices[0] + fee
    for price in prices:
        if price + fee < cur:
            cur = price + fee
        elif price > cur:
            res += price - cur
            cur = price
    return res
