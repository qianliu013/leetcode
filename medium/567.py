# coding=utf-8

"""Permutation in String.

>>> solve = _solve
>>> solve("ab", "eidbaooo")
True
>>> solve("ab", "eidboaoo")
False
>>> solve("adc", "dcda")
True
"""

import collections


def _solve(s1, s2):
    counter, res, start, need = collections.Counter(s1), {}, 0, len(s1)
    for i, ch in enumerate(s2):
        res[ch] = res.get(ch, 0) + 1
        if res[ch] > counter[ch]:
            while res[ch] > counter[ch]:
                res[s2[start]] -= 1
                start += 1
        else:
            # if all(res.get(ch, 0) == counter[ch] for ch in counter):
            if i - start + 1 == need:
                return True
    return False


# 一种更常见的思路：字符串的长度是固定的，只要每次丢一个进一个判断即可
# 虽然最终的数组比较也可以从 26 次比较优化为更少的比较（只需考虑增、减的字符对结果的影响）
# 但实际可能并不会加快运行速度
def _so1ve1(s1, s2):
    s1_counter, s2_counter = [0] * 26, [0] * 26
    for i in s1:
        s1_counter[ord(i) - ord('a')] += 1
    for i in s2[:len(s1)]:
        s2_counter[ord(i) - ord('a')] += 1
    if s2_counter == s1_counter:
        return True
    for i in range(1, len(s2) - len(s1) + 1):
        s2_counter[ord(s2[i - 1]) - ord('a')] -= 1
        s2_counter[ord(s2[i + len(s1) - 1]) - ord('a')] += 1
        if s1_counter == s2_counter:
            return True
    return False
