"""Single Number."""


def _single_num(nums):
    result = {}
    for num in nums:
        result[num] = result.get(num, 0) + 1
    for key, value in result.items():
        if value == 1:
            return key


def _single_num_1(nums):
    ans = 0
    for num in nums:
        ans ^= num
    return ans


if __name__ == '__main__':
    print (_single_num([1, 2, 3, 2, 1]))
    print (_single_num_1([1, 2, 3, 2, 1]))
