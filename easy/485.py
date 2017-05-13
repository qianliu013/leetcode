"""Max Consecutive Ones."""


def _find_max_consecutive_ones(nums):
    result = 0
    ans = 0
    nums.append(0)
    for num in nums:
        if num == 1:
            result = result + 1
        else:
            ans = result if result > ans else ans
            result = 0
    return ans


if __name__ == '__main__':
    print (_find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
