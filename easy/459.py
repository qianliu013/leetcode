# coding=utf-8

"""Repeated Substring Pattern."""

from __future__ import print_function


def _solve(s):
    length = len(s)
    for sub_len in xrange(1, length):
        if length % sub_len == 0:
            if s == s[0: sub_len] * (length / sub_len):
                return True
    return False


# 这个地方需要一些证明
# https://discuss.leetcode.com/topic/68206/easy-python-solution-with-explaination/5
def _solve1(s):
    return s in (2 * s)[1:-1]


# KMP ：感觉 KMP 可以理解为 DP 的一种
# 从初始开始数 j 个和从某个位置（设为 i）倒数 j 个应该是相等的，然后开始判断下一个
# 如果简单 i + 1 和 j + 1 上的 char 相同，那么j 为 j + 1
# 如果不是，那就把 j 置为前一个最大相等的数值，然后在判断 i + 1 和 j + 1
# 注意的问题就是初始坐标从 0 开始和从 1 开始有略微的不同
# 因为两者的初始值都为 0，即 next[1] = 0, next[0] = 0
# 从 1 开始，1~0 表示不包含字符（闭合），那么更新的时候，应该写 j = next[j]
# 从 0 开始，0~0 表示不包含字符（开放），那么更新的时候，应该写 j = next[j - 1]
# 详细的解释可参考： http://www.matrix67.com/blog/archives/115

# 最后的 return 语句的证明画张图就清楚了

def _solve2(s):
    def _kmp(string):
        next = [0 for _ in string]
        j = 0
        for i in xrange(1, len(string)):
            while j > 0 and string[j] != string[i]:
                j = next[j - 1]
            if string[j] == string[i]:
                j += 1
            next[i] = j
        return next

    kmp_next = _kmp(s)[-1]
    return kmp_next > 0 and len(s) % (len(s) - kmp_next) == 0


if __name__ == '__main__':
    # print (_solve2(''))
    print (_solve2('a'))
    print (_solve2('abab'))
    print (_solve2('aba'))
    print (_solve2("aabaaba"))
    print (_solve2('aaaaaaaaa'))
    print (_solve2('aaab'))
