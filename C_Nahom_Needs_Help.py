n, m, k = map(int, input().split())
a = list(map(int, input().split()))
operations = []

for _ in range(m):
    operations.append(list(map(int, input().split())))

pre_operations = [0] * m
for _ in range(k):
    x, y = map(int, input().split())
    x -= 1
    pre_operations[x] += 1
    if y < m:
        pre_operations[y] -= 1
    
for i in range(1,m):
    pre_operations[i] += pre_operations[i - 1]

post_operation = [0] * n
for i in range(m):
    l, r, d = operations[i]
    l -= 1
    num = pre_operations[i]
    post_operation[l] += (num * d)
    if r < n:
        post_operation[r] -= (num * d)

for i in range(1, n):
    post_operation[i] += post_operation[i - 1]
for i in range(n):
    a[i] += post_operation[i]

print(*a)