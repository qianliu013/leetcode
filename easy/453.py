# coding=utf-8

u"""
Minimum Moves to Equal Array Elements.

这道题我是怎么想出来的呢?
其实是找规律得出的，规律是 n * a[0]  = sum + (n - 1) * x
然后数学推导得出答案
其本质就是每个元素都要加它与最小元素的差值，即：
    Arrays.sort(nums);
    int count = 0;
    for (int i = nums.length - 1; i > 0; i--) {
        count += nums[i] - nums[0];
    }
从 DP 来看答案就非常清楚了，从小到大排序，每次平衡两个数的时候，会给其他数增加这两个数的差值

我刚开始陷入误区一直走不出来是为什么呢？
因为我从一开始一直不知道怎么得到答案，换言之做这种题前必须要有思路，知道得出结论的方法是关键

这个问题的其他理解方式可以参见此题的 editorial solution
"""

from __future__ import print_function


def _min_moves(nums):
    return reduce(lambda x, y: x + y, nums, 0) - len(nums) * min(nums)


if __name__ == '__main__':
    print (_min_moves([2, 9, 15, 32]))
