
# memo = {}
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return n
#     if n in memo:
#         return memo[n]
#     memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

#     return fibonacci(n - 1) + fibonacci(n - 2)


n, k = map(int, input().split())
sequence = 0
a = 1
b = 2

for i in range(1, n + 1):
    if i <= 2:
        sequence += (i * (i ** k))
    else:
        a, b = b, a + b         
        sequence += (b * (i ** k))

print(sequence % 1000000007)



