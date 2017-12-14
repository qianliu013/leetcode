# coding=utf-8

"""Find Right Interval."""

import bisect


# 下面的代码可以更简化，只要在 sorted_start 后加一个最大值 [(float('inf'), -1)]
# 就可以将 2 3 行变为一行
def _solve(intervals):
    sorted_start = sorted([(interval.start, i) for i, interval in enumerate(intervals)])
    res = [bisect.bisect_left(sorted_start, (interval.end, )) for interval in intervals]
    return [sorted_start[index][1] if index < len(intervals) else -1 for index in res]
