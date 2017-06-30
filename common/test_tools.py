# coding=utf-8

"""Generate test data."""

import functools
import random
import time


def generate_random_arr(length=7, start=1, end=10):
    """Generate random data.

    :param length: int, default value is 7.
    :param start: int, default value is 1.
    :param end: int, default value is 10.
    :return: list
    """
    return [random.randint(start, end) for _ in range(length)]


def log_execution_time(description=''):
    """Log execution time by using time.time().

    :param description: string, default value is ''.
    :return: function
    """
    def _real_decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print 'Function: {0}; Description: {1} ;time: {2}'.format(
                func.__name__,
                description,
                time.time() - start
            )
            return result
        return _wrapper
    return _real_decorator


def shuffle(arr):
    """Shuffle the input array by random.shuffle.

    :param arr: input
    :return: shuffled arr
    """
    return random.shuffle(arr)
