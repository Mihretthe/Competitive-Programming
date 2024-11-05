class Solution:
    def minChanges(self, s: str) -> int:
        
        array = []

        for i in range(0, len(s), 2):
            array.append(s[i] + s[i + 1])
        
        ans = 0

        for match in array:
            if match != "00" and match != "11":
                ans += 1

                
        return ans