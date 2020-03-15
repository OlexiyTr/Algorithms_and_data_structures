
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

class Node:
    def __init__(self, key: int, value):
        self.key = key
        self.value = value
        self.next = None
        self.valid = True

class HashTable:
    MAX_SIZE = 6000
    def __init__(self):
        self.slots = [None] * HashTable.MAX_SIZE

    @staticmethod
    def hash(key: int) -> int:
        """ Повертає хеш для ключа
        :param key: ключ
        :return: хеш ключа
        """
        hashsum = 0
        N = 31
        M = 5987
        for i in range(len(key)):
            hashsum = hashsum * N + ord(key[i])
        return hashsum % M
        return key % HashTable.MAX_SIZE

    def put(self, key, value):
        """ Додає пару (ключ, значення) до таблиці
        :param key: ключ
        :param value: значення
        """
        hash_key = HashTable.hash(key)  # хеш ключа
        slot = self.slots[hash_key]     # поточний слот таблиці
        while slot != None:
            if slot.key == key:      # якщо ключ у таблиці знайдений
                slot.value.add(value)   # змінюємо значення
                slot.valid = True
                return  # припиняємо роботу методу
            slot = slot.next  # переходмо до наступного елементу у ланцюжку
        slot = Node(key, {value})
        slot.next = self.slots[hash_key]
        self.slots[hash_key] = slot

    def change(self, key, value):
        hash_key = HashTable.hash(key)
        slot = self.slots[hash_key]
        while slot != None:
            if slot.key == key:
                slot.value = value
                slot.valid = True
                return
            slot = slot.next

    def get(self, key):
        """ Повертає значення за ключем
        :param key: ключ
        :return: значення """
        hash_key = HashTable.hash(key)
        slot = self.slots[hash_key]      # поточний слот таблиці
        while slot != None:
            if slot.key == key:    # якщо ключ у таблиці знайдений
                return slot.value  # повертаємо значення, що відповідає ключу
            slot = slot.next       # переходмо до наступного елементу у ланцюжку
        # якщо ключ у таблиці не знайдений
        return None

obj = None

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global obj
    obj = HashTable()



def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global obj
    obj.put(author, title)


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    global obj
    el = obj.get(author)
    if el == None:
        return False
    else:
        if title in el:
            return True
        return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global obj
    el = obj.get(author)
    if title in el:
        el.remove(title)
        obj.change(author, el)


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    global obj
    el = obj.get(author)
    if el == None:
        return []
    return el
