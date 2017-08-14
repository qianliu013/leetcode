# coding=utf-8

"""Friend Circles.

>>> solve = _solve1
>>> solve([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
2
"""


# 一个完整的并查集的实现（可以压缩路径优化）
def _solve(M):
    class UnionUF(object):
        """Represent a union find data type.

        Refer to the Algorithms, 4th.
        """

        def __init__(self, n):
            self.__parent = range(n)
            self.__size = [1] * n
            self.__count = n

        def count(self):
            """Return the number of components."""
            return self.__count

        def find(self, p):
            """Return the component identifier for the component containing site."""
            while p != self.__parent[p]:
                p = self.__parent[p]
            return p

        def connected(self, p, q):
            """Return true if the the two sites are in the same component."""
            return self.find(p) == self.find(q)

        def union(self, p, q):
            """Merge the component containing site p with the the component containing site q."""
            root_p, root_q = self.find(p), self.find(q)
            if root_p == root_q:
                return

            if self.__size[root_p] < self.__size[root_q]:
                self.__parent[root_p] = root_q
                self.__size[root_q] += self.__size[root_p]
            else:
                self.__parent[root_q] = root_p
                self.__size[root_p] += self.__size[root_q]

            self.__count -= 1

    union_uf = UnionUF(len(M))
    for i, row in enumerate(M):
        for j, relationship in enumerate(row[:i]):
            if relationship == 1:
                union_uf.union(i, j)
    return union_uf.count()


# Dfs 实现
def _solve1(M):
    count, length = 0, len(M)
    visited = [False] * length

    def _dfs(index):
        for j in range(length):
            if M[index][j] == 1 and not visited[j]:
                visited[j] = True
                _dfs(j)

    for i in range(length):
        if not visited[i]:
            _dfs(i)
            count += 1
    return count
