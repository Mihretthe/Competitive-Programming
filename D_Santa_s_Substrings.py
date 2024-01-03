n = int(input())
strings = []
for _ in range(n):
    strings.append(input())

strings.sort(key = lambda x : len(x))

for i in range(1,n):
    if strings[i - 1] not in strings[i]:
        print("NO")
        break
else:
    print("YES")
    for i in strings:
        print(i)

