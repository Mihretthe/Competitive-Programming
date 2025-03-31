class Solution:
    def isValid(self, s: str) -> bool:
        
        # to validate the current is balance parentheses I am going to use stack

        stack = []

        # in the stack I am only gonna store the openings

        length = len(s)

        for i in range(length):
            if s[i] in "[{(":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if (s[i] == ")" and stack[-1] == "(") or (s[i] == "]" and stack[-1] == "[") or (s[i] == "}" and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False

        #  return stack is empty else there are openings that are not closed

        return not stack