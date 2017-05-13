# coding=utf-8
"""Find All Numbers Disappeared in an Array."""


def _find_disappeared_numbers(nums):
    n = len(nums)
    answer = []
    for i in xrange(n):
        while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
            origin1 = i
            origin2 = nums[i] - 1
            nums[origin1], nums[origin2] = nums[origin2], nums[origin1]
    for i in xrange(n):
        if i + 1 != nums[i]:
            answer.append(i + 1)
    return answer


def _find_disappeared_numbers2(nums):
    n = len(nums)
    for i in xrange(n):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])
    return [i + 1 for i in xrange(n) if nums[i] > 0]

if __name__ == '__main__':
    print (_find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print (_find_disappeared_numbers2([4, 3, 2, 7, 8, 2, 3, 1]))
