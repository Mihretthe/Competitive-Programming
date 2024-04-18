from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    s = S()
    f = S()
    count_f = f.count("1")
    countfz = n - count_f
    count_s = s.count("1")
    countsz = n - count_s

    

    
    print(count_f,countsz, countfz, count_s)
            

 
 
 
T = I()
for _ in range(T):
    solve()


   