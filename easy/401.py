# coding=utf-8

"""Binary Watch."""

from __future__ import print_function


# 可以直接检测 12， 60 个数中的 1 的数量而无需计算置换
def _solve(num):
    def _get_all_possibility(bit, total_bit):
        result = []

        def _deep(bit, total_bit, cur):
            if len(cur) == total_bit:
                if bit == 0:
                    result.append(cur)
            elif bit == 0:
                _deep(bit, total_bit, cur + '0')
            else:
                _deep(bit, total_bit, cur + '0')
                _deep(bit - 1, total_bit, cur + '1')

        _deep(bit, total_bit, '')
        return [int(bin_str, 2) for bin_str in result]

    def _get_all_hour(bit):
        return [str(pro) for pro in _get_all_possibility(bit, 4) if pro < 12]

    def _get_all_minute(bit):
        mins = [('0' if pro < 10 else '') + str(pro)
                for pro in _get_all_possibility(bit, 6) if pro < 60]
        return mins

    ans = []
    for hour_bit in range(0, min(5, num + 1)):
        for hour in _get_all_hour(hour_bit):
            for minute in _get_all_minute(num - hour_bit):
                ans.append(hour + ':' + minute)
    return ans


if __name__ == '__main__':
    print (_solve(1))
