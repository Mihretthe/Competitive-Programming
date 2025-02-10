class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        next_ = False
        for i in s:
            if i in "0987654321":
                if stack:
                    stack.pop()
                else:
                    next_ = True
            else:
                if next_:
                    next_ = False
                else:
                    stack.append(i)
        
        return "".join(stack)
                