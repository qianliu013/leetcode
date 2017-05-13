# coding=utf-8

"""Next Greater Element I. """


# Brute force
def _next_greater_element(findNums, nums):
    len2 = len(nums)
    result = {}
    for i in xrange(len2):
        for j in xrange(i + 1, len2):
            if nums[i] < nums[j]:
                result[nums[i]] = nums[j]
                break
    return [result.get(num, -1) for num in findNums]


# hashmap + stack
def _quick_next_greater_element(findNums, nums):
    result = {}
    not_found_stack = []
    for num in nums:
        while len(not_found_stack) > 0 and num > not_found_stack[-1]:
            result[not_found_stack.pop()] = num
        not_found_stack.append(num)
    return [result.get(num, -1) for num in findNums]


if __name__ == '__main__':
    print (_next_greater_element([4, 1, 2], [1, 3, 4, 2]))
    print (_next_greater_element([2, 4], [1, 2, 3, 4]))
    print (_quick_next_greater_element([4, 1, 2], [1, 3, 4, 2]))
    print (_quick_next_greater_element([2, 4], [1, 2, 3, 4]))
