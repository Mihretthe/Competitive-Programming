for _ in range(int(input())):
    length, k = map(int, input().split())
    s = input()
    pattern = "RGB"
    left = 0


    operation = 0
    for i in range(k):
        if s[i] != pattern[i % 3]:
            operation += 1
    min_operation_r = operation


    for right in range(k, length):
        if s[left] != pattern[left % 3]:
            operation -= 1
        left += 1
        
        if s[right] != pattern[right % 3]:
            operation += 1
        min_operation_r = min(operation, min_operation_r)

    operation = 0
    left = 0
    for i in range(k):
        if s[i] != pattern[(i + 1) % 3]:
            operation += 1
    min_operation_g = operation

    for right in range(k, length):
        if s[left] != pattern[(left + 1) % 3]:
            operation -= 1
        left += 1
        
        if s[right] != pattern[(right + 1) % 3]:
            operation += 1
        min_operation_g = min(operation, min_operation_g)

    operation = 0
    left = 0
    for i in range(k):
        if s[i] != pattern[(i + 2) % 3]:
            operation += 1
    min_operation_b = operation

    for right in range(k, length):
        if s[left] != pattern[(left + 2) % 3]:
            operation -= 1
        left += 1
        
        if s[right] != pattern[(right + 2) % 3]:
            operation += 1
        min_operation_b = min(operation, min_operation_b)

    print(min(min_operation_b, min_operation_r, min_operation_g))
    
        

