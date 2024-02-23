def isOdd(a):
    return a % 2 == 1

def bothEven(a,b):
    return a % 2 == b % 2 == 0

def calculate(a,b):
    if a % 2 == 0:
        if a // 2 == b:
            print("No")
        else:
            print("Yes")

for _ in range(int(input())):
    a, b = map(int, input().split())

    if isOdd(a) and isOdd(b):
        print("No")
    else:
        if bothEven(a,b):
            if a // 2 == b and b // 2 == a:
                print("No")
            else:
                print("Yes")
        else:
            calculate(a,b)
            calculate(b,a)
    