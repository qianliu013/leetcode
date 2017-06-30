# coding=utf-8

"""Find Duplicate File in System.

>>> solve = _solve
>>> ans = [['root/a/1.txt', 'root/c/3.txt'], ['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt']]
>>> solve(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]) == ans
True
"""

import collections


def _solve(paths):
    path_arr, content_map = [], collections.defaultdict(list)
    for path in paths:
        arr = path.split(' ')
        path_arr.append(arr[0])
        for file_content in arr[1:]:
            name = file_content.split('(')[0]
            content = file_content.split('(')[1][:-1]
            content_map[content].append((len(path_arr) - 1, name))
    return [[path_arr[index] + '/' + file_name for (index, file_name) in files]
            for files in content_map.values() if len(files) > 1]
