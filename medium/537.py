# coding=utf-8

"""Complex Number Multiplication."""

from __future__ import print_function


def _solve(a, b):
    def _parse(complex_num):
        pair = complex_num.split('+')
        return [
            -int(num_str[1:].strip('i')) if num_str.startswith('-') else int(num_str.strip('i'))
            for num_str in pair]
    complex_a, complex_b = _parse(a), _parse(b)
    real = complex_a[0] * complex_b[0] - complex_a[1] * complex_b[1]
    imaginary = complex_a[0] * complex_b[1] + complex_a[1] * complex_b[0]
    return '{0}+{1}i'.format(real, imaginary)


if __name__ == '__main__':
    print (_solve('1+1i', '1+1i'))
    print (_solve('1+-1i', '1+-1i'))
