class MinStack:
    
    def __init__(self):
        global a
        a=list()
        global b
        b=list()
        global c
        c=list()

    def push(self, val: int) -> None:
        a.append(val)
        b.append(val)
    def pop(self) -> None:
        del a[-1]
        b.pop(-1)
        print(b,"\n",a)
    def top(self) -> int:
        return b[-1]

    def getMin(self) -> int:
        c=sorted(a)
        return c[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()