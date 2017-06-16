from random import randint


class LinkedListNode:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class LinkedList:
    def __init__(self, elements=None):
        head = None
        tail = None
        if elements is not None:
            self.add_elements(elements)

    def __print__(self):
        current = self.head
        linkedList = []
        while (current):
            linkedList.append(str(current.data))
            current = current.nextNode
        print(' --> '.join(linkedList))

    def insert(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.nextNode = LinkedListNode(value)
            self.tail = self.tail.nextNode
        return self.tail

    def insertHead(self, value):
        newNode = LinkedListNode(value)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
        return self.head

    def insertTail(self, value):
        newNode = LinkedListNode(value)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.tail.nextNode = newNode
            newNode = self.tail
        return self.tail

    def __generate__(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.insert(randint(min_value, max_value))
        return self


ll = LinkedList()
ll.__generate__(10, 0, 9)
ll.__print__()
ll.insertTail(99)
ll.__print__()