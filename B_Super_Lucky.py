def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)



def isLucky(s):
    return s.count("4") == s.count("7")

path = []
ans = []
def backtrack(index, n, s):
   
    if index == n:
        answer = "".join(path[:])
        ans.append(answer)
        if isLucky(answer) and answer >= s:            
            return True                
        return 
        
    for i in "47":
        path.append(i)
        if backtrack(index + 1, n, s):
            return True
        path.pop()

def solve():
    s = input()
    n = len(s)
    
    if backtrack(0,n,s):
        print(ans[-1])
    else:
        print("4" * (n // 2 + 1) + "7" * (n // 2 + 1))
    
 
T = 1
for _ in range(T):
    solve()