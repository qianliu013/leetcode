# coding=utf-8
"""Longest Substring with At Least K Repeating Characters.

>>> solve = _solve
>>> solve('aaabb', 3)
3
>>> solve('ababbc', 2)
5
>>> solve("bbaaacbd", 3)
3
"""

import collections


# 此题的一种主要思路就是不断根据无法满足要求的字符切割字符串，这种做法递归求解问题
# a-z 共 26 个字符，那么递归最多 26 层，可以使得每层搜索字符串的总长度总数不超过 n
# 因此时间复杂度为 O(26N) 即 O(N)
# 下面的代码加入一些减枝优化
def _solve(s, k):
    ans = [0]

    def _dfs(cur_s):
        if ans[0] > len(cur_s):
            return
        counter = collections.Counter(cur_s)
        to_del = set([ch for ch, total in counter.items() if total < k])
        if not to_del:
            ans[0] = len(cur_s)
            return
        i, length, new_s = 0, len(cur_s), ''
        while i < length:
            if cur_s[i] not in to_del:
                new_s += cur_s[i]
                if (i + 1 == length or cur_s[i + 1] in to_del):
                    if len(new_s) > ans[0]:
                        _dfs(new_s)
                    new_s = ''
            i += 1

    _dfs(s)
    return ans[0]


# 其实实际上代码无需写那么麻烦，无需任何优化，暴力的分治就能直接过，还很快
# 代码参考自 https://discuss.leetcode.com/topic/57092/4-lines-python
def _solve1(s, k):
    def _dfs(cur):
        for ch in set(cur):
            if cur.count(ch) < k:
                return max(_dfs(nxt) for nxt in cur.split(ch))
        return len(cur)

    return _dfs(s)


# 一种 O(N) 的 非递归思路是考虑最终字符串包含的不重复字符个数
# 只要确定了不重复字符个数，如何求解满足要求的最长字符串较易想到（双指针遍历整个字符串）
# 不重复字符个数范围是 1-26，因此整体复杂度为 O(26N), 即 O(N)
# 代码参考自：https://discuss.leetcode.com/topic/57596/java-strict-o-n-two-pointer-solution/21
# 虽然这种代码实际速度比起上面来说慢很多(36ms -> 390ms)
def _solve2(s, k):
    length = len(s)

    def _longest(target_unique):
        counter, num_unique, num_no_less = collections.Counter(), 0, 0
        begin = end = ans = 0
        while end < length:
            if counter[s[end]] == 0:
                num_unique += 1
            counter[s[end]] += 1
            if counter[s[end]] == k:
                num_no_less += 1
            end += 1

            while num_unique > target_unique:
                if counter[s[begin]] == k:
                    num_no_less -= 1
                counter[s[begin]] -= 1
                if counter[s[begin]] == 0:
                    num_unique -= 1
                begin += 1

            if target_unique == num_unique == num_no_less:
                ans = max(ans, end - begin)
        return ans

    return max(_longest(unique_char) for unique_char in xrange(1, 27))
