from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import inf

def solve():
    n = I()
    a = IL()
    
    
    def monotonic(array):
        prefix = [0]
        
        for i in range(len(array)):
            prefix.append(prefix[-1] + array[i])
            
        array = [inf] + array
        
        #decreasing
        stack = []
        
        for i in range(1, len(array)):
            while stack and array[stack[-1]] <= array[i]:
                index = stack.pop()
                right = i - 1
                left = index - 1
                if prefix[right] - prefix[left] > 0:
                    return False
            stack.append(i)
        
        return True
    

    if  monotonic(a) and monotonic(a[::-1]):
        print("YES")
    else:
        print("NO")
                
            
                        
        
        
        

    
    
    
    
 
 
 
 
T = I()
for _ in range(T):
    solve()