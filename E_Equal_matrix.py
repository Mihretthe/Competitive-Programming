for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    operations = 0

    for i in range(n):
        for j in range(m):
            a = matrix[i][j]
            b = matrix[i][m - 1 - j]
            c = matrix[n - 1 - i][j]
            d = matrix[n - 1 - i][m - 1 - j]

            take = min(a,b,c,d) + min(abs(a - c) // 2, abs(b - d) // 2)
            operations += (abs(a - take) + abs(b - take)+ abs(c - take) + abs(d - take))
            
    print(operations // 4)