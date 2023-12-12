import math

for _ in range(int(input())):
    n, c = map(int, input().split())
    s = list(map(int, input().split()))

    size_sum = sum(s)

    square_sum = [i * i for i in s]
    square_sum = sum(square_sum)

    answer = (((0 - size_sum) + (math.sqrt((size_sum * size_sum) + (4 * n * (((c - square_sum)//4))))))) / ( 2 * n)

    print(math.ceil(answer))