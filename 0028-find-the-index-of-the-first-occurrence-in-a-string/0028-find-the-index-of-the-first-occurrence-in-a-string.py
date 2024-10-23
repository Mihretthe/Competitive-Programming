class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n):
            index = i
            for j in range(m):
                if index < n and needle[j] == haystack[index]:
                    index += 1
                else:
                    break
            else:
                return i
        return -1


