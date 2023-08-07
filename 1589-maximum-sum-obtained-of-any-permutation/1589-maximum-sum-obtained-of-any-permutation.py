class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        a = [0] * n
        for i, j in requests:
            a[i] += 1
            if j + 1 < n:
                a[j + 1] -= 1
        for i in range(1, n):
            a[i] += a[i - 1]
        a.sort(reverse = True)
        nums.sort(reverse = True)
        sumz = 0
        for i in range(n):
            if a[i] == 0:
                break
            sumz += (nums[i] * a[i])     
        
        
        return int(sumz % (1e9 + 7))