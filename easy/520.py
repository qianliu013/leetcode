# coding=utf-8

"""Detect Capital."""


def _detect_capital_use(word):
    return word.upper() == word or word.lower() == word or \
        (word[0].upper() == word[0] and word[1:].lower() == word[1:])


# 这个可以非常精简
def _detect_capital_use_2(word):
    return word.isupper() or word.islower() or word.istitle()

if __name__ == '__main__':
    print (_detect_capital_use('FlaG'))
