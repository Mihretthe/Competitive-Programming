class Solution:
    def checkString(self, s: str) -> bool:
        return True if s=="".join(sorted(s)) else False