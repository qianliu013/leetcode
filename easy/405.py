# coding=utf-8

"""Convert a Number to Hexadecimal."""

from __future__ import print_function


def _solve(num):
    hex_dict = {}
    hex_dict[10] = 'a'
    hex_dict[11] = 'b'
    hex_dict[12] = 'c'
    hex_dict[13] = 'd'
    hex_dict[14] = 'e'
    hex_dict[15] = 'f'
    max_num = 1 << 32

    def _my_hex(num):
        ans = ''
        while num:
            ans = hex_dict.get(num % 16, str(num % 16)) + ans
            num /= 16
        return ans

    if num == 0:
        return '0'
    elif num > 0:
        return _my_hex(num)
    else:
        return _my_hex(max_num + num)


def _to_hex(num):
    return ''.join('0123456789abcdef'[(num >> 4 * i) & 15]
                   for i in range(8))[::-1].lstrip('0') or '0'


if __name__ == '__main__':
    print (_to_hex(0))
    print (_to_hex(-0))
    print (_to_hex(+0))
    print (_to_hex(-1))
    print (_to_hex(26))
