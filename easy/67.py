# coding=utf-8

"""Add Binary."""


def _solve(a, b):
    num_a = [int(digit) for digit in reversed(a)]
    num_b = [int(digit) for digit in reversed(b)]
    len_a, len_b = len(num_a), len(num_b)
    ans = []
    carry = 0
    for i in range(max(len_a, len_b)):
        result = (num_a[i] if i < len_a else 0) + (num_b[i] if i < len_b else 0) + carry
        ans.append(str(result % 2))
        carry = result // 2
    return ('1' if carry else '') + ''.join(ans[::-1])


if __name__ == '__main__':
    print _solve('0', '0')
    print _solve('0', '1')
    print _solve('1', '0')
    print _solve('1', '1')
    print _solve('11', '1')
