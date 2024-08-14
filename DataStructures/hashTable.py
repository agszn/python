class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def delete(self, key):
        if key in self.table:
            del self.table[key]

    def search(self, key):
        return self.table.get(key, None)

# Example usage
ht = HashTable()
ht.insert("key1", "value1")
print(ht.search("key1"))  # value1
ht.delete("key1")
print(ht.search("key1"))  # None
