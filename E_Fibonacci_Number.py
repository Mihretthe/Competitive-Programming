memo = {}

def fibonacci(num):    
    if num == 0 or num == 1:
        return num
    
    if num in memo:
        return memo[num]
    
    memo[num] = fibonacci(num - 1) + fibonacci(num - 2)
    
    return fibonacci(num - 1) + fibonacci(num - 2)


fibonacci_number = int(input())

count = 0
num = 0
number = 0
flag = False

while fibonacci_number > number:
    number = fibonacci(num)
    if number == fibonacci_number:
        print(count % 10000000000000)
        break
    count += 1
    num += 1
else:
    print(-1)

