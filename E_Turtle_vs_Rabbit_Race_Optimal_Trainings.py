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
    
    prefix = [0]

    for num in nums:
        prefix.append(prefix[-1] + num)
    
    # print(prefix)

    def add(i, j):
        i -= 1
        i = i*(i + 1) // 2
        j = j *(j + 1) // 2

        return j - i
    
    def check(l, r):
        val = prefix[r] - prefix[l - 1]
        
        return val
    
    answer = []
    for _ in range(I()):
        l, u = II()
        
        r = length 
        init = l 

        while l + 1< r:
            mid = (l + r) // 2
            val = check(init, mid)
            if val <= u:
                l = mid 
            elif val > u:
                r = mid 
        vall = check(init, l)
        val2 = check(init, r)
        first = add(vall - u, u + 1)
        second = add(val2 - u, u + 1)
        

        if first >= second:
            answer.append(l)
        else:
            answer.append(r)
    
    print(*answer)

        

 
T = I()
for _ in range(T):
    solve()
