# coding=utf-8

"""Find All Anagrams in a String."""


def _solve(s, p):
    result = {}
    ans = []
    for char in p:
        result[char] = result.get(char, 0) + 1
    p_len = count = len(p)
    # 只考虑 result[char] 为正数
    # 因为 result[char] 为负数，在 result 有其他的 value 来代表其值
    for i, char in enumerate(s):
        result[char] = result.get(char, 0) - 1
        count -= 1 if result[char] >= 0 else 0
        if count == 0:
            ans.append(i - p_len + 1)
        if i >= p_len - 1:
            result[s[i - p_len + 1]] += 1
            count += 1 if result[s[i - p_len + 1]] > 0 else 0
    return ans


if __name__ == '__main__':
    print _solve('cbaebabacd', 'abc')
    print _solve('abab', 'ab')
