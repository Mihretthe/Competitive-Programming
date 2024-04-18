s = input()
left = 0
right = 1

length = len(s)
stack = []

for i in range(length):
    if not stack:
        stack.append(s[i])
    else:
        if stack[-1] == s[i]:
            while stack and stack[-1] == s[i]:
                stack.pop()
        else:
            stack.append(s[i])

print("".join(stack))
        

