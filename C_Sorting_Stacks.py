for _ in range(int(input())):
    n = int(input())
    heights = list(map(int, input().split()))
    

    remain = 0

    for i in range(n):
        if heights[i] + remain < i:
            print("NO")
            break

        remain += heights[i] - i

    else:
        print("YES")

