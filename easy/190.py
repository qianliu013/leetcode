# coding=utf-8

"""Reverse Bits."""


def _solve(n):
    return sum(1 << (32 - i - 1) for i in range(32) if n & (1 << i))


def _solve1(n):
    ans = 0
    for _ in range(32):
        ans = (ans << 1) | (n & 1)
        n >>= 1
    return ans


def _print32(num):
    string = '{0:032b}'.format(num)
    if len(string) > 32:
        print string
        string = string[8:]
    print string[0:8] + ',' + string[8:16] + ',' + string[16:24] + ',' + string[24:32]


# abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
# 最后 a~h 都是四位的，只需交换两次即可
# 当然顺序反过来也可以
def _solve2(n):
    n = ((n & 0xffff0000) >> 16) | ((n & 0x0000ffff) << 16)
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
    return n


if __name__ == '__main__':
    print _solve(43261596)
    print _solve1(43261596)
    print _solve2(43261596)
