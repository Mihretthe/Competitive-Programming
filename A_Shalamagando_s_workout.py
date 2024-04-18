from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    a = IL()
    answer = [0] * 3

    for i in range(n):
        answer[i % 3] += a[i]
    
    dict = {0 : "chest", 1 : "biceps" , 2 : "back"}

    print(dict[answer.index(max(answer))])
        
 
 
 
T = 1
for _ in range(T):
    solve()