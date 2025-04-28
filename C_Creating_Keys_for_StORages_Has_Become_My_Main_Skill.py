from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()
    
    answer = []
    ans = 0
    for i in range(k + 1):
        if i | k == k:
            answer.append(i)
            ans |= i
        else:            
            if ans == k:
                print(*answer, [0 for _ in range(n - len(answer))] )
                return
            else:
                print(*answer, *[0 for _ in range(n - len(answer) - 1)], k)
                return
            
        
            
        if len(answer) == n:
            if ans == k:
                print(*answer)
                return
            break
    else:
        answer += [0 for _ in range(n - len(answer))]
        if ans == k:
            print(*answer)
        else:
            answer[-1] = k
            print(*answer)
        return
        
       
    if ans == k:
        print(*answer)
    else:
        answer[-1] = k
        print(*answer)
            
            
            
    
    
    
        
        
 
 
 
 
T = I()
for _ in range(T):
    solve()