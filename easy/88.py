# coding=utf-8

"""Merge Sorted Array."""


def _solve(nums1, m, nums2, n):
    last_index = m + n
    while last_index > 0:
        last_index -= 1
        if m == 0:
            nums1[last_index] = nums2[n - 1]
            n -= 1
        elif n == 0:
            nums1[last_index] = nums1[m - 1]
            m -= 1
        elif m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last_index] = nums1[m - 1]
                m -= 1
            else:
                nums1[last_index] = nums2[n - 1]
                n -= 1


def _solve1(nums1, m, nums2, n):
    last_index = m + n
    while m and n:
        last_index -= 1
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last_index] = nums1[m - 1]
            m -= 1
        else:
            nums1[last_index] = nums2[n - 1]
            n -= 1
    while n:
        last_index -= 1
        nums1[last_index] = nums2[n - 1]
        n -= 1
    return nums1


# 还有一种更为简便的写法，但是 Python 由于没有自增和自减，所以无法实现，代码如下：
# int i = m - 1, j = n - 1, tar = m + n - 1;
# while (j >= 0) nums1[tar--] = i >= 0 && nums1[i] > nums2[j] ? nums1[i--] : nums2[j--];
if __name__ == '__main__':
    print _solve1([1, 2, 3, 0, 0, 0], 3, [1, 2, 3], 3)
    print _solve1([-1, 0, 1, 0, 0, 0], 3, [1, 2, 3], 3)
    print _solve1([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
    print _solve1([1, 5, 9, 0, 0, 0], 3, [2, 6, 8], 3)
