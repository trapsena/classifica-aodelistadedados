class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTableLinked:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        node = self.table[index]
        if not node:
            self.table[index] = Node(key, value)
        else:
            while node.next:
                node = node.next
            node.next = Node(key, value)

    def search(self, key, value):
        index = self._hash(key)
        node = self.table[index]
        while node:
            if node.key == key and node.value == value:
                return True
            node = node.next
        return False

    def delete(self, key, value):
        index = self._hash(key)
        node = self.table[index]
        prev = None
        while node:
            if node.key == key and node.value == value:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                return True
            prev = node
            node = node.next
        return False

    def __str__(self):
        result = []
        for i, node in enumerate(self.table):
            chain = []
            while node:
                chain.append(f"({node.key}: {node.value})")
                node = node.next
            result.append(f"{i}: {' -> '.join(chain)}")
        return "\n".join(result)


# Teste
htable = HashTableLinked(10)
htable.insert("key1", 42)
htable.insert("key2", 50)
htable.insert("key1", 99)
print("Tabela:\n", htable)
print("Busca 42 em key1:", htable.search("key1", 42))
htable.delete("key1", 42)
print("Tabela após remoção:\n", htable)
