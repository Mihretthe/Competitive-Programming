s = input()
n = len(s)
prefix = [0]

for i in range(n - 1):
    if s[i] == s[i + 1]:
        prefix.append(prefix[-1] + 1)
    else:
        prefix.append(prefix[-1])

for _ in range(int(input())):
    l, r = map(int,input().split())
    print(prefix[r - 1] - prefix[l - 1])