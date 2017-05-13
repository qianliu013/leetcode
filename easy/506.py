"""Relative Ranks."""


def _find_relative_ranks(nums):
    sorted_nums = sorted(nums, reverse=True)
    result = {}
    medals = {
        '1': 'Gold Medal',
        '2': 'Silver Medal',
        '3': 'Bronze Medal'
    }
    for rank in xrange(1, len(sorted_nums) + 1):
        result[sorted_nums[rank - 1]] = medals.get(str(rank), str(rank))
    return [result[num] for num in nums]


if __name__ == '__main__':
    print (_find_relative_ranks([5, 1, 3, 2, 4]))
