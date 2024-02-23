from math import sqrt

for _ in range(int(input())):
    vertices = []
    for __ in range(4):
        vertices.append(list(map(int, input().split())))

    vertices.sort()
    side = (vertices[1][1] - vertices[0][1]) 

    print(side * side)



