class MinStack:

    def __init__(self):
        self.minimum = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum:
            if val <= self.minimum[-1]:
                self.minimum.append(val)
        else:
            self.minimum.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minimum[-1]:
            self.minimum.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()