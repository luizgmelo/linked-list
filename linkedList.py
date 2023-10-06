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
        if self.head is None:
            return
        removed = self.head.value
        self.head = self.head.next
        return removed
    
    def removeAtPosition(self, position):
        if self.head is None:
            return
        currentNode = self.head
        onlyOneElement = self.head.next is None
        i = 0
        if (position == 0) | (onlyOneElement):
            removed = self.head.value
            self.head = self.head.next
            return removed
        
        while currentNode.next is not None and i < position:
            previous = currentNode
            currentNode = currentNode.next
            i += 1
        removed = currentNode.value
        previous.next = currentNode.next
        return removed

    def removeAtEnd(self):
        if self.head is None:
            return
        currentNode = self.head
        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next
        removed = currentNode.value
        previousNode.next = currentNode.next
        return removed

    def removeAtElement(self, element):
        if self.head is None:
            return
        currentNode = self.head
        currentNodeElement = currentNode.value
        while currentNode.next is not None and currentNodeElement != element:       
            previousNode = currentNode
            currentNode = currentNode.next 
            currentNodeElement = currentNode.value
        if currentNodeElement == element:
            removed = currentNodeElement
            previousNode.next = currentNode.next
            return removed
        return

    def getElementAtPosition(self, position):
        if (self.head is None):
            return None
        
        currentNode = self.head
        i = 0
        while currentNode is not None and i < position:
            currentNode = currentNode.next
            i += 1
        return currentNode.value

    def getHead(self):
        if self.head is None:
            return
        return self.head.value

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