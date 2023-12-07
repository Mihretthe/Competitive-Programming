class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        at = 0
        ans = []
        for i in spaces:
          ans.append(s[at:i])
          ans.append(" ")
          at = i
        ans.append(s[at:])    

        return "".join(ans)