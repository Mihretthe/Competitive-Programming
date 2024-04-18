s = input()
no_substring = 0
valids = 0

stack = []

ans = set()
for i in s:
    
    if i == "(":
        stack.append(i)
    else:
        
        if stack and stack[-1] == "(":
            valids += 1
            stack.pop()
        else:
            stack.append(i)
            ans.add(valids)        
    
if valids:
    print(valids, len(ans))
else:
    print(0,1)

