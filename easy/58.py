# coding=utf-8

"""Length of Last Word."""


# 要注意的是空字符串的问题
# The behavior of split on an empty string depends on the value of sep.
# If sep is not specified, or specified as None, the result will be an empty list.
# If sep is specified as any string, the result will be a list containing one element which is an empty string.
def _solve(s):
    return len(s.rstrip(' ').split(' ')[-1])


if __name__ == '__main__':
    print _solve('')
