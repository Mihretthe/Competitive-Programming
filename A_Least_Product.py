for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0) 
        continue   

    negatives = [i for i in a if i < 0]
    if len(negatives) == 0:
        print(1)
        print(1, 0)
        continue


    if len(negatives) % 2 == 0:
        idx = a.index(negatives[0])  
        print(1)      
        print(idx + 1, 0)
        continue
    else:
        print(0)
    


    