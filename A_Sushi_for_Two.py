def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)
 
def solve():
    n = I()
    t = IL()
    ans = 0

    ones = []
    twos = []

    for i in t:
        if i == 2:
            twos.append("1")
            ones.append("0")
        else:
            twos.append("0")
            ones.append("1")

    ans = 0
    twos = "".join(twos)
    ones = "".join(ones)
    for i in range(1, n//2 + 1):
        if "1" * i in twos and "1" * i in ones:
            ans = i * 2

    print(ans)
    

        

        
 
 
 
 
T = 1
for _ in range(T):
    solve()