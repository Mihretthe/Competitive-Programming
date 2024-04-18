for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    first = a[0]
    last = a[-1]

    #for first

    left = 1
    right = n - 1

    while left <= right:
        if a[left] != first and a[right] != first:
            break
        if a[left] == first:
            left += 1
        if a[right] == first:
            right -= 1
        

    if left > right:
        first = 0
    else:
        first = right - left + 1

    #for last

    left = 0
    right = n - 2

    while left <= right:
        if a[left] != last and a[right] != last:
            break
        if a[left] == last:
            left += 1
        if a[right] == last:
            right -= 1

        
    if left > right:
        last = 0
    else:
        last = right - left + 1

  
    print(min(last, first))