n = int(input())
welfare = list(map(int, input().split()))
welfare.sort()
m = welfare[-1]
burles = 0
for i in welfare:
    burles += (m - i)
print(burles)