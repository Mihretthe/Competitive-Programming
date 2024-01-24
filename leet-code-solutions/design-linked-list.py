class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if self.length == 0:
            return -1
        if index < self.length:
            currentNode = self.head
            for _ in range(index):
                currentNode = currentNode.next
            return currentNode.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.addAtHead(val)
            return 
        currentNode = self.head
        for _ in range(self.length - 1):
            currentNode = currentNode.next
        currentNode.next = Node(val)
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index < self.length:
            currentNode = self.head
            newNode = Node(val)
            for _ in range(index - 1):
                currentNode = currentNode.next
            newNode.next = currentNode.next
            currentNode.next = newNode
            self.length += 1
        
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
                self.length -= 1
            return 
        if index < self.length:
            currentNode = self.head
            for _ in range(index - 1):
                currentNode = currentNode.next
            currentNode.next = currentNode.next.next
            self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)