# coding=utf-8

"""Intersection of Two Arrays II."""

from __future__ import print_function

# python short code
# list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
# or...
# c1, c2 = Counter(nums1), Counter(nums2)
# return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])


def _solve(nums1, nums2):
    ordered_numbers1 = sorted(nums1)
    ordered_numbers2 = sorted(nums2)
    length1 = len(ordered_numbers1)
    length2 = len(ordered_numbers2)
    index1 = 0
    index2 = 0
    ans = []
    while index1 < length1 and index2 < length2:
        if ordered_numbers1[index1] == ordered_numbers2[index2]:
            ans.append(ordered_numbers1[index1])
            index1 += 1
            index2 += 1
        elif ordered_numbers1[index1] < ordered_numbers2[index2]:
            index1 += 1
        else:
            index2 += 1
    return ans


if __name__ == '__main__':
    print (_solve([1, 2, 2, 1], [2, 2]))
