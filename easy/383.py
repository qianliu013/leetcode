# coding=utf-8

"""Ransom Note."""

from __future__ import print_function


def _can_construct(ransomNote, magazine):
    result = {}
    for letter in magazine:
        result[letter] = result.get(letter, 0) + 1
    for letter in ransomNote:
        if letter in result and result[letter] > 0:
            result[letter] -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    print (_can_construct('baaa', 'aaa'))
    print (_can_construct('aaa', 'baaa'))
