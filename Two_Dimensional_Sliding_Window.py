matrix = [[1,2,3],[4,5,6],[6,7,8]]

# fixed window 2 x 2
starter = 0
answer = 0

for rows in range(2):
    for cols in range(2):
        starter += matrix[rows][cols]
for rows in range(2):
    ans = starter
    for cols in range(1, 3 - 1):
        ans -= matrix[rows][cols - 1]
        ans += matrix[rows][cols + 1]

    answer = max(ans, answer)

    
print(answer)
        




