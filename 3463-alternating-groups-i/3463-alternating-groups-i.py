class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        length = len(colors)
        count = 0

        for i in range(1, length - 1):
            if colors[i] != colors[i - 1] and colors[i] != colors[i + 1]:
                count += 1
        if colors[0] != colors[1] and colors[0] != colors[-1]:
            count += 1

        if colors[0] != colors[-1] and colors[-2] != colors[-1]:
            count += 1
        
        return count