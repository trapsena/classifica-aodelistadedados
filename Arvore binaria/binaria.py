class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class ABB:
    def __init__(self):
        self.root = None

    # Criação (inicializa a ABB)
    def create(self, key):
        self.root = Node(key)

    # Inserção
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    # Impressão (Percurso em Pré-ordem)
    def pre_order(self, node):
        if node:
            print(node.key, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    # Impressão (Percurso em Pós-ordem)
    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.key, end=" ")

    # Impressão (Percurso em Ordem Simétrica)
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.key, end=" ")
            self.in_order(node.right)

    # Busca
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    # Deleção
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Caso 1: Nó folha
            if node.left is None and node.right is None:
                node = None
            # Caso 2: Nó com apenas um filho
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            # Caso 3: Nó com dois filhos
            else:
                min_larger_node = self._find_min(node.right)
                node.key = min_larger_node.key
                node.right = self._delete_recursive(node.right, min_larger_node.key)
        return node

    # Auxiliar para encontrar o menor valor em uma subárvore
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

# Criação da ABB
abb = ABB()

# Inserção de elementos
abb.insert(50)
abb.insert(30)
abb.insert(70)
abb.insert(20)
abb.insert(40)
abb.insert(60)
abb.insert(80)

# Impressão em diferentes ordens
print("Pré-ordem:")
abb.pre_order(abb.root)

print("\nPós-ordem:")
abb.post_order(abb.root)

print("\nOrdem Simétrica (In-ordem):")
abb.in_order(abb.root)

# Busca
key = 70
result = abb.search(key)
print(f"\nBusca por {key}: {'Encontrado' if result else 'Não encontrado'}")

# Deleção de um nó
abb.delete(20)
print("\nApós deleção de 20:")
abb.in_order(abb.root)
