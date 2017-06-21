# coding=utf-8

"""Subtree of Another Tree."""

from TreeNode import TreeNode


def _solve(s, t):
    def _help1(head1, head2):
        if _help2(head1, head2):
            return True
        else:
            if head1:
                return _help1(head1.left, head2) or _help1(head1.right, head2)
            else:
                return False

    def _help2(head1, head2):
        if not head1 and not head2:
            return True
        if head1 and head2 and head1.val == head2.val:
            return _help2(head1.left, head2.left) and _help2(head1.right, head2.right)
        return False

    if not t and not s:
        return True
    if not t and s:
        return False
    return _help1(s, t)


def _solve1(s, t):
    def _pre_order(cur):
        return '$' if cur is None else ('#' + str(cur.val) +
                                        _pre_order(cur.left) + _pre_order(cur.right))
    return _pre_order(t) in _pre_order(s)


def _solve2(s, t):
    def _in_order(cur, is_left):
        return ('l' if is_left else 'r') if cur is None else (
            _in_order(cur.left, True) + str(cur.val) + _in_order(cur.right, False))
    return _in_order(t, True) in _in_order(s, True)


def _solve3(s, t):
    def _post_order(cur):
        return '$' if cur is None else (_post_order(cur.left) + _post_order(cur.right)
                                        + str(cur.val) + '^')
    return _post_order(t) in _post_order(s)


if __name__ == '__main__':
    print _solve2(TreeNode.de_serialize('[3,4,5,1,2,null,null,0]'), TreeNode.de_serialize('[4,1,2]'))
    print _solve(None, None)
    print _solve(TreeNode.de_serialize('[3,4,5,1,2]'), None)
    print _solve(TreeNode.de_serialize('[3,4,5,1,2]'), TreeNode.de_serialize('[4,1,2]'))
    print _solve(TreeNode.de_serialize('[3,4,5,1,2,null,null,null,null,0]'),
                 TreeNode.de_serialize('[4,1,2]'))
    print _solve(
        TreeNode.de_serialize(
            '[1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]'),
        TreeNode.de_serialize('[1,null,1,null,1,null,1,null,1,null,1,2]'))

    print '---'
    print _solve2(None, None)
    print _solve2(TreeNode.de_serialize('[3,4,5,1,2]'), None)
    print _solve2(TreeNode.de_serialize('[3,4,5,1,2]'), TreeNode.de_serialize('[4,1,2]'))
    print _solve2(TreeNode.de_serialize('[3,4,5,1,2,null,null,null,null,0]'),
                  TreeNode.de_serialize('[4,1,2]'))
    print _solve2(
        TreeNode.de_serialize(
            '[1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]'),
        TreeNode.de_serialize('[1,null,1,null,1,null,1,null,1,null,1,2]'))
