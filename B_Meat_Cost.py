n = int(input())
a = []
p = []

for _ in range(n):
    amount, cost = map(int, input().split())
    a.append(amount)
    p.append(cost)

minimum = float("inf")
total_meet = sum(a)
money = 0

for i in range(n):
    minimum = min(p[i], minimum)

    money += (a[i] * minimum)
    total_meet -= a[i]

print(money)


