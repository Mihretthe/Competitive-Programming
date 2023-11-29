class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = lambda x : len(x))
        pre = strs[0]
        ans = ""
        for i in range(len(pre)):
            for j in strs[1:]:
                if j[i] != pre[i]:
                    return ans
            ans += pre[i]


        return ans