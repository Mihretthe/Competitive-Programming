class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens = {i:nums[i] for i in range(len(nums)) if nums[i] % 2 == 0}
        answer = []

        s = sum(evens.values())

        for val, index in queries:
            nums[index] += val
            if nums[index] % 2 == 0:
                if index in evens:
                    s += nums[index] - evens[index]
                    evens[index] = nums[index]
                else:
                    evens[index] = nums[index]
                    s += nums[index]
            else:
                if index in evens:
                    s -= evens[index]
                    evens.pop(index)
                
            answer.append(s)
            
        
        return answer