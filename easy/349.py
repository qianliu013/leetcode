# coding=utf-8

"""Intersection of Two Arrays."""

from __future__ import print_function


def _intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    print (_intersection([1, 2, 2, 1], [2, 2]))
