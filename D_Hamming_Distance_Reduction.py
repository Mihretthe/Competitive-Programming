from collections import defaultdict

n = int(input())
s = input()
t = input()


test = defaultdict(int)
ans = []

for i in range(n):
    if s[i] != t[i]:
        if t[i] in test:
            ans =[i + 1, test[t[i]] + 1]
            del test[t[i]]
        else:
            test[s[i]] = i

print(len(test))
print(*ans)