from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    total = n * (n + 1) // 2
    
    if total % 2:
        print("NO")
        return
    
    total //= 2
    
    
    """
    to find the numbers sum up to total // 2, we use backtracking of finding the sum then if 
    
    """  
    path2 = []
    path = []
    
    for i in range(n, 0, -1):
        if i <= total:
            path.append(i)
            total -= i 
        else:
            path2.append(i)
    print("YES")
    print(len(path))
    print(*path)
    print(len(path2))
    print(*path2)
            
 
 
 
 

    
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    T = 1
    for _ in range(T):
        solve()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
    
    
    
    