from collections import defaultdict

for _ in range(int(input())):
    n, m = map(int,input().split())
    max_sum = 0

    diagonals = defaultdict(int)
    right = defaultdict(int)
    matrix = []

    for i in range(n):
        a = list(map(int,input().split()))
        for j in range(m):
            diagonals[i+j] += a[j]
            right[i - j] += a[j]
        matrix.append(a)

    
    # print(diagonals, right)
    for i in range(n):
        for j in range(m):
            max_sum = max(max_sum, (diagonals[i + j] + right[i - j] - matrix[i][j]))

    print(max_sum)
        
 


