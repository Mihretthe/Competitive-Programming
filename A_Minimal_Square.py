testCase = int(input())
for _ in range(testCase):
    a, b = map(int, input().split())
    
    print((min(max(2 * b, a), max(2 * a, b))) ** 2)