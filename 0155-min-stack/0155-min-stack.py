class MinStack:
    
    def __init__(self):
        global b
        b=list()
        global c
        c=list()

    def push(self, val: int) -> None:
        b.append(val)
    def pop(self) -> None:
        b.pop(-1)
    def top(self) -> int:
        return b[-1]

    def getMin(self) -> int:
        c=sorted(b)
        return c[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()