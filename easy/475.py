# coding=utf-8

"""Heaters."""


def _solve(houses, heaters):
    sorted_houses = sorted(houses)
    sorted_heaters = sorted(heaters)
    ans = 0
    i = 0
    total = len(heaters)
    for house in sorted_houses:
        while i + 1 < total:
            # 不能是 < 号
            if abs(sorted_heaters[i + 1] - house) <= abs(sorted_heaters[i] - house):
                i += 1
            else:
                break
        ans = max(abs(house - sorted_heaters[i]), ans)
    return ans


# 还有一种方法是二分，可利用默认库
# 在 Python 中是 bisect.bisect
if __name__ == '__main__':
    print _solve([1, 2], [1, 1, 2])
    print _solve([1, 2, 3], [2])
    print _solve([1, 2, 3, 4], [1, 4])
    print _solve([28, 16, 6, 7, 14, 13, 2, 12, 8, 24], [18, 8, 6])
