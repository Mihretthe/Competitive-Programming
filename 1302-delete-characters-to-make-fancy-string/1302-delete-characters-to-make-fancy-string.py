class Solution:
    def makeFancyString(self, s: str) -> str:
        
        length = len(s)
        container = [1] * length

        for i in range(1, length):
            if s[i] == s[i - 1]:
                container[i] = container[i - 1] + 1
        
        answer = []

        for i in range(length):
            if container[i] < 3:
                answer.append(s[i])
        
        return "".join(answer)