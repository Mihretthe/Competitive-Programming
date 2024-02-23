n = int(input())
v = list(map(int, input().split()))
u = sorted(v)
length = len(v)
for i in range(1,length):
    u[i] += u[i - 1]
    v[i] += v[i - 1]

for _ in range(int(input())):
    type, l, r = map(int, input().split())
    if type == 1:
        if l > 1:
            print(v[r - 1] - v[l - 2])
        else:
            print(v[r - 1])
    else:
        if l > 1:
            print(u[r - 1] - u[l - 2])
        else:
            print(u[r - 1])

