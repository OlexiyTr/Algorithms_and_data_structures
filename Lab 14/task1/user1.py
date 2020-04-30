#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Реалізуйте структуру даних зв'язний (однозв'язний) список з поточним елементом.
"""

class Node:

    def __init__(self, item):
        self.mItem = item
        self.mNext = None


class ListWithCurrent:

    def __init__(self):
        self.mHead = None
        self.mCurr = None

    def empty(self):
        return self.mHead is None

    def reset(self):
        self.mCurr = self.mHead

    def next(self):
        if self.empty() or not self.mCurr.mNext:
            raise StopIteration
        else:
            self.mCurr = self.mCurr.mNext

    def current(self):
        if empty():
            return None
        else:
            return self.mCurr.mItem

    def insert_after(self, item):
        node = Node(item)
        if self.empty():
            self.mHead = self.mCurr = node
        else:
            node.mNext = self.mCurr.mNext
            self.mCurr.mNext = node

    def insert_before(self, item):
        node = Node(item)
        if self.empty():
            self.mHead = node
            self.mCurr = node
        elif self.mHead is self.mCurr:
            node.mNext = self.mCurr
            self.mHead = node
        else:
            prev = self.mHead
            while prev.mNext is not(self.mCurr):
                prev = prev.mNext
            node.mNext = self.mCurr
            prev.mNext = node

    def delete(self):
        if self.empty():
            return
        elif self.mHead is self.mCurr:
            if self.mCurr.mNext:
                self.mHead = self.mCurr = self.mCurr.mNext
            else:
                self.mHead = self.mCurr = None
        else:
            prev = self.mHead
            while prev.mNext is not self.mCurr:
                prev = prev.mNext
            prev.mNext = self.mCurr.mNext
            self.mCurr = self.mCurr.mNext if self.mCurr.mNext else prev

    def damp(self):
        array = []
        node = self.mHead
        while node:
            array.append(node.mItem)
            node = node.mNext
        return array

obj = 0

def init():
    """ Викликається один раз на початку виконання програми. """
    global obj
    obj = ListWithCurrent()


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return obj.empty()


def reset():
    """ Зробити поточний елемент першим.

    Переставляє поточний елемент на перший елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    obj.reset()


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    obj.next()


def current():
    """ Повертає навантаження поточного елементу.

    Гарантується, що функція не буде викликана, якщо список порожній.
    :return: Навантаження поточного елементу
    """
    return obj.current()


def insert_after(item):
    """ Вставляє новий елемент у список після поточного.

    :param item: елемент, що вставляється у список
    """
    obj.insert_after(item)


def insert_before(item):
    """ Вставляє новий елемент у список перед поточним.

    :param item: елемент, що вставляється у список
    """
    obj.insert_before(item)


def delete():
    """ Видаляє поточний елемент.

    Поточним при цьому стає наступний елемент, що йшов у списку після поточного.
    Якщо елемент, що видаляється був у списку останнім, то поточним стає передостанній елемент цього списку.
    """
    obj.delete()



def damp():
    """ Повертає масив у якому записані всі елементи поточного списку.

    :return: список list елементів списку
    """
    return obj.damp()
