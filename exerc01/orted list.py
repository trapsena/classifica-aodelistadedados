class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def insertion_sort_linked_list(linked_list):
    if linked_list.head is None or linked_list.head.next is None:
        return

    sorted_list = LinkedList()
    current = linked_list.head

    while current:
        next_node = current.next
        sorted_insert(sorted_list, current)
        current = next_node

    linked_list.head = sorted_list.head

def sorted_insert(sorted_list, new_node):
    if sorted_list.head is None or sorted_list.head.data >= new_node.data:
        new_node.next = sorted_list.head
        sorted_list.head = new_node
    else:
        current = sorted_list.head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

# Função para criar e ordenar a lista encadeada
def test_insertion_sort(test_data, description):
    ll = LinkedList()
    for data in test_data:
        ll.append(data)

    print(f"Teste: {description}")
    print("Lista original:")
    ll.print_list()

    insertion_sort_linked_list(ll)

    print("Lista ordenada:")
    ll.print_list()
    print("\n")

# Testes
test_insertion_sort([1, 2, 3, 4, 5], "Elementos já ordenados")
test_insertion_sort([5, 4, 3, 2, 1], "Elementos ordenados na ordem inversa")
test_insertion_sort([3, 1, 2, 3, 1], "Elementos duplicados")
test_insertion_sort([7, 2, 5, 3, 8, 6, 1, 4], "Elementos aleatórios sem repetição")
