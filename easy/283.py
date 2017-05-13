"""Move Zeros."""


def _move_zeros(nums):
    total_zeros = 0
    length = len(nums)
    for i in xrange(length):
        if nums[i] == 0:
            total_zeros += 1
        else:
            nums[i - total_zeros] = nums[i]
    for i in xrange(length - total_zeros, length):
        nums[i] = 0


if __name__ == '__main__':
    print (_move_zeros([0, 1, 0, 3, 12]))
