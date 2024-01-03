s, n = map(int, input().split())

dragons = []

for _ in range(n):
    dragons.append(list(map(int, input().split())))
dragons.sort()
for strength, bonus in dragons:
    if s > strength:
        s += bonus
    else:
        print("NO")
        break
else:
    print("YES")