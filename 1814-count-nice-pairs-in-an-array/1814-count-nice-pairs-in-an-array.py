class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            a = str(num)
            a = a[::-1]
            return num - int(a)
        hashmap = defaultdict(int)
        for i in nums:            
            hashmap[rev(i)] += 1
        count = 0
        for i in hashmap:
            r = hashmap[i]
            if r > 1:
                a = math.factorial(r) / (math.factorial(2)*(math.factorial(r - 2)))
                count += a
        return int(int(count) % (1e9 + 7))
            