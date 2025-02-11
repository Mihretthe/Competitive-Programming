class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for i in s:
            stack.append(i)

            print("".join(stack[-1 * len(part):]))
            while len(stack) >= len(part) and "".join(stack[-1 * len(part):]) == part:
                stack = stack[0:len(stack) - len(part)]
            
        
        return "".join(stack)