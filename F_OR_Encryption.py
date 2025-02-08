from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    matrix = []
    answer = []
    all_zero = True
    for _ in range(n):
        row = IL()
        matrix.append(row)
        andy = 2**31 - 1
        for i in range(n):
            if row[i] != 0:
                all_zero = False
            if i != _:
                andy &= row[i]
        if andy == 2**31 - 1:
            andy = 1073741822
        answer.append(andy)
    
    if all_zero:
        print("YES")
        print(*answer)
    else:
        if len(set(answer)) == 1 and 0 in set(answer):
            print("NO")
        else:
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] != matrix[j][i]:
                        print("NO")
                        return 
                    if i != j and  (answer[i]|answer[j]) != matrix[i][j]:
                        print("NO")
                        return            
            print("YES")
            print(*answer)
        
    
    
        
 
 
 
 
T = I()
for _ in range(T):
    solve()