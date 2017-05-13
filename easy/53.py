# coding=utf-8

"""Maximum Subarray."""

from __future__ import print_function


def _solve(nums):
    if not nums:
        return 0
    cur_sum = ans = nums[0]
    for num in nums[1:]:
        cur_sum = max(cur_sum + num, num)
        ans = max(cur_sum, ans)
    return ans


# 分治1
def _solve1(nums):
    def _help(left, right):
        if left == right:
            return nums[left]
        mid = left + (right - left) / 2
        mid_max = nums[mid + 1] + nums[mid]
        tmp_sum = max_sum = 0
        for i in xrange(mid, left, -1):
            tmp_sum += nums[i - 1]
            max_sum = max(max_sum, tmp_sum)
        mid_max += max_sum
        tmp_sum = max_sum = 0
        for i in xrange(mid + 2, right + 1):
            tmp_sum += nums[i]
            max_sum = max(max_sum, tmp_sum)
        mid_max += max_sum
        return max(mid_max, _help(left, mid), _help(mid + 1, right))
    return _help(0, len(nums) - 1)


# 分治2
def _solve2(nums):
    def _help(left, right):
        if left == right:
            arr_sum = left_max_sum = right_max_sum = max_sum = nums[left]
        else:
            mid = left + (right - left) / 2
            left_result = _help(left, mid)
            right_result = _help(mid + 1, right)
            arr_sum = left_result[0] + right_result[0]
            left_max_sum = max(
                left_result[1], left_result[0] + right_result[1])
            right_max_sum = max(
                right_result[2], left_result[2] + right_result[0])
            max_sum = max(left_result[3], right_result[3],
                          left_result[2] + right_result[1])
        return arr_sum, left_max_sum, right_max_sum, max_sum

    return _help(0, len(nums) - 1)[3]


if __name__ == '__main__':
    nums = [8, -19, 5, -4, 20]
    print (_solve(nums), _solve1(nums), _solve2(nums))
    nums = [1, 2, -1, -2, 2, 1, -2, 1]
    print (_solve(nums), _solve1(nums), _solve2(nums))
