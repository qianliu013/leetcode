# coding=utf-8

"""Assign Cookies."""


def _find_content_children(g, s):
    greeds = sorted(g)
    sizes = sorted(s)
    total_children = len(greeds)
    total_cookie = len(sizes)
    cur_child = 0
    cur_cookie = 0
    while cur_cookie < total_cookie:
        if cur_child < total_children:
            if greeds[cur_child] <= sizes[cur_cookie]:
                cur_child += 1
        else:
            break
        cur_cookie += 1
    return cur_child


if __name__ == '__main__':
    print (_find_content_children([1, 2, 3], [1, 1]))
    print (_find_content_children([1, 2], [1, 2, 3]))
