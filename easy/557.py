# coding=utf-8

"""Reverse Words in a String III."""

from __future__ import print_function


def _reverse_words(s):
    return ' '.join([word[::-1] for word in s.split(' ')])


if __name__ == '__main__':
    print (_reverse_words('Let\'s take LeetCode contest'))
