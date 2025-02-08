from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()
    cap = k
    if n == 1 or k == 1:
        print(n)
        return
    count = 0

    while n >= 1:
        index = 0
        while cap ** index <= n:
            index += 1
        val = (n // (cap**(index - 1)))
        # print(n, val)
        count += val
        n %= (cap**(index - 1))
        
    # print("n: ", n)
    print(count)
       

        
            
 
 
 
 
T = I()
for _ in range(T):
    solve()