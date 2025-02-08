from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    s = S()
    n = len(s)
    ptr = 0
    for i in range(n):
        if s[i] == "1":
            ptr = i 
            break
    
    count = 0
    if s[ptr] == "1":
        for i in range(ptr + 1, n):
            if s[i] == "0":
                count += (i - ptr + 1)
                ptr += 1

    print(count)


 
 
 
 
T = I()
for _ in range(T):
    solve()