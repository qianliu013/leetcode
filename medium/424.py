# coding=utf-8

"""Longest Repeating Character Replacement.

>>> solve = _solve1
>>> solve('abcde', 1)
2
>>> solve('ababa', 2)
5
>>> solve('abbba', 2)
5
"""

import collections


# 下面的方法是获得 A-Z 每个字母位置，获得每个字母中其能包含的最远的两个 index
def _solve(s, k):
    letter_dict = collections.defaultdict(list)
    for i, letter in enumerate(s):
        letter_dict[letter].append(i)
    # 不初始化为 0 是为了处理所有字母都只有一个情况，如 'ABCDE'
    ans = min(k + 1, len(s))
    for letter, i_list in letter_dict.items():
        start, diff_sum = 0, 0
        for i in xrange(1, len(i_list)):
            diff_sum += i_list[i] - i_list[i - 1] - 1
            while diff_sum > k:
                diff_sum -= i_list[start + 1] - i_list[start] - 1
                start += 1
            ans = max(ans, i_list[i] - i_list[start] + 1 + min(k - diff_sum, i_list[start] + len(s) - i_list[i] - 1))
    return ans


# 参考自 https://discuss.leetcode.com/topic/63494/java-12-lines-o-n-sliding-window-solution-with-explanation
# 其想法是一段字符串 s[start, end] 的 max_count + k 应该小于等于其长度（不是 max_count 的字母可以认为是需要被替换的字母）
# 判断语句是 if 而不是 while 是因为我们已经知道了当前的最长长度，因此就算当前的 max_count + k 小于字符串长度也无所谓
# 因为不会影响到我们最大长度的更新
def _solve1(s, k):
    start, max_count, count = 0, 0, collections.defaultdict(int)
    for end, char in enumerate(s):
        count[char] += 1
        max_count = max(max_count, count[char])
        if max_count + k <= end - start:
            count[s[start]] -= 1
            start += 1
    return len(s) - start
