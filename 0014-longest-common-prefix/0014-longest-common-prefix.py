class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        prefix = ""
        for i in range(len(strs[0])):
            if all(x[i] == strs[0][i] for x in strs):
                prefix += strs[0][i]
            else:
                break
        return prefix
        