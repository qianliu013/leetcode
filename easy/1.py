# coding=utf-8

"""Two Sum."""


def _solve(nums, target):
    def _get_ans(values):
        ans = [-1, -1]
        for index, num in enumerate(nums):
            if ans[0] == -1 and num == values[0]:
                ans[0] = index
            if num == values[1]:
                ans[1] = index
        return ans

    ordered_nums = sorted(nums)
    ans = [0, len(ordered_nums) - 1]
    while ans[0] < ans[1]:
        if ordered_nums[ans[0]] + ordered_nums[ans[1]] == target:
            return _get_ans([ordered_nums[index] for index in ans])
        if ordered_nums[ans[0]] + ordered_nums[ans[1]] > target:
            ans[1] -= 1
        if ordered_nums[ans[0]] + ordered_nums[ans[1]] < target:
            ans[0] += 1


def _solve1(nums, target):
    result = {}
    for index, num in enumerate(nums):
        if target - num in result:
            return [result[target - num], index]
        result[num] = index


if __name__ == '__main__':
    print _solve1([3, 2, 4], 6)
    print _solve1([3, 3], 6)
    print _solve1([2, 7, 11, 15], 9)
