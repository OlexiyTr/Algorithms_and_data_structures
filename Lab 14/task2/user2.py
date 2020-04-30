#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Реалізуйте структуру даних двбічнооднозв'язний список з поточним елементом.
"""

class Node:
    def __init__(self, item):
        self.mItem = item
        self.mNext = None
        self.mPrev = None


class DoublyLinkedList:

    def __init__(self):
        self.mFirst = None
        self.mLast = None
        self.mCurr = None
        self._size = 0

    def empty(self):
        return self.mCurr is None

    def len(self):
        return self._size

    def set_first(self):
        self.mCurr = self.mFirst

    def set_last(self):
        self.mCurr = self.mLast

    def next(self):
        if self.empty() or not(self.mCurr.mNext):
            raise StopIteration
        else:
            self.mCurr = self.mCurr.mNext

    def prev(self):
        if self.empty() or not self.mCurr.mPrev:
            raise StopIteration
        else:
            self.mCurr = self.mCurr.mPrev

    def current(self):
        if self.mCurr:
            return self.mCurr.mItem
        else:
            return None

    def insert_after(self, item):
        node = Node(item)
        if self.empty():
            self.mCurr = self.mFirst = self.mLast = node
        else:
            node.mPrev = self.mCurr
            if self.mCurr.mNext:
                node.mNext = self.mCurr.mNext
                node.mNext.mPrev = node
            else:
                self.mLast = node
            node.mPrev.mNext = node
        self._size += 1

    def insert_before(self, item):
        node = Node(item)
        if self.empty():
            self.mCurr = self.mFirst = self.mLast = node
        else:
            node.mNext = self.mCurr
            if self.mCurr.mPrev:
                node.mPrev = self.mCurr.mPrev
                node.mPrev.mNext = node
            else:
                self.mFirst = node
            node.mNext.mPrev = node
        self._size += 1

    def damp(self):
        array = []
        node = self.mFirst
        while node:
            array.append(node.mItem)
            node = node.mNext
        return array

    def delete(self):
        if self.empty():
            return
        elif self.mFirst is self.mCurr:
            if self.mCurr.mNext:
                self.mFirst = self.mCurr = self.mCurr.mNext
                self.mCurr.mPrev = None
            else:
                self.mFirst = None
                self.mLast = None
                self.mCurr = None
                self._size = 0
                return
        else:
            self.mCurr.mPrev.mNext = self.mCurr.mNext
            if self.mCurr.mNext:
                self.mCurr.mNext.mPrev = self.mCurr.mPrev
                self.mCurr = self.mCurr.mNext
            else:
                self.mLast = self.mCurr = self.mCurr.mPrev
        self._size -= 1

    def swap_prev(self):
        if self.mCurr.mPrev:
            prev = self.mCurr.mPrev
            self.mCurr.mPrev = prev.mPrev
            prev.mNext = self.mCurr.mNext
            if prev.mPrev:
                prev.mPrev.mNext = self.mCurr
            else:
                self.mFirst = self.mCurr
            if self.mCurr.mNext:
                self.mCurr.mNext.mPrev = prev
            else:
                self.mLast = prev
            self.mCurr.mNext = prev
            prev.mPrev = self.mCurr

    def swap_next(self):
        if self.mCurr.mNext:
            self.mCurr.mItem, self.mCurr.mNext.mItem = self.mCurr.mNext.mItem, self.mCurr.mItem
            self.mCurr = self.mCurr.mNext

obj = 0

def init():
    """ Викликається один раз на початку виконання програми. """
    global obj
    obj = DoublyLinkedList()


def empty():
    """ Перевіряє чи список порожній.

    :return: True, якщо список не містить жодного елемента
    """
    return obj.empty()


def set_first():
    """ Зробити поточний елемент першим.

    Переставляє поточний елемент на перший елемент списку.
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    obj.set_first()


def set_last():
    """ Зробити поточними останній елемент списку

    Переставляє поточний елемент на перший елемент списку
    Гарантується, що функція не буде викликана, якщо список порожній.
    """
    obj.set_last()


def next():
    """ Перейти до наступного елемента.

    Робить поточним елементом списку, елемент що йде за поточним.
    Породжує виключення StopIteration, якщо поточний елемент є останнім у списку.
    """
    obj.next()


def prev():
    """ Перейти до попереднього елемента списка.

    робить поточним елементом елемент списку, що йде перед поточним.
    Породжує виключення StopIteration, якщо поточний елемент є першим у списку.
    """
    obj.prev()


def current():
    """ Повертає навантаження поточного елементу.

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


def len():
    """ Повертає кількість елементів у списку

    :return: кількість елементів у списку
    """
    return obj.len()


def swap_prev():
    """ Міняє місцями поточний елемент списку з попереднім
    Гарантується, що виклик функції здійснюється лише, якщо поточний елемент не перший у списку
    Поточний елемент лишається не змінним
    """
    obj.swap_prev()


def swap_next():
    """ Міняє місцями поточний елемент списку з наступним
    Гарантується, що виклик функції здійснюється лише, якщо поточний елемент не останній у списку
    Поточний елемент лишається не змінним
    """
    obj.swap_next()
