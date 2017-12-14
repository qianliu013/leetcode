# coding=utf-8

"""Flatten Nested List Iterator."""


# 参考自 https://discuss.leetcode.com/topic/41870/real-iterator-in-python-java-c?page=1
class NestedIterator(object):

    def __init__(self, nestedList):
        self.__stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        cur_list, index = self.__stack[-1]
        self.__stack[-1][1] += 1
        return cur_list[index].getInteger()

    def hasNext(self):
        stack = self.__stack
        while stack:
            cur_list, index = stack[-1]
            if index == len(cur_list):
                stack.pop()
            else:
                if cur_list[index].isInteger():
                    return True
                stack[-1][1] += 1
                stack.append([cur_list[index].getList(), 0])
        return False


class NestedIterator1(object):

    def __init__(self, nestedList):
        self.__stack = nestedList[::-1]

    def next(self):
        return self.__stack.pop().getInteger()

    def hasNext(self):
        while self.__stack:
            top = self.__stack[-1]
            if top.isInteger():
                return True
            self.__stack = self.__stack[:-1] + top.getList()[::-1]
        return False


# 参考自 https://discuss.leetcode.com/topic/45844/python-generators-solution
class NestedIterator2(object):

    def __init__(self, nestedList):
        def _gen(nestedList):
            for item in nestedList:
                if item.isInteger():
                    yield item.getInteger()
                else:
                    for in_item in _gen(item.getList()):
                        yield in_item
        self.__gen = _gen(nestedList)

    def next(self):
        return self.cur

    def hasNext(self):
        try:
            self.cur = next(self.__gen)
            return True
        except StopIteration:
            return False
