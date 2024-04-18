n = int(input())
neg = 0
pos = 0
nums = list(map(int,input().split()))
for i in nums:
    if i < 0 :
        neg+=i
    else:
        pos+=i
print(pos- neg )
    
