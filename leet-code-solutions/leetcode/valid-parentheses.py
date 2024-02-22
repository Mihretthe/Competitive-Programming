class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        length = len(s)

        for i in range(length):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if (s[i] == ")" and popped == "(") or  (s[i] == "]" and popped == "[") or  (s[i] == "}" and popped == "{"):
                    continue
                else:
                    return False
        if not stack:
            return True
        
        return False
