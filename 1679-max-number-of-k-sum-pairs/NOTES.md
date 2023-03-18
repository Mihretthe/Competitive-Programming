class Solution:
def maxOperations(self, nums: List[int], k: int) -> int:
count=0
x=list(list())
for i in range(len(nums)):
for j in range(i+1,len(nums)):
x.append((nums[i],nums[j]))
for i in range(len(x)):
if x[i][0]+x[i][1]==k:
count+=1
print(x)
return count
class Solution:
def maxOperations(self, nums: List[int], k: int) -> int:
c=0
for i in range(len(nums)-1):
for j in range(i+1,len(nums)):
if nums[i]+nums[j]==k and j!=i:
c+=1
# x=lambda a:a=j
del nums[i]
del nums[j]
break
print(nums)
return c