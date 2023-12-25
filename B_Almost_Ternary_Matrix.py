row = [1,0,0,1]
row_invert = [0,1,1,0]

testcase = int(input())

for _ in range(testcase):
    n, m = map(int, input().split())
    
    row_new = row * (m // 4) + row[: m % 4]
    row_invert_new = row_invert * (m // 4) + row_invert[: m % 4]

    
    for i in range(n):
        if i % 3 != 0:
            print(*row_invert_new)
        else:
            print(*row_new)


