# coding=utf-8

"""Longest Univalue Path."""


def _solve(root):
    res = [0]

    def _dfs(cur):
        if cur:
            left_path, right_path = _dfs(cur.left), _dfs(cur.right)
            total_path, longest_single_path = 0, 0
            if cur.left and cur.left.val == cur.val:
                total_path += 1 + left_path
                longest_single_path = max(longest_single_path, 1 + left_path)
            if cur.right and cur.right.val == cur.val:
                total_path += 1 + right_path
                longest_single_path = max(longest_single_path, 1 + right_path)
            res[0] = max(res[0], total_path)
            return longest_single_path
        else:
            return 0

    _dfs(root)
    return res[0]
