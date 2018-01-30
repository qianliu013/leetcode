# coding=utf-8

"""Knight Probability in Chessboard.

>>> solve = _solve
>>> solve(3, 2, 0, 0)
0.0625
"""

import collections


def _solve(N, K, r, c):
    chessboard = collections.defaultdict(float)
    chessboard[(r, c)] = 1.0
    dirs, probability = [(1, 2), (2, 1), (-1, 2), (1, -2), (-2, 1), (2, -1), (-1, -2), (-2, -1)], 1.0 / 8
    for _ in xrange(K):
        transition = collections.defaultdict(float)
        for (i, j), in_board in chessboard.items():
            for i_inc, j_inc in dirs:
                if 0 <= i + i_inc < N and 0 <= j + j_inc < N:
                    transition[(i + i_inc, j + j_inc)] += in_board * probability
        chessboard = transition
    return sum(chessboard.values())


# 另一种 dp 思路；从某个位置经过 K 步调到棋盘任一位置，可以反过来想，任意位置经过 K 步最终调到某一位置
# 代码参考自： https://discuss.leetcode.com/topic/105571/my-accepted-dp-solution
def _solve1(N, K, r, c):
    dp = [[1] * N for _ in xrange(N)]
    dirs = [(1, 2), (2, 1), (-1, 2), (1, -2), (-2, 1), (2, -1), (-1, -2), (-2, -1)]
    for _ in xrange(K):
        transition = [[0] * N for _ in xrange(N)]
        for i in xrange(N):
            for j in xrange(N):
                for i_inc, j_inc in dirs:
                    if 0 <= i + i_inc < N and 0 <= j + j_inc < N:
                        transition[i + i_inc][j + j_inc] += dp[i][j]
        dp = transition
    # print dp
    return dp[r][c] * 1.0 / (8 ** K)


# 一种很短代码的 dp 写法可见： https://discuss.leetcode.com/topic/105635/python

# 另外，正如此题的 solution 所示（https://leetcode.com/articles/knight-probability-in-chessboard/）
# 可以使用状态转移的矩阵乘法，即计算矩阵的每个点(n ^ 2)到下一个点的概率，然后得到 (n ^ 2) ^ 2 的概率矩阵
# 然后，利用快速幂算法，得到最后的概率
# 虽然，有点杀鸡焉用牛刀的味道，因为此题的数据范围的确不适合用这种思路，事实证明这种方法也是很慢的
# 但是可以拓宽思路，无论是矩阵的思想，还是对称减少状态（n^2 -> (n^2)/8），都很值得鉴戒
# 具体代码请看原 solution
