class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_blue = 0
        count = 0
        
        for i in range(len(flips)):
            max_blue = max(max_blue, flips[i])
            if i + 1 == max_blue:
                count += 1
            
            

        return count

            
