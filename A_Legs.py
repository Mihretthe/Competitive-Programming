test =int(input())
for _ in range(test):
    n = int(input())
    a = n//4
    if n%4:
        a += 1
        print(a)
    else: print(a)
  