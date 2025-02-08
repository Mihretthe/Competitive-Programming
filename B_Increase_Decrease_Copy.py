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
    b = IL()

    operations = 0
    last = b[-1]
    flag = False

    for i in range(n):
        if not flag and last in range(min(a[i], b[i]), max(a[i], b[i]) + 1):
            operations += 1
            flag = True
        operations += abs(a[i] - b[i])


    if flag:
        print(operations)
        return
    
   
    
    num = float('inf')
    a = a + b[:-1]
    add = float('inf')

    for i in range(2 * n):
        if abs(num - last) > abs(last - a[i]):
            num = a[i]



    print(operations + abs(last - num) + 1)
    
    
 
 
 
 
T = I()
for _ in range(T):
    solve()