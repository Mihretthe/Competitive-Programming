class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        def addDigits(num):

            ans = 0

            while num:
                ans += num % 10
                num //= 10
            
            return ans
        flag = False
        for num in nums:
            n = addDigits(num)
            heappush(hashmap[n], num)
            if len(hashmap[n]) > 2:
                heappop(hashmap[n])
        maxi = -1

        for key, value in hashmap.items():
            if len(value) > 1:
                maxi = max(maxi, sum(value))
                

        return maxi

