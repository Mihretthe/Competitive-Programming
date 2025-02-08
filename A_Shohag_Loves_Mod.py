from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    array = []
    num = 1
    index = 1
    till = set()

    while len(array) < n:
        if num not in array and num % index not in till:
            array.append(num)
            till.add(num % index)
            index += 1
        else:
            num += 1
    print(*array)


 
 
 
T = I()
for _ in range(T):
    solve()