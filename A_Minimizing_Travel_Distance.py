x = list(map(int, input().split()))
x.sort()
a,b,c = x

print(b - a + c - b)