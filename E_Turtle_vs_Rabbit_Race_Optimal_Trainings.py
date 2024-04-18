from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

    

def solve():
    length = I()
    nums = IL()
    
    def check(left, right, u):
        count = 0
        for i in range(left, right + 1):
            if u >= nums[i] - u:
                count += 1
                u -= nums[i]
            else:
                break
        return count
    ans = []
    for _ in range(I()):
        left, u = II()  
        right = length - 1
        left -= 1
        right = length - 1
        for i in range(length - 1, left - 1, -1):
            right = max(right,check(left, i, u)) 
        ans.append(right)
            

    print(*ans)

            

   
 
 
 
 
T = I()
for _ in range(T):
    solve()







