# coding=utf-8

u"""
Sum of Two Integers.

python 位运算不溢出
"""


def _get_num(a, b):
    MASK = 0xfffffff
    MAX = 0x7ffffff

    a &= MASK
    b &= MASK
    while b != 0:
        a, b = a ^ b, ((a & b) << 1) & MASK

    # 任何一个数与 MASK 异或其实都相当于取反，然后再取反，因此不变
    # 重点是把一个正数映射到了 32 位的符号数，这应该就是 ^ 起的作用
    # 作者的解释是
    # In sum, you can consider a^mask gets a's 32-bit positive complement
    #  with more 32-bit 0's on left,and ~ gets the common Python complement.
    return a if a <= MAX else ~(a ^ MASK)


if __name__ == '__main__':
    print (_get_num(-300, 100))
    print (_get_num(-30, 100))
    print (_get_num(0, 0))
    print (_get_num(30, 100))
