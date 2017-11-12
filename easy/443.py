# coding=utf-8

"""String Compression.

>>> solve = _solve
>>> solve(['a', 'a', 'b', 'b', 'c', 'c', 'c'])
6
>>> solve(['a'])
1
>>> solve(['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'])
4
"""


def _solve(chars):
    length = len(chars)
    if length < 2:
        return length
    i, cur_i, total = 1, 0, 1
    while i < length + 1:
        char = chars[i] if i < length else -1
        if char != chars[i - total]:
            chars[cur_i] = chars[i - total]
            cur_i += 1
            if total > 1:
                for char in str(total):
                    chars[cur_i] = char
                    cur_i += 1
                total = 1
        else:
            total += 1
        i += 1
    return cur_i
