class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class List:
    def __init__(self):
        self.head = None

    def insertAtPosition(self, value, position):
        node = Node(value)
        if self.head is None:
            self.head = node
            return

        currentNode = self.head
        i = 0
        while currentNode.next is not None and i < position - 1:
            currentNode = currentNode.next

        if (position == 0):
            node.next = currentNode
            self.head = node
            return
        
        node.next = currentNode.next
        currentNode.next = node
        
    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->", end=' ')
            currentNode = currentNode.next
        print("None")


list = List()
list.printLinkedList()
list.insertAtPosition('Guilherme', 0)
list.printLinkedList()
list.insertAtPosition('Gabriel', 1)
list.printLinkedList()
list.insertAtPosition('Fernando', 2)
list.printLinkedList()
list.insertAtPosition('Manoel', 1)
list.printLinkedList()
list.insertAtPosition('Z', 0)
list.printLinkedList()

