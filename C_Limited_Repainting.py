from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, operation = II()
    string = S()
    penalities = IL()
    
    
    
    def checker(mid):
        count = 0
        flag = False
        
        for i in range(n):
            if string[i] == "B" and penalities[
        i] > mid:
                flag = True
            
            if string[i] == "R" and penalities[
        i] > mid:
                count += flag
                flag = False
                
        count += flag
        
        return count <= operation
    
    
    low = 0
    high = max(penalities)
    
    while low <= high:
        mid = (low + high) // 2
        
        if checker(mid):
            high = mid - 1
        else:
            low = mid + 1
    
    print(low)
    
    

    
 
 
 
 
T = I()
for _ in range(T):
    solve()
    
