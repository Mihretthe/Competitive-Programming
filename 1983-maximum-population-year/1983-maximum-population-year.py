class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        OFFSET = 1950

        array = [0] * 101

        for birth, death in logs:
            birth -= OFFSET
            death -= OFFSET

            array[birth] += 1
            array[death] -= 1

        for i in range(1, 101):
            array[i] += array[i - 1]
        
        maxi = max(array)
        
        return array.index(maxi) + OFFSET
