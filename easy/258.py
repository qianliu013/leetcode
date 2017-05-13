# coding=utf-8

"""Add digits."""


def _add_digits(num):
    # 简单证明：(100a+10b+c)%9=(a+99a+b+9b+c)%9=(a+b+c)%9
    return 0 if num == 0 else 9 if num % 9 == 0 else num % 9

if __name__ == '__main__':
    print (_add_digits(0))
    print (_add_digits(10213))
