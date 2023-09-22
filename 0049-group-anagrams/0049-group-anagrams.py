class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         ans = []
#         v = []
#         for i in range(len(strs)):
#             if strs[i] in v:
#                 continue
#             a = Counter(strs[i])
#             ana = []
#             for j in strs:
#                 if Counter(j) == a and j not in v:
#                     ana.append(j)
#             v += ana
#             ans.append(ana)
                    
        
#         return ans    
            
        memo = defaultdict(list)
        for i in strs:
            s = "".join(sorted(i))
            memo[s].append(i)
        return memo.values()
        
        
                    