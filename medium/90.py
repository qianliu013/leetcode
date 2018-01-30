# coding=utf-8

"""Subsets II.

>>> solve = _solve
>>> len(solve([1, 2, 2, 2, 3, 4, 3, 5, 3]))
128
"""


# Iterative1
def _solve(nums):
    res = [[]]
    nums.sort()
    for i, num in enumerate(nums):
        if i == 0 or nums[i - 1] != num:
            res.extend([a_list + [num] for a_list in res])
            equal_num = 1
        else:
            for j in xrange(len(res) - 1, 0, -1):
                if equal_num <= len(res[j]) and res[j][-equal_num] == num:
                    res.append(res[j] + [num])
                else:
                    break
            equal_num += 1
    return res


# Recursive (Backtracking)
def _solve1(nums):
    nums.sort()
    res, length = [], len(nums)

    def _dfs(cur, start):
        res.append(cur)
        for i in xrange(start, length):
            if i == start or nums[i] != nums[i - 1]:
                _dfs(cur + [nums[i]], i + 1)
    _dfs([], 0)
    return res


# 其实在迭代中，重要的就是知道从从哪儿开始迭代，我代码中 equal num 就是用于判断此的
# 但仔细一想，其实从上一次的结果可得知迭代起点，由此得到更为优雅的写法
def _solve2(nums):
    res = [[]]
    nums.sort()
    for i in xrange(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            length = len(res)
        for j in range(len(res) - length, len(res)):
            res.append(res[j] + [nums[i]])
    return res


# 不过除此之外，也可以直接集体处理相同数的部分，而不是分别处理，也是一种思路
# 即，任意一段 k 个相同的数，可以认为是每个之前得到的结果加 1 到 k 个此新的相同的数
# 逻辑简单，写起来可能代码比起上述稍微不够简洁，具体可参考
# https://discuss.leetcode.com/topic/4661/c-solution-and-explanation
