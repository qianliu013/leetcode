# coding=utf-8

"""Isomorphic Strings."""


# 注意双向
def _solve(s, t):
    result = {}
    for index, char in enumerate(s):
        if char in result:
            if result[char] != t[index]:
                return False
        else:
            result[char] = t[index]
    result = {}
    t, s = s, t
    for index, char in enumerate(s):
        if char in result:
            if result[char] != t[index]:
                return False
        else:
            result[char] = t[index]
    return True


def _solve1(s, t):
    s_map, t_map = {}, {}
    for index, _ in enumerate(s):
        if s_map.get(s[index], 0) != t_map.get(t[index], 0):
            return False
        s_map[s[index]] = index + 1
        t_map[t[index]] = index + 1
    return True


def _solve2(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))


def _solve3(s, t):
    s_map, t_map = {}, {}
    for s_char, t_char in zip(s, t):
        if s_char not in s_map and t_char not in t_map:
            s_map[s_char], t_map[t_char] = t_char, s_char
        else:
            if s_map.get(s_char, 0) != t_char or t_map.get(t_char, 0) != s_char:
                return False
    return True


if __name__ == '__main__':
    print _solve3('ab', 'aa')
    print _solve3('', '')
    print _solve3('egg', 'add')
    print _solve3('foo', 'bar')
    print _solve3('paper', 'title')
