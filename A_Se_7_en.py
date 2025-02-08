from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

d = []

for i in range(10, 1000):
    if i % 7 == 0:
        d.append(str(i))



def solve():
    n = I()
    if n % 7 == 0:
        print(n)
        return 
    n = str(n)
    ans = ""
    for i in d:
        count = 0
        if len(i) != len(n):
            continue
        for a, b in zip(i, n):
            if a != b:
                count += 1
            
        if not ans:
            ans = (i, count)
        else:
            if ans[1] > count:
                ans = (i, count)
        
    print(ans[0])



    
    

        

        
        
 
 
 
 
T = I()
for _ in range(T):
    solve()