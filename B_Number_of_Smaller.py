n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []

idx = 0
for num in b:
    while idx < n and num > a[idx]:
        idx += 1
    ans.append(idx)
print(*ans)


"""
start from the left and append how many numbers that are less than it 
while sorting using merge sort we store the sorted array and the sorted array before it counts as a smaller number
"""