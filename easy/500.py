"""Keyboard Row."""


def _find_words(words):
    row_dict = {}
    row_line = 0
    for keyboard_row in ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']:
        row_line = row_line + 1
        for char in keyboard_row:
            row_dict[char] = row_line
    answer = []
    for word in words:
        row_line = 0
        ok = True
        for char in word.lower():
            if row_line == 0:
                row_line = row_dict[char]
            elif row_line != row_dict[char]:
                ok = False
                break
        if ok:
            answer.append(word)
    return answer


if __name__ == '__main__':
    print (_find_words(["Hello", "Alaska", "Dad", "Peace"]))
