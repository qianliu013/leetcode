# coding=utf-8

"""Binary Number with Alternating Bits."""


# One liner solutions：https://discuss.leetcode.com/topic/106356/oneliners-c-java-ruby-python

def _solve(n):
    bin_s = bin(n)[2:]
    return bin_s == '10' * (len(bin_s) / 2) + ('1' if len(bin_s) & 1 else '')


def _solve1(n):
    bin_s = bin(n)
    return all(bin_s[i] != bin_s[i + 1] for i in xrange(len(bin_s) - 1))
