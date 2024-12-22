class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        check_set = set()
        longest_substring = 0

        while l < len(s) and r < len(s):
            if s[r] in check_set:
                check_set.remove(s[l])
                l += 1
            else:
                check_set.add(s[r])
                r += 1
                longest_substring = max(longest_substring, r - l)

        return longest_substring