# coding=utf-8
"""UTF-8 Validation.

>>> solve = _solve1
>>> solve([197, 130, 1])
True
>>> solve([235, 140, 4])
False
"""


def _solve(data):
    bins = [format(num, '08b')[-8:] for num in data]
    i, length = 0, len(bins)
    while i < length:
        if bins[i].startswith('0'):
            i += 1
        elif bins[i].startswith('110') and i + 1 < length and bins[i + 1].startswith('10'):
            i += 2
        elif bins[i].startswith('1110') and (i + 2 < length and bins[i + 1].startswith('10')
                                             and bins[i + 2].startswith('10')):
            i += 3
        elif bins[i].startswith('11110') and (i + 3 < length and bins[i + 1].startswith('10')
                                              and bins[i + 2].startswith('10') and bins[i + 3].startswith('10')):
            i += 4
        else:
            return False
    return True


def _solve1(data):
    count = 0
    for num in data:
        if count:
            if num >> 6 != 0b10: return False
            count -= 1
        else:
            if num >> 5 == 0b110: count = 1
            elif num >> 4 == 0b1110: count = 2
            elif num >> 3 == 0b11110: count = 3
            elif num >> 7: return False
    return count == 0
