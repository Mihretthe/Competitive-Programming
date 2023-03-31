class MyLinkedList:

    def __init__(self):
        global val
        val=-1
        global a
        a=[val]

    def get(self, index: int) -> int:
        if index<len(a):
            return a[index]
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        a.insert(0,val)

    def addAtTail(self, val: int) -> None:
        a.insert(-1,val)

    def addAtIndex(self, index: int, val: int) -> None:
        a.insert(index,val)

    def deleteAtIndex(self, index: int) -> None:
        if index<len(a)-1:
            a.pop(index)
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)