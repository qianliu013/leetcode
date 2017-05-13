# coding=utf-8

"""Perfect Number."""


def _solve(num):
    if num < 2:
        return False

    def _gen_prime():
        test = [True for _ in range(10000)]
        for i in range(2, 100):
            if test[i]:
                j = i
                while j * i < 10000:
                    test[j * i] = False
                    j += 1
        return [num for num in range(2, 10000) if test[num]]

    primes = _gen_prime()
    factors = {1: True}
    for prime in primes:
        if prime > num:
            break
        tmp = num
        factor = prime
        while tmp % prime == 0:
            tmp /= prime
            factors[tmp] = True
            factors[factor] = True
            factor *= prime
    return sum(factors.keys()) == num


def _solve1(num):
    if num < 1:
        return False
    result, i = -num, 1
    while i < num ** 0.5:
        if num % i == 0:
            div = num / i
            if div < i:
                return result == num
            result += i + div
        i += 1
    return result == num


# 不正确的 O(sqrt(n))
def _solve2(num):
    if num < 1:
        return False
    result, i = -num, 1
    while i < num:
        if num % i == 0:
            div = num / i
            if div < i:
                return result == num
            result += i + div
        i += 1
    return result == num



def _solve2(num):
    # perfect numbers: 2 ** (p - 1) * (2 ** p - 1)
    # p : prime
    return num in (6, 28, 496, 8128, 33550336)


if __name__ == '__main__':
    for i in range(10000):
        if _solve1(i):
            print i
