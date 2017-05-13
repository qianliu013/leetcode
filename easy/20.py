# coding=utf-8

"""Valid Parentheses."""


def _solve(s):
    stack = []
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for char in s:
        if char in match:
            if len(stack) > 0:
                if stack.pop() != match[char]:
                    return False
            else:
                return False
        else:
            stack.append(char)
    return len(stack) == 0


if __name__ == '__main__':
    print _solve('()')
    print _solve('()[]{}')
    print _solve('(([][{}{[(())]}]((){}){})[[[]]])')
    print _solve('')
    print _solve('[')
    print _solve('(]')
    print _solve('([)]')
    print _solve('[[]]()()([]))')
