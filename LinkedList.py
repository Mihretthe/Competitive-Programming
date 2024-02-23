class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self,head : Node):
        self.head = head

    def traverse(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.val)
            currentNode = currentNode.next

head = Node(1)

second = Node(2)
third = Node(3)

head.next = second
second.next = third

linkedList = LinkedList(head)
linkedList.traverse()


# node = Node(1)
# print(node.val)
# print(node.next)