k = int(input())

def fun(n):
    if n % 2 == 0:
        return (n // 2)
    return (3 * (n) + 1)

index = 1
num = fun(k)

while num != 1:
    num = fun(num)
    index += 1

print(index)
