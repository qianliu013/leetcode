# coding=utf-8

"""Different Ways to Add Parentheses.

>>> solve = _solve
>>> len(solve('1+1+1+1'))
5
>>> len(solve('1+1+1+1+1'))
14
"""

import operator


# 38ms
def _solve(input):
    last_i, nums, ops = 0, [], []
    for i, ch in enumerate(input):
        if not ch.isdigit():
            ops.append(ch)
            nums.append(input[last_i:i])
            last_i = i + 1
    nums.append(input[last_i:])
    nums = map(int, nums)
    ops_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    cache = {(i, i): [num] for i, num in enumerate(nums)}

    def _dfs(left, right):
        if (left, right) not in cache:
            cache[(left, right)] = [ops_map[ops[mid]](a, b)
                                    for mid in xrange(left, right)
                                    for a in _dfs(left, mid)
                                    for b in _dfs(mid + 1, right)]
        return cache[(left, right)]
    return _dfs(0, len(nums) - 1)


# 也可以不用任何优化，直接计算
# 代码来自 https://discuss.leetcode.com/topic/19894/1-11-lines-python-9-lines-c
def diffWaysToCompute(self, input):
    return [a + b if c == '+' else a - b if c == '-' else a * b
            for i, c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i + 1:])] or [int(input)]
