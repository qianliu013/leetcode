# coding=utf-8
"""Super Pow.

>>> solve = _solve
"""

# python 支持大数，因此最简单的可以这样写：`pow(a, int(''.join(map(str, b))), 1337)`

# mod 的性质
# (a+b)%n = ((a%n)+(b%n))%n
# (a-b)%n = ((a%n)-(b%n)+n)%n
# (a*b)%n = (a%n)(b%n)%n

# 计算幂的循环节，因为总共数的数量小于 1337，因此一定存在循环，即最初想法是得到一个取余后的数的数列
# 这个数列应该是由前缀部分（长度设为 p_l）和循环部分(r_l)构成，那么只要计算 (a ^ ((b - p_l) % r_l)) % 1337 即可
# 另外，大数取余可以根据性质 1，3 推出
# 参考 https://discuss.leetcode.com/topic/50504/java-4ms-solution-using-the-remainder-repeat-pattern
# 如果一个数小于 1337，那么就没有前缀部分
def _solve(a, b):
    if a % 1337 == 0:
        return 0
    a %= 1337
    cur, count, nxt = a, 0, [0] * 1337
    while nxt[cur] == 0:
        nxt[cur] = cur * a % 1337
        cur = nxt[cur]
        count += 1

    def _mod(n):
        res = 0
        for digit in b:
            res = (res * 10 + digit) % n
        return res

    mod, ans = _mod(count), a
    while mod > 1:
        mod -= 1
        ans = nxt[ans]
    return ans


# 思想来自：https://discuss.leetcode.com/topic/50489/c-clean-and-short-solution
# a^1234567 % k = (a^1234560 % k) * (a^7 % k) % k = (a^123456 % k)^10 % k * (a^7 % k) % k
# 令 f(a, b) = a^b % k
# f(a,1234567) = f(a, 1234560) * f(a, 7) % k = f(f(a, 123456),10) * f(a,7)%k
def _solve1(a, b):
    result = 1
    for digit in b:
        result = pow(result, 10, 1337) * pow(a, digit, 1337) % 1337
    return result


# 数学解法，可参考
# https://discuss.leetcode.com/topic/50586/math-solusion-based-on-euler-s-theorem-power-called-only-once-c-java-1-line-python
# https://discuss.leetcode.com/topic/50591/fermat-and-chinese-remainder
