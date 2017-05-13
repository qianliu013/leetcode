"""Hamming Distance."""


def _hammingDistance(x, y):

    xor_result = x ^ y
    ans = 0
    while xor_result > 0:
        ans = ans + (1 if xor_result % 2 == 1 else 0)
        xor_result /= 2
    return ans


if __name__ == '__main__':
    print (_hammingDistance(1, 4))
