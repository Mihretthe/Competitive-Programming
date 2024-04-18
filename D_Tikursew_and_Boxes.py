n = int(input())
operations = 0
to_be_removed = 1


stack = []
for _ in range(2 * n):
    command = input()
    if "add" in command:
        command = command.split()
        num = int(command[1])
        stack.append(num)
    else:
        if stack and stack[-1] == to_be_removed:
            stack.pop()
        else:
            if stack:
                operations += 1
                stack = []
        to_be_removed += 1

print(operations)





