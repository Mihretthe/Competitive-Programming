class Solution:
    def balancedString(self, s: str) -> int:
        def helper(counter, needed):
            for i in needed:
                if i not in counter or counter[i] < needed[i]:
                    return False
            return True

        counter = Counter(s)
        length = len(s)
        fourth = length // 4
        min_sub = 0
        min_length = inf
        needed = {}


        for key, value in counter.items():
            if value > fourth:
                min_sub += value - fourth
                needed[key] = value - fourth
            
        counter2 = defaultdict(int)
        for i in s[:min_sub]:
            if i in needed:
                counter2[i] += 1
                
        left = 0
        for right in range(min_sub, length):
            if s[right] in needed:
                counter2[s[right]] += 1
            
            while left <= right and counter2 and helper(counter2, needed):
                min_length = min(min_length, right - left + 1)
                if s[left] in counter2:
                    counter2[s[left]] -= 1
                left += 1        
        
        if min_length == inf:
            return 0
        return min_length