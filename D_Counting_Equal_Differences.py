

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    hashmap = {}

    for i in range(n):
        if (a[i] - i) in hashmap:
            hashmap[a[i] - i] += 1
            count += hashmap[a[i] - i]
        else:
            hashmap[a[i] - i] = 0

    print(count)
    

            

        


   