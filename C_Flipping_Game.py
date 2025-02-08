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
    
    if n == 1:
        if a[0] == 1:
            print(0)
        else:
            print(1)
        return
    
    number_of_ones = [0]
    total = sum(a)
    
    for i in range(n):
        if a[i] == 1:
            number_of_ones.append(number_of_ones[-1] + 1)
        else:
            number_of_ones.append(number_of_ones[-1])
    
    # print(number_of_ones)    
    
    def calc(i, j):
        if i > 0:
            num = number_of_ones[j] - number_of_ones[i - 1]
            diff = j - i + 1
        else:
            num = number_of_ones[j] # 1
            diff = 1
         # 0
        tot = total # 2
        tot -= num # 2
        tot += (diff - num)
        
        return tot
        
        
        
    maxi = 0
    
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            # print(calc(i, j), i, j)
            maxi = max(maxi, calc(i, j))
        
    print(maxi)            
 
 
 
 
T = 1
for _ in range(T):
    solve()