n = int(input())
register = {}

for _ in range(n):
    s = input()
    if s not in register:
        register[s] = 1
        print("OK")
    else:
        print(s + str(register[s]))
        register[s] += 1


