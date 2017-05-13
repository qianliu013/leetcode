# coding=utf-8

"""Generate test data."""

import random


def generate_random_arr(length=7, start=1, end=10):
    """Generate random data.

    Args:

        :type length: int, default value is 7.
        :type start: int, default value is 1.
        :type end: int, default value is 10.
        :rtype: list
    """
    return [random.randint(start, end) for _ in range(length)]
