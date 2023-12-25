n, m = map(int, input().split())
cs = 0
rs = 0
ct = 0
rt = 0

matrix = []

for i in range(n):
    s = list(input())
    if "S" in s:
        cs = s.index("S")
        rs = i
    
    if "T" in s:
        ct= s.index("T")
        rt = i
    
    matrix.append(s)


mymat = matrix[rs:rt + 1]

trans = list(zip(*mymat))

if rs == rt and len(set(matrix[rs][cs:ct + 1])) == 1 and matrix[rs][cs:ct + 1][1] == ".":
    print("YES")

elif cs == ct and len(set(trans[rs][rs:rt + 1])) == 1 and trans[cs][rs:rt + 1][1] == ".":
    print("YES")
else:

    
    for row in trans:
        if "S" in row and "T" in row:
            a = row[row.index("S") + 1:row.index("T") ]
            if a and len(set(a)) == 1 and a[0] == ".":
                print("YES")
                break
            elif a == []:
                print("YES")
                break

        if len(set(row)) == 1 and row[0] == "." :
            print("YES")
            break
    else:
        print("NO")
