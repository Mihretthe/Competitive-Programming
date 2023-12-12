hashmap = {"a" : 0, "b" : 1, "c" : 2}
t = int(input())

for _ in range(t):
    s = input()
    a = []
    for i in s:
        a.append(hashmap[i])
    if a == sorted(a) or a == sorted(a)[::-1]:
        print("YES")
        continue

    for i in range(2):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            break
    if a == sorted(a):
        print("YES")
    else:
        print("NO")