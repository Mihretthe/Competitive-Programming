class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        type = {}
        length = len(fruits)
        max_sum = 0
        sum = 0

        for right in range(length):
            if fruits[right] in type:
                type[fruits[right]] += 1
            else:
                type[fruits[right]] = 1
            sum += 1

            while left < right and len(type) > 2:
                type[fruits[left]] -= 1
                sum -= 1
                if type[fruits[left]] == 0:
                    del type[fruits[left]]
                left += 1
            max_sum = max(max_sum, sum)

        return max_sum
        
