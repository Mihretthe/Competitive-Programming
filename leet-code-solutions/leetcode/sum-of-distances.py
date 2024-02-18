class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        def doPrefix(nums):
            length = len(nums)
            ans = []
            prefix = []
            for i in range(length):
                if prefix:
                    prefix.append(prefix[-1] + nums[i])
                else:
                    prefix.append(nums[i])
            
            for i in range(length):
                before = (nums[i] * (i + 1)) - prefix[i]
                after = prefix[-1]  - prefix[i] - (nums[i] * ( length - i - 1))
                ans.append(before + after)

            return ans

            


        length = len(nums)
        indices = defaultdict(list)
        answer = [0] * length


        for i in range(length):
            indices[nums[i]].append(i)

        for key, values in indices.items():
            new = doPrefix(values)
            for i in range(len(values)):
                answer[values[i]] = new[i]

        return answer