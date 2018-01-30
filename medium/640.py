# coding=utf-8

"""Solve the Equation.

>>> solve = _solve
"""


def _solve(equation):
    def _parse(string):
        prev, values = 0, []
        for i, ch in enumerate(string):
            if ch in '+-':
                values.append(string[prev: i])
                prev = i
        values.append(string[prev:])
        x_co, sum_int = 0, 0
        for value in values:
            if value:
                if 'x' in value:
                    if len(value) == 1:
                        x_co += 1
                    elif value[0] in '+-' and len(value) == 2:
                        x_co += int(value[0] + '1')
                    else:
                        x_co += int(value[:-1])
                else:
                    sum_int += int(value)
        return x_co, sum_int

    left, right = map(_parse, equation.split('='))
    if left[0] == right[0] and left[1] == right[1]:
        return 'Infinite solutions'
    if left[0] == right[0] and left[1] != right[1]:
        return 'No solution'
    return 'x=' + str((right[1] - left[1]) / (left[0] - right[0]))


print _solve("x+5-3+x=6+x-2")
print _solve("x=x")
print _solve("2x=x")
print _solve("2x+3x-6x=x+2")
print _solve("x=x+2")
print _solve("-x=-1")
