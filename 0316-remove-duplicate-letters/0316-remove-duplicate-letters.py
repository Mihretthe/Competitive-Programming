class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letters = "abcdefghijklmnopqrstuvwxyz"
        
        stack = [s[0]]
        for i in range(len(s)):
            if s[i] in stack:
                continue
            else:
                if letters.index(s[i]) > letters.index(stack[-1]):
                    stack.append(s[i])
                else:
                    while stack and letters.index(s[i]) < letters.index(stack[-1]) and stack[-1] in s[i:]:
                        stack.pop()
                    stack.append(s[i])
        
        return "".join(stack)
                    
        