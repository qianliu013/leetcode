"""Nim Game."""


def _can_win_nim(n):
    return n % 4 != 0

if __name__ == '__main__':
    print (_can_win_nim(4))
