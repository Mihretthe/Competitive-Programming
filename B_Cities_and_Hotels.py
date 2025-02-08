from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, d = II()
    a = IL()
    
    if n == 1:
        print(2)
        return 
    
    collect = set()
    
    for i in range(n):
        num = a[i] + d
        if i == 0:
            if i + 1 < n:
                if abs(a[i + 1] - num) >= d:
                    # print(i)
                    collect.add(num)
                
        elif i == n - 1:
            if i - 1 >= 0:
                if abs(a[i - 1] - num) >= d:
                    # print(i)
                    collect.add(num)
        else:
            if abs(num - a[i - 1]) >= d and abs(num - a[i + 1]) >= d:
                # print(i)
                collect.add(num)
        
        num = a[i] - d
        if i == 0:
            if i + 1 < n:
                if abs(a[i + 1] - num) >= d:
                    # print(i)
                    collect.add(num)
                
        elif i == n - 1:
            if i - 1 >= 0:
                if abs(a[i - 1] - num) >= d:
                    # print(i)
                    collect.add(num)
        else:
            if abs(num - a[i - 1]) >= d and abs(num - a[i + 1]) >= d:
                # print(i)
                collect.add(num)
        
    print(len(collect) - len(collect & set(a)))
 
 
 
 
T = 1
for _ in range(T):
    solve()