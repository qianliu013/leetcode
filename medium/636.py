# coding=utf-8

"""Exclusive Time of Functions.

>>> solve = _solve
>>> solve(2, ["0:start:0", "1:start:2", "1:end:5", "1:start:8", "1:end:11", "0:end:12"])
[5, 8]
>>> solve(3, ["0:start:0", "0:end:0", "1:start:1", "1:end:1", "2:start:2", "2:end:2", "2:start:3", "2:end:3"])
[1, 1, 2]
"""


# 每条 log 都计算一次当前运行函数的执行时间
def _solve(n, logs):
    res, prev, f_ids = [0] * n, 0, []
    for log in logs:
        splits = log.split(':')
        cur_f_id, is_start, timestamp = int(splits[0]), splits[1] == 'start', int(splits[2])
        if is_start:
            if f_ids:
                res[f_ids[-1]] += timestamp - prev
            f_ids.append(cur_f_id)
            prev = timestamp
        else:
            res[f_ids.pop()] += timestamp - prev + 1
            prev = timestamp + 1
    return res


# 只计算结束时候的时间，并在父函数中减去子函数时间
# 参考自 https://discuss.leetcode.com/topic/96085/c-o-n-stack-with-explaination
def _solve1(n, logs):
    res, stack = [0] * n, []
    for log in logs:
        splits = log.split(':')
        item = int(splits[0]), splits[1] == 'start', int(splits[2])
        if item[1]:
            stack.append(item)
        else:
            assert item[0] == stack[-1][0]

            total_time = item[2] - stack[-1][2] + 1
            res[stack.pop()[0]] += total_time

            if stack:
                assert stack[-1][1]
                res[stack[-1][0]] -= total_time
    return res
