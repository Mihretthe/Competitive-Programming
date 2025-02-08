from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    array = IL()
    s = S()
    one = 0
    zero = 0

    prexor = [0]
    #pre-calculate
    for i in range(n):
        if s[i] == "0":
            zero ^= array[i]
        else:
            one ^= array[i]
        prexor.append(prexor[-1] ^ array[i])

     
    answer = []
    q = I()
    for _ in range(q):
        command = IL()
        if len(command) == 2:
            g = command[1]
            if g == 1:
                answer.append(one)
            else:
                answer.append(zero)

        else:
            l, r = command[1:]
            xor = prexor[r] ^ prexor[l - 1]
            one ^= xor
            zero ^= xor
    
    print(*answer)



    

 
 
 
 
T = I()
for _ in range(T):
    solve()


