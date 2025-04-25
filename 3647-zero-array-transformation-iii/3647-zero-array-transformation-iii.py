class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # sort the queries
        queries.sort()

        # two heaps
        # max heap
        candidate = []
        # min heap
        chosen = []

        answer = 0
        length = len(nums)
        queries_length = len(queries)

        index = 0
        for i in range(length):
            while index < queries_length and queries[index][0] == i:
                heappush(candidate, -queries[index][1])
                index += 1

            nums[i] -= len(chosen)

            while nums[i] > 0 and candidate and -candidate[0] >= i:
                answer += 1
                heappush(chosen, -heappop(candidate))
                nums[i] -= 1
            
            if nums[i] > 0:
                return -1
            
            while chosen and chosen[0] == i:
                heappop(chosen)
            
        return queries_length - answer
            
