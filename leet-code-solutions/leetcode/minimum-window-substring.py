class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(s)
        counter_t = Counter(t)
        counter_s = defaultdict(int)
        min_length = inf
        answer_window = ""

        def helper(s, t):
        
            for k, v in t.items():
                if k not in s or v > s[k]:
                    return False
            return True

        left = 0
        for right in range(length):
            if s[right] in counter_t:
                counter_s[s[right]] += 1
            while left < length and helper(counter_s, counter_t):

                if right - left < min_length :
                    min_length = right - left
                    answer_window = s[left : right + 1]
                if s[left] in counter_s:
                    counter_s[s[left]] -= 1
                    if counter_s[s[left]] == 0:
                        del counter_s[s[left]]
                left += 1
        

        
        return answer_window