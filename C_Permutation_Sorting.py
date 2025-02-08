from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


from collections import deque


def solve():
    n = I()
    p = IL()
    def divide(array, mid):
        n = len(array)
        if array == sorted(array) or not array:
            return 0
        
        left = []
        right = []
        for i in array:
            if i < mid + 1:
                left.append(i)
            else:
                right.append(i)
        
        
        return 1 + divide(left, mid // 2) + divide(right, mid + mid // 2)

    print(divide(p, 2))
        
    


    
   

    
    
 
 
 
T = I()
for _ in range(T):
    solve()