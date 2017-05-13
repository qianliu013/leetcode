# coding=utf-8

"""Reshape the Matrix."""


def _solve(nums, r, c):
    if not nums or len(nums) == 0:
        return nums
    if nums and len(nums) * len(nums[0]) != r * c:
        return nums
    ans = []
    origin_column = len(nums[0])
    row, column = 0, 0
    for i in xrange(r):
        ans.append([])
        for _ in xrange(c):
            ans[i].append(nums[row][column])
            column += 1
            if column == origin_column:
                column = 0
                row += 1
    return ans


if __name__ == '__main__':
    print _solve([[1, 2], [3, 4]], 1, 4)
    print _solve([[1, 2], [3, 4]], 2, 4)
