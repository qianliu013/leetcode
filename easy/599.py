# coding=utf-8

"""Minimum Index Sum of Two Lists."""

from __future__ import print_function


def _solve(list1, list2):
    map1 = {string: index for (index, string) in enumerate(list1)}
    map2 = {string: index for (index, string) in enumerate(list2)}
    ans = []
    min_sum = 3000
    for key in map1:
        if key in map2:
            cur_sum = map1[key] + map2[key]
            if cur_sum < min_sum:
                min_sum, ans = cur_sum, [key]
            elif cur_sum == min_sum:
                ans.append(key)
    return ans


def _solve1(list1, list2):
    map1 = {string: index for (index, string) in enumerate(list1)}
    ans = []
    min_sum = 3000
    for index, key in enumerate(list2):
        if key in map1:
            cur_sum = map1[key] + index
            if cur_sum < min_sum:
                min_sum, ans = cur_sum, []
            if cur_sum == min_sum:
                ans.append(key)
    return ans


if __name__ == '__main__':
    print (_solve1(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    ))
    print (_solve1(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"]
    ))
