# coding=utf-8

"""Generate test data."""

import functools
import random
import time


def generate_random_arr(length=7, start=1, end=10):
    """Generate random data.

    Args:

        :type length: int, default value is 7.
        :type start: int, default value is 1.
        :type end: int, default value is 10.
        :rtype: list
    """
    return [random.randint(start, end) for _ in range(length)]


def log_execution_time(description=''):
    """Log execution time by using time.time().

    Args:
        :type description: string, default value is ''.
        :rtype: function
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
