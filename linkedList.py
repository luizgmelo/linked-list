class LinkedList:
    class Node:
        def __init__(self, element, next = None):
            self.element = element
            self.next = next
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __setitem__(self, position, element):
        if position < 0:
            position = len(self) + position
        
        if position < 0 or position >= len(self):
            raise IndexError('Invalid Position')

        current = self.head
        i = 0
        while i < position:
            current = current.next
            i += 1
        
        current.element = element

    def __str__(self):
        current = self.head
        if self.head is None:
            return '[]'
        string = f'[{current.element}'
        while current.next is not None:
            string = f'{string}, {current.next.element}'
            current = current.next
        return string + ']'
    
    def __len__(self):
        return self.count

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.element
            current = current.next
        
    def __delitem__(self, position):
        if position < 0:
            position = len(self) + position

        if position < 0 or position >= len(self):
            raise IndexError('Invalid Position')
        
        self.count -= 1

        if position == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        
        current = self.head
        i = 0
        while i < position - 1:
            current = current.next
            i += 1
        current.next = current.next.next

    def __getitem__(self, position):
        if isinstance(position, slice):
            step = position.step if position.step is not None else 1

            if step == 0:
                raise ValueError('Step cannot be zero.')

            if step > 0:
                start = position.start if position.start is not None else 0
                stop = position.stop if position.stop is not None else len(self)
            else:
                start = position.start if position.start is not None else len(self) - 1
                stop = position.stop if position.stop is not None else -1

            if start < 0:
                start = len(self) + start

            if stop < 0 and position.stop is not None:
                stop = len(self) + stop

            part = LinkedList()
            scope = range(start,stop,step)
             
            if step > 0:
                i = 0
                it = iter(self)
                while i < stop:
                    element = next(it)
                    if i in scope:
                        part.append(element)
                    i += 1
            else:
                for i in scope:
                    part.append(self[i])
            return part

        if position < 0:
            position = len(self) + position
        if position < 0 or position >= self.count:
            raise IndexError('Invalid Position')
        current = self.head
        i = 0
        while i < position:
            current = current.next
            i += 1
        return current.element

    def __reversed__(self):
        return self[::-1]


    def append(self, element):
        node = self.Node(element)
        self.count += 1
    
        if self.tail is None:
            self.head = node
            self.tail = node
            return
      
        self.tail.next = node
        self.tail = node
    
    def insert(self, position, element):
        node = self.Node(element)
        self.count += 1
        if self.head is None:
            self.head = node
            self.tail = self.head
            return
        if position == 0:
            node.next = self.head
            self.head = node
            return
        current = self.head
        i = 0
        while current.next is not None and i < position - 1:
            current = current.next
            i += 1

        if current == self.tail:
            self.tail = node

        node.next = current.next
        current.next = node

    def copy(self):
        return self[:]
    
    def extend(self, iterable):
        if iterable is None or not hasattr(iterable, '__iter__'):
            raise TypeError('Object is not iterable')
        
        for item in iterable:
            self.append(item)

    def indexOf(self, element):
        i = 0
        current = self.head
        while current is not None:
            if current.element == element:
                return i
            current = current.next
            i += 1
        raise ValueError('x not in list')

    def remove(self, element):
        position = self.indexOf(element)
        del self[position]

    def pop(self, position=None):
        if position is None:
            position = len(self) - 1

        if position < 0:
            position = len(self) + position

        removed = self[position]
        del self[position]

        return removed

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0

    def reverse(self):
        reversed = self[::-1]
        self.clear()
        it = iter(reversed)
        i = 0
        while i < len(reversed):
            self.append(next(it))
            i += 1

my_list = LinkedList()
