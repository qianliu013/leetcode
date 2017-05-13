# coding=utf-8

"""Climbing Stairs."""

from __future__ import print_function
import math


def _solve(n):
    fibonacci = [1, 1]
    flag = 1
    for _ in range(n):
        fibonacci[flag - 1] = fibonacci[0] + fibonacci[1]
        flag = 1 - flag
    return fibonacci[n & 1]


def _solve_1(n):
    def _quick_power(init, base, power_n, multiply):
        ans = init
        while power_n:
            if power_n & 1:
                ans = multiply(ans, base)
            base = multiply(base, base)
            power_n >>= 1

        return ans

    def _multiply_matrix(matrix_1, matrix_2):
        matrix_row1 = len(matrix_1)
        matrix_col1 = len(matrix_1[0])
        matrix_col2 = len(matrix_2[0])
        ans = [[0 for _ in xrange(matrix_col2)] for _ in xrange(matrix_row1)]
        for i in xrange(matrix_row1):
            for j in xrange(matrix_col2):
                for k in xrange(matrix_col1):
                    ans[i][j] += matrix_1[i][k] * matrix_2[k][j]
        return ans
    matrix_i = [[1, 0], [0, 1]]
    matrix_power_base = [[1, 1], [1, 0]]
    matrix_power = _quick_power(
        matrix_i, matrix_power_base, n - 1, _multiply_matrix)
    return _multiply_matrix(matrix_power, [[1], [1]])[0][0]


def _solve_2(n):
    fibonacci_1 = fibonacci_2 = 1
    for _ in range(n - 1):
        fibonacci_1, fibonacci_2 = fibonacci_1 + fibonacci_2, fibonacci_1
    return fibonacci_1


def _solve_3(n):
    sqrt_5 = math.sqrt(5)
    fibonacci = math.pow((1 + sqrt_5) / 2, n + 1) - \
        math.pow((1 - sqrt_5) / 2, n + 1)
    return int(fibonacci / sqrt_5)


if __name__ == '__main__':
    print (_solve_1(1))
    print (_solve_2(5))
    print (_solve_3(5))
