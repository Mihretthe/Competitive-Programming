array = [1, 2, 3, 4, 5, 6, 7]

global count
count = 0
def maximum(array): # a function with unnecessary recursive calls
    global count
    count += 1
    
    
    if len(array) == 1:
        return array[0]
    val = maximum(array[1:])
    if array[0] > val:
        return array[0]

    return maximum(array[1:])

print(maximum(array), count)


count = 0
def maximum(array): # a function with only necessary recursive calls
    global count
    count += 1
    
    
    if len(array) == 1:
        return array[0]
    val = maximum(array[1:])
    if array[0] > val:
        return array[0]

    return val

print(maximum(array), count)

memo = {}
def fibonnacci(num):
    if num in memo:
        return memo[num]
    
    if num < 2:
        return num

    memo[num] = fibonnacci(num - 1) + fibonnacci(num - 2)
    return memo[num]



