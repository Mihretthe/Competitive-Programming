class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        length = len(s)

        for i in range(length):
            if s[i] == "(":
                stack.append(s[i])
            else:
                num = 0
                while stack:
                    val = stack.pop()
                    if val == "(" and num == 0:
                        stack.append(1)
                        break
                    elif val == "(" and num > 0:
                        stack.append( 2 * num)
                        break
                    else:
                        num += val

        return sum(stack)