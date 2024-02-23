n = int(input())
x = list(map(int, input().split()))
mini = x[0]
maxi = x[-1]

for i in range(n):
    if i == 0:
        print(abs(x[i] - x[i + 1]), abs(maxi - mini))
    elif i == n - 1:
        print(abs(x[i] - x[i - 1]), abs(maxi - mini))
    else:
        print(min(abs(x[i] - x[i + 1]), abs(x[i] - x[i - 1])), max(abs(mini - x[i]), abs(maxi - x[i])))