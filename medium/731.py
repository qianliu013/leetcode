# coding=utf-8

"""My Calendar II."""


# 一种思路是，计算 overlap，然后使用 MyCalendar I 的方法直接求解
class MyCalendarTwo(object):

    def __init__(self):
        self.__books = []
        self.__overlaps = []

    def book(self, start, end):
        for s, e in self.__overlaps:
            if s < end and start < e:
                return False
        for s, e in self.__books:
            if s < end and start < e:
                self.__overlaps.append((max(s, start), min(end, e)))
        self.__books.append((start, end))
        return True
