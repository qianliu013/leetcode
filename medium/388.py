# coding=utf-8

"""Longest Absolute File Path.

>>> solve = _solve
"""


def _solve(input):
    stack, ans = [], 0
    for path in input.splitlines():
        count_tab = len(path) - len(path.lstrip('\t'))
        while count_tab < len(stack):
            stack.pop()
        stack.append(len(path) - count_tab + (stack[-1] if stack else 0))
        if '.' in path:
            ans = max(ans, stack[-1] + len(stack) - 1)
    return ans


# 其实出栈过程并非必要，因为已经知道了下标索引；因此可以直接申请一个很大的数组或者用 map 来解决此问题
# 代码参考自：https://discuss.leetcode.com/topic/55097/simple-python-solution
def _solve1(input):
    maxlen, pathlen = 0, {0: 0}
    for line in input.splitlines():
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1
    return maxlen


assert _solve1('dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext') == 20
assert _solve1('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext') == 32
