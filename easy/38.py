# coding=utf-8

"""Count and Say."""


def _solve(n):
    def _read(num_str):
        result, prev, count = '', num_str[0], 1
        for char in num_str[1:]:
            if char == prev:
                count += 1
            else:
                result += str(count) + prev
                count = 1
                prev = char
        return result + (str(count) + prev if count > 0 else '')

    ans = '1'
    while n > 1:
        n -= 1
        ans = _read(ans)
    return ans


if __name__ == '__main__':
    for i in range(11):
        print _solve(i)
