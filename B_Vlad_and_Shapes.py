for _ in range(int(input())):
    n = int(input())
    
    counts = set()
    for i in range(n):
        count_1 = input().count("1")
        if count_1 > 0:
            counts.add(count_1)
    if len(counts) == 1:
        print("SQUARE")
    else:
        print("TRIANGLE")
