# coding=utf-8
"""Find the Difference."""


import operator


def _find_the_difference(s, t):
    s_arr = sorted(s)
    t_arr = sorted(t)
    for i in xrange(len(s_arr)):
        if s_arr[i] != t_arr[i]:
            return t_arr[i]
    return t_arr[-1]


def _find_the_difference_2(s, t):
    return chr(reduce(operator.xor, map(ord, s + t)))


if __name__ == '__main__':
    print (_find_the_difference('abcd', 'aecdb'))
    print (_find_the_difference_2('abcd', 'aecdb'))
