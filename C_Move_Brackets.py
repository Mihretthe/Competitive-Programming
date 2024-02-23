for _ in range(int(input())):
    n = int(input())
    s = input()

    stack = []

    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)

    print(len(stack) // 2)

        