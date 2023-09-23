# class Solution:
#     def longestStrChain(self, words: List[str]) -> int:
#         words.sort(key = lambda x: len(x))
#         def isPredecessor(s, s2):
#             if (len(s) + 1) != len(s2):
#                 return False
#             i = 0
#             j = 0
#             count = 0
#             while i < len(s) and j < len(s2):
#                 if s[i] == s2[j]:
#                     i += 1
#                 j += 1
#             if i == len(s):
#                 return True
#             return False
#         n = len(words)
#         c = 1
#         word = words[0]
        
#         for i in range(1, n):
#             if isPredecessor(word, words[i]):
#                 c += 1
#                 word = words[i]
                
        
#         return c


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        dp = {}
        max_length = 0
        
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            max_length = max(max_length, dp[word])
        
        return max_length
            