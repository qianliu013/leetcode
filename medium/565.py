# coding=utf-8

"""Array Nesting.

>>> solve = _solve
>>> solve([5, 4, 0, 3, 1, 6, 2])
4
"""


# 可以修改 nums 本身来避免使用额外数组
def _solve(nums):
    ans, visited = 0, [False] * len(nums)
    for i, num in enumerate(nums):
        length = 0
        while not visited[i]:
            visited[i] = True
            length += 1
            i, num = num, nums[num]
        ans = max(ans, length)
    return ans
