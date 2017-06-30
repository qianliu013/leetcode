# coding=utf-8

"""Queue Reconstruction by Height.

>>> solve = _solve3
>>> solve([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
>>> for _ in range(3):
...   data = _generate_test_data()
...   if solve(data[1]) != data[0]:
...      print data
...      break
"""


# O(n ^ 2)
def _solve(people):
    sorted_people = sorted(people, key=lambda person: (person[1], person[0]))
    ans, cur_len = [], 0
    for j, (h, k) in enumerate(sorted_people):
        i = 0
        while i < cur_len:
            if ans[i][0] >= h:
                k -= 1
                if k == -1:
                    break
            i += 1
        ans.insert(i, sorted_people[j])
        cur_len += 1
    return ans


# O(n ^ 2)
def _solve1(people):
    ans = []
    for person in sorted(people, key=lambda x: (-x[0], x[1])):
        ans.insert(person[1], person)
    return ans


# 参考自：https://discuss.leetcode.com/topic/60422/worse-case-o-n-2-and-o-nlogn-in-average-using-binary-tree-travel
# 平均 O(lgn)，最差 O(n^2)
def _solve2(people):
    class _Node(object):

        def __init__(self, person):
            """Init the node with the person and h_count."""
            self.person = person
            self.h_count = 1
            self.left = self.right = None

        def insert(self, person, h_count):
            """Insert the person based h_count."""
            if h_count < self.h_count:
                if self.left:
                    self.left.insert(person, h_count)
                else:
                    self.left = _Node(person)
                self.h_count += 1
            else:
                if self.right:
                    self.right.insert(person, h_count - self.h_count)
                else:
                    self.right = _Node(person)

        def in_order(self, result):
            """In-order traversal append person to result."""
            if self.left:
                self.left.in_order(result)
            result.append(self.person)
            if self.right:
                self.right.in_order(result)

    if people:
        people.sort(key=lambda x: (-x[0], x[1]))
        root = _Node(people[0])
        for person in people[1:]:
            root.insert(person, person[1])
        ans = []
        root.in_order(ans)
        return ans
    else:
        return []


# O(n * lgn)：Binary Index Tree（树状数组）
# 参考自： https://discuss.leetcode.com/topic/60694/o-nlogn-binary-index-tree-c-solution
def _solve3(people):
    length, bit = len(people), [0] * (len(people) + 1)

    def _update(idx, val):
        while idx <= length:
            bit[idx] += val
            idx += idx & -idx

    def _sum(idx):
        i_sum = 0
        while idx > 0:
            i_sum += bit[idx]
            idx -= idx & -idx
        return i_sum

    def _find_kth(kth):
        left, right, mid = 1, length, 0
        while left <= right:
            mid = (left + right) >> 1
            if _sum(mid) >= kth:
                right = mid - 1
            else:
                left = mid + 1
        return left

    ans = [None] * length
    for i in range(length):
        _update(i + 1, 1)
    people.sort()
    prev, prev_poses = -1, []
    for person in people:
        if person[0] != prev:
            for prev_pos in prev_poses:
                _update(prev_pos, -1)
            prev_poses = []

        pos = _find_kth(person[1] + 1)
        ans[pos - 1] = person

        prev = person[0]
        prev_poses.append(pos)
    return ans


# 其他一些解法
# O(sqrt n)： https://discuss.leetcode.com/topic/60550/o-n-sqrt-n-solution
# 对结果数组分块处理


def _generate_test_data(input_arr=None):
    import test_tools
    arr = input_arr or test_tools.generate_random_arr(7, 1, 5)
    origin = []
    for i, num in enumerate(arr):
        origin.append([num, len([x for x in arr[:i] if x >= num])])
    shuffled_arr = origin[:]
    test_tools.shuffle(shuffled_arr)
    return (origin, shuffled_arr)


# print _solve3([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
