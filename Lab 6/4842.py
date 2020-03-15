class HashTable(object):

    def __init__(self):
        self.size = 100
        self.value_array = []
        self.w = []
        self.total_entries = 0
        for i in range(100):
            self.value_array.append(None)

    def add(self, key, value):
        self.add_internal(key, value, self.value_array, self.size)
        self.w.append(key)

    def add_internal(self, key, value, value_array, size, during_resize=False):
        if value_array[self.hash1(key)] == None:
            value_array[self.hash1(key)] = key, value
        else:
            # find the next slot
            added = False
            attempt_count = 1
            while (not added):
                newhash = (self.hash1(key) + attempt_count * self.hash2(key)) % size
                if value_array[newhash] == None:
                    value_array[newhash] = key, value
                    added = True
                else:
                    attempt_count += 1
        if not during_resize:
            self.total_entries += 1
            if self.total_entries > size / 2:
                self.resize()

    def resize(self):
        new_value_array = []
        new_size = 2 * self.size
        for i in range(self.size * 2):
            new_value_array.append(None)
        for i in range(self.size):
            if self.value_array[i] != None:
                self.add_internal(self.value_array[i][0], self.value_array[i][1], new_value_array, new_size, True)
        self.value_array = new_value_array
        self.size = new_size

    def get(self, key):
        got_value = self.value_array[self.hash1(key)]
        if got_value == None:
            return None
        retrieved_key, retrieved_value = got_value
        if retrieved_key != key:
            found = False
            attempt_count = 1
            while (not found and attempt_count < 50):
                newhash = (self.hash1(key) + attempt_count * self.hash2(key)) % self.size
                value_at_hash = self.value_array[newhash]
                if value_at_hash != None:
                    retrieved_key, retrieved_value = value_at_hash
                    if retrieved_key == key:
                        found = True
                    attempt_count += 1
                else:
                    attempt_count += 1
        return str(key.replace(" ", "")) + " - " + str(retrieved_value)

    def hash1(self, key):
        return id(key) % self.size

    def hash2(self, key):
        hashval = (id(key) + 501) % self.size
        return hashval


def test_hashtable():
    ht = HashTable()
    SIZE = int(input())
    for i in range(SIZE):
        english_word, array_of_latin_words = list(map(str, input().split("-")))
        array_of_latin_words = array_of_latin_words.split(",")

        for i in range(len(array_of_latin_words)):
            ht.add(array_of_latin_words[i], english_word)

    print(len(ht.w))
    for y in sorted(ht.w):
        print(ht.get(y))

test_hashtable()
