class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class List:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

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

    def insertAtEnd(self, value):
        node = Node(value)
        if (self.head is None):
            self.head = node
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = node

    def removeAtBegin(self):
        removed = self.head.value
        self.head = self.head.next
        return removed
    
    def removeAtEnd(self):
        currentNode = self.head
        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next
        removed = currentNode.value
        previousNode.next = currentNode.next
        return removed

    def getElementAtPosition(self, position):
        if (self.head is None):
            return None
        
        currentNode = self.head
        i = 0
        while currentNode is not None and i < position:
            currentNode = currentNode.next
            i += 1
        return currentNode.value

    def indexOf(self, value):
        currentNode = self.head
        if (self.head == None):
            return None
        currentNode = self.head
        i = 0
        while currentNode.next is not None and currentNode.value != value:
            currentNode = currentNode.next
            i += 1
        return i

    def size(self):
        if (self.head == None):
            return 0
        currentNode = self.head
        count = 1
        while currentNode.next is not None:
            currentNode = currentNode.next
            count += 1
        return count

    def isEmpty(self):
        return self.head == None

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->", end=' ')
            currentNode = currentNode.next
        print("None")


list = List()
print(list.isEmpty())
list.printLinkedList()
list.insertAtPosition('Guilherme', 0)
print(list.isEmpty())
list.printLinkedList()
list.insertAtPosition('Gabriel', 1)
list.printLinkedList()
list.insertAtPosition('Fernando', 2)
list.printLinkedList()
list.insertAtPosition('Manoel', 1)
list.printLinkedList()
list.insertAtPosition('Z', 0)
list.printLinkedList()
print(list.getElementAtPosition(1))
print(list.getElementAtPosition(0))
list.insertAtEnd('Rafael')
list.insertAtEnd('Leonardo')
list.printLinkedList()
list.insertAtBegin('Cristiano')
list.insertAtBegin('Mario')
list.printLinkedList()
print(list.size())
print(list.indexOf('Guilherme'))
print(list.getElementAtPosition(list.indexOf('Guilherme')))
print(list.isEmpty())
print(list.removeAtBegin())
print(list.removeAtBegin())
list.printLinkedList()
print(list.removeAtEnd())
print(list.removeAtEnd())
list.printLinkedList()