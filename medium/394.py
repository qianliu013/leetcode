# coding=utf-8

"""Decode String.

>>> solve = _solve
>>> solve('a2[b2[c2[d]]2[e]]3[f]g')
'abcddcddeebcddcddeefffg'
"""


def _solve(s):
    i, length = 0, len(s)
    str_stack, k_stack = [''], [1]
    while i < length:
        if 'a' <= s[i] <= 'z':
            str_stack[-1] += s[i]
        elif '0' <= s[i] <= '9':
            num = 0
            while '0' <= s[i] <= '9':
                num = num * 10 + ord(s[i]) - ord('0')
                i += 1
            k_stack.append(num)
            str_stack.append('')
        elif s[i] == ']':
            cur = str_stack.pop() * k_stack.pop()
            str_stack[-1] += cur
        i += 1
    return str_stack[0]


# 更加简洁、易懂的写法可以参考
# https://discuss.leetcode.com/topic/57121/share-my-python-stack-simple-solution-easy-to-understand
# 使用正则表达式的 3-Line solution
# https://discuss.leetcode.com/topic/57145/3-lines-python-2-lines-ruby-regular-expression
