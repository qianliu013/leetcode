# coding=utf-8

"""Maximum Swap.

>>> solve = _solve
>>> solve(2736)
7236
>>> solve(2737)
7732
>>> solve(9973)
9973
"""


def _solve(num):
    num_s = list(str(num))
    max_ch = list(num_s)
    for i in xrange(len(max_ch) - 2, -1, -1):
        max_ch[i] = max(max_ch[i], max_ch[i + 1])
    for i, ch in enumerate(num_s):
        if ch < max_ch[i]:
            j = str(num).rindex(max_ch[i])
            num_s[i], num_s[j] = num_s[j], num_s[i]
            break
    return int(''.join(num_s))


# 较为简洁的写法
def _solve1(num):
    res = map(int, str(num))
    last = {digit: i for i, digit in enumerate(res)}
    for i, digit in enumerate(res):
        for big in xrange(9, digit, -1):
            if last.get(big, None) > i:
                res[i], res[last[big]] = res[last[big]], res[i]
                return int(''.join(map(str, res)))
    return num
