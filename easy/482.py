# coding=utf-8

"""License Key Formatting

>>> solve = _solve
>>> solve("5F3Z-2e-9-w", 4)
'5F3Z-2E9W'
>>> solve("2-4A0r7-4k", 3)
'24-A0R-74K'
>>> solve("-5F3Z-2E9W", 4)
'5F3Z-2E9W'
"""


def _solve(S, K):
    S = S.upper().replace('-', '')
    S = '-' * (K - len(S) % K) + S
    return '-'.join([S[i:i + K] for i in range(0, len(S), K)]).strip('-')
