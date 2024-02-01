class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        answer = []

        for i in range(length): 
            if answer and len(answer[-1]) < 3:
                if nums[i] - answer[-1][0] <= k:
                    answer[-1].append(nums[i])
                else:
                    return []
            else:
                answer.append([nums[i]])

        return answer
