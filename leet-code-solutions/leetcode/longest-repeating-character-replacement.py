class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # only the maximum frequency makes change
        length = len(s)
        counter = defaultdict(int)
        left = 0
        longest = 0
        max_count = 0

        for right in range(length):
            counter[s[right]] += 1
            max_count = max(max_count, counter[s[right]])
            window = right - left + 1
            while left < right and window - max_count > k:             
                counter[s[left]] -= 1
                window -= 1              
                left += 1
            longest = max(longest, right - left + 1)                      
        return longest
        