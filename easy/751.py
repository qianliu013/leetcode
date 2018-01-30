# coding=utf-8

"""IP to CIDR.

>>> solve = _solve
>>> solve('255.0.0.7', 10)
['255.0.0.7/32', '255.0.0.8/29', '255.0.0.16/32']
"""


def _solve(ip, n):
    def _int_to_ip(int_ip):
        return '.'.join(map(str, [int_ip >> 24 & 255, int_ip >> 16 & 255, int_ip >> 8 & 255, int_ip & 255]))

    ip_start = sum([int(part) * (256 ** (3 - i)) for i, part in enumerate(ip.split('.'))])
    res = []
    while True:
        last1 = (ip_start & -ip_start).bit_length() - 1
        count = 1 << last1
        if n < count:
            break
        res.append((ip_start, 32 - last1))
        ip_start += count
        n -= count
    while n != 0:
        half = 1 << (last1 - 1)
        if n >= half:
            last1 -= 1
            res.append((ip_start, 32 - last1))
            n -= half
            ip_start += half
        else:
            last1 -= 1
    return [_int_to_ip(int_ip) + '/' + str(mask) for int_ip, mask in res]


# 上面代码的优化版本
# 参考自此题的 solution https://leetcode.com/articles/ip-to-cidr/
def _solve1(ip, n):
    def _int_to_ip(int_ip):
        return '.'.join(map(str, [int_ip >> 24 & 255, int_ip >> 16 & 255, int_ip >> 8 & 255, int_ip & 255]))

    ip_start = sum([int(part) * (256 ** (3 - i)) for i, part in enumerate(ip.split('.'))])
    res = []
    while n:
        mask = max(33 - (ip_start & -ip_start).bit_length(), 33 - n.bit_length())
        res.append(_int_to_ip(ip_start) + '/' + str(mask))
        ip_start += 1 << (32 - mask)
        n -= 1 << (32 - mask)
    return res
