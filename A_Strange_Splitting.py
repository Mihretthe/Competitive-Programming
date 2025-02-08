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

    if len(set(a)) == 1:
        print("NO")
        return 

    print("YES")
    indices = {}
    counter = {}

    for i in range(n):
        indices[a[i]] = i 
        if a[i] in counter:
            counter[a[i]] += 1
        else:
            counter[a[i]] = 1
    
    answer = ['R'] * n

    for i in counter:
        if counter[i] > 1:
            answer[indices[i]] = "B"
            break
    else:
        answer[-1] = "B"

    print("".join(answer))
    

    

 
 
 
 
T = I()
for _ in range(T):
    solve()