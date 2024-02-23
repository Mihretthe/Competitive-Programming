n = int(input())
m = int(input())

capacities = []

for _ in range(n):
    capacities.append(int(input()))
capacities.sort(reverse = True)

for i in range(n):
    m -= capacities[i]
    if m <= 0:
        print(i + 1)
        break
else:
    print(n)