t = int(input())

for _ in range(t):
    n = int(input())
    matrix = []
    operation = 0

    for i in range(n):
        row = list(map(int, list(input())))
        matrix.append(row)
    
    for i in range(n):
        for j in range(n):
            counter = {0:0, 1:0}
            counter[matrix[i][j]] += 1
            counter[matrix[j][n - i - 1]] += 1
            counter[matrix[n - 1 - j][i]] += 1
            counter[matrix[n - i - 1][n - 1 - j]] += 1

            operation += min(counter.values())



    print(operation // 4)

            
        
        


    


    







