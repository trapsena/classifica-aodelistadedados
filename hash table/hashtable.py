class HashTableArray:
    def __init__(self, size):
        self.size = size
        self.table = {i: [] for i in range(self.size)}

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append(value)

    def search(self, key, value):
        index = self._hash(key)
        return value in self.table[index]

    def delete(self, key, value):
        index = self._hash(key)
        if value in self.table[index]:
            self.table[index].remove(value)

    def __str__(self):
        return str(self.table)


# Teste
htable = HashTableArray(10)
htable.insert("key1", 42)
htable.insert("key2", 50)
htable.insert("key1", 99)
print("Tabela:", htable)
print("Busca 42 em key1:", htable.search("key1", 42))
htable.delete("key1", 42)
print("Tabela após remoção:", htable)
