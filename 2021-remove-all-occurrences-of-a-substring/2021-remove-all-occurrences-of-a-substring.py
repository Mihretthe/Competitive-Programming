class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        length = len(s)
        p_length = len(part)

        for i in range(length):
            while len(stack) >= p_length and "".join(stack[-p_length:]) == part:
                stack = stack[:-p_length]
            stack.append(s[i])
        if "".join(stack[-p_length:]) == part:
            stack = stack[:-p_length]


        return "".join(stack) 