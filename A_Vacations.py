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

    memo = {}
    def dp(index, lastTaken):
        if (index, lastTaken) in memo:
            return memo[(index, lastTaken)]
        
        if index == n:
            return 0

        if a[index] == 0:
            memo[(index, lastTaken)] = 1 + dp(index + 1, 0)
        
        elif a[index] == 3:
            one = int(lastTaken == 1) + dp(index + 1, 1)
            two = int(lastTaken == 2) + dp(index + 1, 2)
            zero = 1  + dp(index + 1, 0)

            memo[(index, lastTaken)] = min(one, two, zero) 

        else:
            memo[(index, lastTaken)] = int(lastTaken == a[index]) + dp(index + 1, a[index])
        
        return memo[(index, lastTaken)]
    
    print(dp(0, 8))
        

        
        


 
 
 
 
T = 1
for _ in range(T):
    solve()