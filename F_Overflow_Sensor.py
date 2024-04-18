stack = []
n = int(input())
for _ in range(n):
    s = input().split()
    if "for" in s:
        s = s[1] + "*("
    elif s[0] == "end":
        s = "0) + " 
    else:
        s = "1 +"
    stack.append(s)

stack = "".join(stack) + "0"
# print(stack)
value = eval(stack)

if value <= (2**32 - 1):
    print(value)
else:
    print("OVERFLOW!!!")

# num = "1+" * 100000
# num += "0"
# print(eval(num))
