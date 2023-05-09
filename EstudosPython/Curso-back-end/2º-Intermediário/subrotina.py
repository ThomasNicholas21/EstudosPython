class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, x):
        current = self.head
        position = 1
        while current is not None:
            if current.data == x:
                return position
            current = current.next
            position += 1
        return -1

lista = LinkedList()
lista.head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
lista.head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

posicao = lista.search(2)
if posicao == -1:
    print("Elemento não encontrado na lista")
else:
    print(f"Elemento encontrado na posição {posicao}")
