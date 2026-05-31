class DoublyNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = DoublyNode(-1)
        self.tail = DoublyNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curNode = self.head.next
        while index > 0:
            curNode = curNode.next
            index -= 1
        return curNode.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        newNode = DoublyNode(val)
        curNode = self.head.next
        for _ in range(index):
            curNode = curNode.next
        
        newNode.prev = curNode.prev
        newNode.next = curNode
        newNode.prev.next = newNode
        curNode.prev = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curNode = self.head.next
        for _ in range(index):
            curNode = curNode.next
        curNode.prev.next = curNode.next
        curNode.next.prev = curNode.prev
        self.size -= 1