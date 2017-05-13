# coding=utf-8

"""Word Pattern."""


def _solve(pattern, str):
    str_arr = str.split(' ')
    if len(pattern) != len(str_arr):
        return False
    return len(set(zip(str_arr, pattern))) == len(set(pattern)) == len(set(str_arr))


if __name__ == '__main__':
    print _solve('', '')
    print _solve('abba', 'dog cat cat dog')
    print _solve('abba', 'dog cat cat fish')
    print _solve('aaaa', 'dog cat cat dog')
    print _solve('abba', 'dog dog dog dog')
