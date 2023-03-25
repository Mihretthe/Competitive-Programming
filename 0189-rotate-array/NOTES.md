class Solution:
def rotate(self, nums: List[int], k: int) -> None:
"""
Do not return anything, modify nums in-place instead.
"""
r=len(nums)-1
while k>0:
nums.insert(0,nums[r])
nums=nums[:r+1]
print(nums)
k-=1