# coding=utf-8

"""Maximum XOR of Two Numbers in an Array.

>>> solve = _solve
>>> solve([3, 10, 5, 25, 2, 8])
28
"""


# TODO: summary the discuss
def _solve(nums):
    root, max_xor = [None, None], 0
    bits_arr = [[int(bit) for bit in '{:032b}'.format(num)] for num in nums]

    for bits in bits_arr:
        cur, res = root, ''
        # find max xor
        for bit in bits:
            if cur[1 - bit]:
                cur = cur[1 - bit]
                res += '1'
            elif cur[bit]:
                cur = cur[bit]
                res += '0'
            else:
                res += '0'
        max_xor = max(max_xor, int(res, 2))
        # add current number
        cur = root
        for bit in bits:
            if not cur[bit]:
                cur[bit] = [None, None]
            cur = cur[bit]

    return max_xor


print _solve([3, 10, 5, 25, 2, 8])
