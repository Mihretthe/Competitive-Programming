class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = [0] * n
        ones = [0] * n

        count_z = 0
        for i in range(1, n):
            if nums[i - 1] == 0:
                count_z += 1
            zeros[i] = count_z

        count_o = 0
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                count_o += 1
            ones[i] = count_o

        for i in range(n):
            ones[i] += zeros[i]
        
        ones.append(nums.count(0))
        m = max(ones)
        ans = []
        for i, val in enumerate(ones):
            if val == m:
                ans.append(i)


        return ans


