# coding=utf-8

"""Non-overlapping Intervals."""


def _solve(intervals):
    res, end = 0, float('-inf')
    for interval in sorted(intervals, key=lambda i: i.end):
        if interval.start < end:
            res += 1
        else:
            end = interval.end
    return res


# 排序 start 显然比排序 end 麻烦许多，但为什么要补充这个代码呢？
# 因为从 Runtime Distribution 来看，貌似排序 start 的速度会比排序 end 快很多
def _solve1(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda i: i.start)
    res, end = 0, intervals[0].end
    for interval in intervals[1:]:
        if interval.start < end:
            res += 1
            if interval.end < end:
                end = interval.end
        else:
            end = interval.end
    return res
