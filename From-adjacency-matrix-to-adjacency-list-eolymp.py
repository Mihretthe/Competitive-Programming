def indexes(lists):
    ans = []
    for i in range(len(lists)):
        if lists[i] == 1:
            ans.append(str(i + 1))
    return " ".join(ans)
count = 0
for i in range(int(input())):
    row = list(map(int, input().split()))
    print( row.count(1), indexes(row))
