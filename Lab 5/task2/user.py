
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

def init():
    pass

max_size = 100000
current_size = 0
keys = [None] * max_size
values = [None] * max_size

def pr():
    global max_size, current_size
    print('coll', current_size/max_size*100)

def hash(key):
    hashsum = 0
    N = 31
    M = 99991

    '''for idx, c in enumerate(key[:6]):
        hashsum += (idx + len(key)) ** ord(c)
        hashsum = hashsum % M'''
    for i in range(len(key)):
        hashsum = hashsum * N + ord(key[i])
    return hashsum % M

def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global current_size, keys, values
    current = hash(author)
    while keys[current] != None:
        if keys[current] == author:
            if title not in values[current]:
                values[current] += [title]
            return
        current += 1

    keys[current] = author
    values[current] = [title]
    current_size += 1


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    global current_size, keys, values
    current = hash(author)
    if keys[current] != None:
        while keys[current] != author:
            if keys[current] == None:
                return False
            current += 1
        else:
            if title in values[current]:
                return True
            else:
                return False
    else:
        return False

def ff(author):
    current = hash(author)
    if keys[current] != None:
        while keys[current] != author:
            if keys[current] == None:
                return False
            current += 1
        else:
            return set(values[current])
    else:
        return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global current_size, keys, values
    current = hash(author)
    while keys[current] != author:
        current += 1
    else:
        if title in values[current]:
            values[current].remove(title)


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    global current_size, keys, values
    current = hash(author)
    if keys[current] != None:
        while keys[current] != author:
            current += 1
        else:
            return set(values[current])
    else:
        return []
