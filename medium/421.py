# coding=utf-8

"""Maximum XOR of Two Numbers in an Array.

>>> solve = _solve
>>> solve([3, 10, 5, 25, 2, 8])
28
"""


# Trie
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


# 来自 https://discuss.leetcode.com/topic/63299/python-6-lines-bit-by-bit
# 其思路与 discuss 排名第一的方法是一致的
def _solve1(nums):
    ans = 0
    for i in range(32)[::-1]:
        ans <<= 1
        prefixes = {num >> i for num in nums}
        ans += any(ans ^ 1 ^ p in prefixes for p in prefixes)
    return ans


# 还有一类比较容易想到的想法是二分迭代，但是写法较为繁琐
# 1. 从所有数的最高位开始，将数组分为此位是 0 和 1 的两组
# 2. 将这两组根据下一位分为 4 组，即 10、01 和 11、00 两个大组
# 3. 把两个大组分别进行 2 的步骤。需要根据迭代到最后一位或者某个组为空来判断终止。
# 写法如 https://discuss.leetcode.com/topic/64354/c-o-n-solution-explanation-added
