from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

pair = [(0,0),(1,3),(2,6),(3,1),(4,4),(5,7),(6,2),(7,5),(8,8)]

def solve():
    sudoku = []
    count = 0
    for _ in range(9):
        sudoku.append(list(S()))
    
    for i, j in pair:
        if sudoku[i][j] == "1":
                sudoku[i][j] = "2"
        else:
            sudoku[i][j] = "1"
    for row in sudoku:
         print("".join(row))


    
    
 
 
 
T = I()
for _ in range(T):
    solve()