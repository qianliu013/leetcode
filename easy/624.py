# coding=utf-8

"""Maximum Distance in Arrays."""

from __future__ import print_function


def _solve(arrays):
    two_max_index = [0, 1] if arrays[0][-1] > arrays[1][-1] else [1, 0]
    two_min_index = [0, 1] if arrays[0][0] < arrays[1][0] else [1, 0]

    for index, arr in enumerate(arrays):
        if index < 2:
            continue
        if arr[0] < arrays[two_min_index[0]][0]:
            two_min_index[1] = two_min_index[0]
            two_min_index[0] = index
        elif arr[0] < arrays[two_min_index[1]][0]:
            two_min_index[1] = index

        if arr[-1] >= arrays[two_max_index[0]][-1]:
            two_max_index[1] = two_max_index[0]
            two_max_index[0] = index
        elif arr[-1] >= arrays[two_max_index[1]][-1]:
            two_max_index[1] = index

    if two_max_index[0] != two_min_index[0]:
        return arrays[two_max_index[0]][-1] - arrays[two_min_index[0]][0]
    else:
        return max(arrays[two_max_index[0]][-1] - arrays[two_min_index[1]][0],
                   arrays[two_max_index[1]][-1] - arrays[two_min_index[0]][0])


def _solve1(arrays):
    ans, cur_min, cur_max = 0, arrays[0][0], arrays[0][-1]
    for arr in arrays[1:]:
        ans = max(ans, abs(cur_max - arr[0]), abs(arr[-1] - cur_min))
        cur_min = min(cur_min, arr[0])
        cur_max = max(cur_max, arr[-1])
    return ans


if __name__ == '__main__':
    print (_solve1([[1], [2]]))
    print (_solve1([[1, 2, 3], [4, 5], [1, 2, 3]]))
    print (_solve1([[1, 4], [0, 5]]))
    print (_solve1([[1, 4], [0, 5], [0, 3]]))
    print (_solve1([[-1, 1], [-3, 1, 4], [-2, -1, 0, 2]]))
    print (_solve1([[1, 5], [3, 4]]))
    print (_solve1([[-5, -2, 0, 1, 1, 2], [-7, -6, -3], [-8, -7, -4, -4, 0, 2, 3, 4]]))
