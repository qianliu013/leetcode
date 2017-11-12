# coding=utf-8

'''Integer to Roman.

>>> solve = _solve
>>> [solve(num) for num in xrange(1, 20)]
['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX']
'''


def _solve(num):
    roman = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    def _compute(n, basis):
        if n < 4 * basis:
            return roman[basis] * (n / basis)
        elif n < 5 * basis:
            return roman[basis] + roman[5 * basis]
        elif n < 9 * basis:
            return roman[5 * basis] + (roman[basis] * ((n / basis - 5)))
        else:
            return roman[basis] + roman[basis * 10]

    basis, ans = 10 ** (len(str(num)) - 1), ''
    while basis:
        ans += _compute(num, basis)
        num %= basis
        basis /= 10
    return ans


def _solve1(num):
    thous = ['', 'M', 'MM', 'MMM']
    hunds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    return thous[num / 1000] + hunds[(num % 1000) / 100] + tens[(num % 100) / 10] + ones[num % 10]


def _solve2(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    ans = ''
    for i, value in enumerate(values):
        while num >= value:
            num -= value
            ans += strs[i]
    return ans
