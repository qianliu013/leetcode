"""Construct the Rectangle."""


import math


def _construct_rectangle(area):
    ans = [area, 1]
    for width in xrange(1, int(math.sqrt(area) + 1)):
        if area % width == 0:
            ans = [area / width, width]
    return ans


if __name__ == '__main__':
    print (_construct_rectangle(4))
