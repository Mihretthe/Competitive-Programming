from collections import Counter

for _ in range(int(input())):
    n, q = map(int, input().split())
    rectangles = []
    
    for __ in range(n):
        rectangles.append(tuple(map(int, input().split())))
    counter = Counter(rectangles)

    for __ in range(q):
        hs, ws, hb, wb = map(int, input().split())
        area = 0

        for h, w in counter:
            if h > hs and w > ws and h < hb and w < wb:
                area += (h * w) * counter[(h,w)]
        
        print(area)