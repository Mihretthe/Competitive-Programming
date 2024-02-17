class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def makeMax(counter):
            if not counter:
                return ""
            max_count = ""
            val = 0
            for key, value in counter.items():
                if value > val:
                    max_count = key
                    val = value
            
            return max_count

        length = len(s)
        counter = defaultdict(int)
        left = 0
        longest = 0
        max_count = makeMax(counter)

        for right in range(length):
            counter[s[right]] += 1
            max_count = makeMax(counter)
            window = right - left + 1
            while left < right and window - counter[max_count] > k:             
                counter[s[left]] -= 1
                window -= 1
                max_count = makeMax(counter)                
                left += 1
            longest = max(longest, right - left + 1)      

                
        return longest
        