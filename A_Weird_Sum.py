n, m = map(int, input().split())
matrix = []
collect = {}
sum_same = 0

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] in collect:
            sum_same += abs(i + 1 - collect[row[j]][-1][0]) + abs(j + 1 - collect[row[j]][-1][1])
            collect[row[j]].append((i + 1,j + 1))
        else:
            collect[row[j]] = [(i + 1,j + 1)]
# print(collect)
print(sum_same)
        

    
    

