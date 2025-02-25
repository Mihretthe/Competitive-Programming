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
    
    counter = [0] * (n + 1)
    
    for num in a:
        counter[num] += 1
    
    indexes = []
    
    # print(counter)
  
    for i in range(n):
        if counter[a[i]] == 1:
            indexes.append(i)
    
    if not indexes:
        print(0)
        return
    # print(indexes)
    ans = []
    starter = indexes[0]
    
    for i in range(1, len(indexes)):
        if indexes[i] - 1 != indexes[i - 1]:
            if ans:
                if ans[-1] - ans[0] < indexes[i - 1] - starter:
                    ans = [starter + 1, indexes[i - 1] + 1]
            else:
                ans = [starter + 1, indexes[i - 1] + 1]
            starter = indexes[i]
    
            
    if len(indexes) > 1 and indexes[-1] - indexes[-2] == 1:
        if ans:
            if ans[-1] - ans[0] < indexes[-1] - starter:
                ans = [starter + 1, indexes[-1] + 1]
        else:
            ans = [starter + 1, indexes[-1] + 1]
    
    
       
    
    
    if ans:
        print(*ans)
    else:
        print(indexes[0] + 1, indexes[0] + 1)
 
 
T = I()
for _ in range(T):
    solve()