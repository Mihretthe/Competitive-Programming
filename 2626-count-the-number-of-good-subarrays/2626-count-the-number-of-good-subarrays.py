class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        def calc(num):
            
            return  (num * (num - 1)) // 2

        

        length = len(nums)
        total = (length * (length + 1)) // 2

        left = 0
        counter = defaultdict(int)
        calculation = 0
        for right in range(length):
            
            calculation -= calc(counter[nums[right]])

            counter[nums[right]] += 1

            calculation += calc(counter[nums[right]])

            
            while calculation >= k:
                
                calculation -= calc(counter[nums[left]])
                counter[nums[left]] -= 1
                calculation += calc(counter[nums[left]])
                left += 1

            total -= (right - left + 1)
            
        return total



