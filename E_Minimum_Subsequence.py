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
    
    zeros = []
    ones = []
    collect = []
    
    maxi = 1
    for i in range(n):
        if s[i] == "0":
            if ones:
                index = ones.pop()
                collect.append(collect[index])
            else:
                collect.append(maxi)
                maxi += 1   
            zeros.append(i)            
        else:
            if zeros:
                index = zeros.pop()
                collect.append(collect[index])
            else:
                collect.append(maxi)
                maxi += 1   
            ones.append(i) 
    
    print(max(collect))
    print(*collect)
    
        

   
        
        
    
        
    
            
            
        
    
            
    
 
 
T = I()
for _ in range(T):
    solve()