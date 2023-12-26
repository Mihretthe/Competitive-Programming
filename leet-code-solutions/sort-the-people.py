class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)

        for i in range(n):
            position = i
            for j in range(i + 1, n):
                if heights[j] > heights[position]:
                    position = j
            names[i], names[position] = names[position], names[i]
            heights[i], heights[position] = heights[position], heights[i]

        return names
