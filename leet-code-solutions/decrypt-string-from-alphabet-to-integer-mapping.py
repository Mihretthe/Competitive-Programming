class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha = string.ascii_lowercase
        stack = []
        ans = ''
        for i in s:

            if i == "#":
                a = stack[-2:]
                stack = stack[:-2]
                a = "".join(a)
                stack.append(a)
            else:
                stack.append(i)
        for i in stack:
            ans += alpha[int(i) - 1]

        
        return ans


        




        return ""
