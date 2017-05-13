# coding=utf-8

"""Remove Duplicates from Sorted Array."""


def _solve(nums):
    ans, prev = 0, None
    for num in nums:
        if num != prev:
            nums[ans] = num
            ans += 1
            prev = num
    return ans


if __name__ == '__main__':
    print _solve([1, 1, 1, 1, 1])
    print _solve([1, 2, 3, 4])
    print _solve([1, 1, 2])
    print _solve([])
