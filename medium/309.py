# coding=utf-8

"""Best Time to Buy and Sell Stock with Cooldown.

>>> solve = _solve
>>> solve([1, 2, 3, 0, 2, 1])
3
"""


# 此题只要想清楚了多状态间的转移方程，就很容易得到答案；
# 状态的定义多种多样，因此此题的 dp 方式也有很多

# 很慢的、思路非常简单的 n^2 dp
def _solve(prices):
    if not prices:
        return 0
    length = len(prices)
    dp = [0] * length
    for i in xrange(1, length):
        dp[i] = dp[i - 1]
        for j in xrange(i):
            cur = prices[i] - prices[j]
            if j > 2:
                cur += dp[j - 2]
            if cur > dp[i]:
                dp[i] = cur
    return dp[-1]


# 思路和 https://discuss.leetcode.com/topic/31349/7-line-java-only-consider-sell-and-cooldown 基本一致
def _solve1(prices):
    prev, cold_down, sell = 0, 0, 0
    for i, price in enumerate(prices[1:], 1):
        prev = cold_down
        cold_down = max(cold_down, sell)
        sell = max(prev, sell + price - prices[i - 1])
    return max(cold_down, sell)


# buy[i] = max(sell[i-2]-price, buy[i-1])
# sell[i] = max(buy[i-1]+price, sell[i-1])
# 来自：https://discuss.leetcode.com/topic/30421/share-my-thinking-process
def _solve2(prices):
    if len(prices) < 2:
        return 0
    sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
    for price in prices:
        prev_buy = buy
        buy = max(prev_sell - price, prev_buy)
        prev_sell = sell
        sell = max(prev_buy + price, prev_sell)
    return sell


# 另一种常见的、写起来简洁的思路
# https://discuss.leetcode.com/topic/33836/4-line-python-solution-52-ms
def _solve3(prices):
    not_hold, not_hold_cooldown, hold = 0, float('-inf'), float('-inf')
    for price in prices:
        hold, not_hold, not_hold_cooldown = max(hold, not_hold - price), max(not_hold, not_hold_cooldown), hold + price
    return max(not_hold, not_hold_cooldown)
