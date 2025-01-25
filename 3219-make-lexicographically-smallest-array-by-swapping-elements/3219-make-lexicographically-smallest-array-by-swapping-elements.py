class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        sorted_nums = sorted([(nums[i], i) for i in range(len(nums))])

        left = 0
        right = 1


        parent = {i:i for i in range(len(nums))}

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            parentX = find(x)
            parentY = find(y)

            if parentX != parentY:
                parent[parentY] = parentX
            

        while right < len(nums):
            if abs(sorted_nums[left][0] - sorted_nums[right][0]) <= limit:
                # print(sorted_nums[left][0], sorted_nums[right][0])
                union(sorted_nums[left][1], sorted_nums[right][1])
                right += 1
            else:
                left += 1
        
        
        answer = [0] * len(nums)

        collect = defaultdict(list)

        for i in parent:
            collect[parent[i]].append(i)
        
        
        for key, value in collect.items():
            val = [nums[i] for i in value]
            val.sort()
            index = 0
            for i in value:
                answer[i] = val[index]
                index += 1
        
        return answer
