"""
zip it up 
"""


for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    sorted_matrix = []
    indexes = set()
    indices = set(range(0, n))

    for i in range(n):
        a = list(map(int, input().split()))
        matrix.append(a)
        sorted_matrix.append(sorted(a))

    for i in range(n):
        if sorted_matrix[i] == matrix[i]:
            continue
        else:
            for j in range(m):
                if sorted_matrix[i][j] != matrix[i][j]:
                    indexes.add(j)
                    indices.discard(i)
                
                    
    if len(indexes) > 2:
        print(-1)
    elif len(indexes) == 0:
        print(1,1)
    else:
        for i in indices:
            j, k = indexes
            if matrix[i][j] != matrix[i][k]:
                print(-1)
                break
            pass
        else:
            indexes = set(map(lambda x : x + 1, indexes))
            print(*indexes)
            
        




    





































        
    #     sorted_a = sorted(a)
    #     count = 0
    #     for j in range(m):
    #         if sorted_a[j] != a[j]:
    #             count += 1
    #             ans.append(j + 1)
    #         if matrix and matrix[i - 1][j] > sorted_a[j]:
    #             flag = False
    #             break
    #         if count > 2:
    #             flag = False
    #             break
    #     matrix.append(a)
    # if flag:
    #     if ans:
    #         print(*set(ans))
    #     else:
    #         print(1,1)
    # else:
    #     print(-1)
    


        
    

    
