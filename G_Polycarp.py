from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, m = II()
    array = []

    for _ in range(n):
        array.append(S())
    
    the = []

    ms = IL()

    first = None

    for i in ms:
        if first and first != len(array[i - 1]):
            print("No")
            return
        the.append(array[i - 1])
        first = len(array[i - 1])

    ans = []
    
    for i in range(first):
        fi = the[0][i]
        # flag = False
        for let in the:
            if let[i] != fi:
                ans.append("?")
                break
        else:
            ans.append(fi)
    
    
        
    for i in range(n):
        word = array[i]
        if i + 1 not in ms and len(word) == len(ans):
            
            for j in range(len(word)):
                if ans[j] != "?" and word[j] != ans[j]:
                    break
            else:
                print("No")
                return
            





    

    print("Yes")
    print("".join(ans))


        

    
 
 
 
 
T = 1
for _ in range(T):
    solve()