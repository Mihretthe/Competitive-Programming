matrix = []
a = 0
b = 0
for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        a = i
        b = row.index(1)
    matrix.append(row)
print(abs(2 - a) + abs(2 - b))

